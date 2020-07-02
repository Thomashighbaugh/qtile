from libqtile.widget.base import _TextBox, ThreadedPollText
from libqtile.widget.mpriswidget import Mpris
from libqtile.widget.battery import Battery
#from libqtile.widget.wlan import Wlan, Wireless
#from libqtile.widget import GoogleCalendar
from libqtile import bar
from libqtile import config as settings
from libqtile.pangocffi import markup_escape_text
import dbus
import os
import re
import platform
from collections import defaultdict
#from cache import configure_cache
import subprocess
from tasklib import TaskWarrior, local_zone, Task
from datetime import datetime, timedelta
import html


# Taken from: https://github.com/qtile/qtile-examples/blob/master/user-configs/ei-grad/config.py
class Metrics(ThreadedPollText):
    defaults = [
        ("font", "Arial", "Metrics font"),
        ("fontsize", None, "Metrics pixel size. Calculated if None."),
        ("fontshadow", None, "font shadow color, default is None(no shadow)"),
        ("padding", None, "Metrics padding. Calculated if None."),
        ("background", "000000", "Background colour"),
        ("foreground", "ffffff", "Foreground colour"),
        ("cpu_label_foreground", "#5555dd", "CPU stat label foreground color"),
        ("mem_label_foreground", "#5555dd", "Mem stat label foreground color"),
        ("net_label_foreground", "#5555dd", "Net stat label foreground color"),
        ("download_foreground", "#5555dd", "Color for the download reading"),
        ("upload_foreground", "#5555dd", "Color for the upload reading"),
        ("separator_color", "#444444", "Separator colour"),
        ('update_interval', 1, 'The update interval.'),
    ]

    def __init__(self, **config):
        super(Metrics, self).__init__(**config)
        self.add_defaults(self.defaults)
        self.cpu_usage, self.cpu_total = self.get_cpu_stat()
        self.interfaces = {}
        self.idle_ifaces = {}

    def _configure(self, qtile, bar):
        super(Metrics, self)._configure(qtile, bar)
        self.layout = self.drawer.textlayout(
            self.text, self.foreground, self.font,
            self.fontsize, self.fontshadow, markup=True)

    def get_cpu_stat(self):
        stat = [int(i) for i in open('/proc/stat').readline().split()[1:]]
        return sum(stat[:3]), sum(stat)

    def get_cpu_usage(self):
        new_cpu_usage, new_cpu_total = self.get_cpu_stat()
        cpu_usage = new_cpu_usage - self.cpu_usage
        cpu_total = new_cpu_total - self.cpu_total
        self.cpu_usage = new_cpu_usage
        self.cpu_total = new_cpu_total
        return '<span weight="bold" color="%s">Cpu:</span> %3d%%' % (self.cpu_label_foreground, float(cpu_usage) / float(cpu_total) * 100.)

    def get_mem_usage(self):
        info = {}
        for line in open('/proc/meminfo'):
            key, val = line.split(':')
            info[key] = int(val.split()[0])
        mem = info['MemTotal']
        mem -= info['MemFree']
        mem -= info['Buffers']
        mem -= info['Cached']
        return '<span weight="bold" color="%s">Mem:</span> %d%% <span color="#444444">%s/%s</span>' % (self.mem_label_foreground, float(mem) / float(info['MemTotal']) * 100, humanize_bytes(float(mem) * 1000), humanize_bytes(float(info['MemTotal']) * 1000))

    def get_load_avg(self):
        stat = open('/proc/loadavg').readline().split(" ")[:3]
        return '<span weight="bold" color="{cpu_label_foreground}">Load Avg:</span> {stat}'.format(stat=", ".join(stat), cpu_label_foreground=self.cpu_label_foreground)

    #@cache.cache_on_arguments()
    def read_sensors(self):
        # TODO: Find another sensor library, this one breaks qtile
        results = defaultdict(dict)
        # sensors.init()

        # for chip in sensors.ChipIterator():
        #     chip_name = chip.prefix.decode('utf-8')
        #     if chip_name.startswith('nouveau'):
        #         continue
        #     for feature in sensors.FeatureIterator(chip):
        #         sfs = list(sensors.SubFeatureIterator(chip, feature))
        #         label = sensors.get_label(chip, feature).encode('utf-8')
        #         vals = [sensors.get_value(chip, sf.number) for sf in sfs]
        #         skipname = len(feature.name) + 1  # skip common prefix
        #         names = [sf.name[skipname:].encode("utf-8") for sf in sfs]
        #         data = dict(zip(names, vals))
        #         results[chip_name][label] = data.get('input')

        # sensors.cleanup()

        return results

    def format_fan_speed(self, sensors_output=None):
        if not sensors_output:
            sensors_output = self.read_sensors()
        template = '<span weight="bold" color="{cpu_label_foreground}">Fan:</span> {fan_speed:.1f} RPM'
        return template.format(cpu_label_foreground=self.cpu_label_foreground,
                               fan_speed=sensors_output.get('thinkpad', {}).get('fan1', -1))

    def format_cpu_temp(self, sensors_output=None):
        if not sensors_output:
            sensors_output = self.read_sensors()
        template = '<span weight="bold" color="{cpu_label_foreground}">Temp:</span> {avg_temp:.0f}C'
        # core_temps = {label: value for label, value in sensors_output.get('coretemp',
        #                                                                   {}).items() if label.startswith('Core')}
        return template.format(cpu_label_foreground=self.cpu_label_foreground,
                               avg_temp=sensors_output.get('coretemp', {}).get('Physical id 0', 0))
                               # avg_temp=sum(val for val in core_temps.values()) / len(core_temps))

    def get_net_usage(self):
        interfaces = []
        basedir = '/sys/class/net'
        for iface in os.listdir(basedir):
            if iface == "lo": continue
            if iface.startswith(tuple(['veth', 'docker', 'br'])): continue
            j = os.path.join
            ifacedir = j(basedir, iface)
            statdir = j(ifacedir, 'statistics')
            idle = iface in self.idle_ifaces
            try:
                if int(open(j(ifacedir, 'carrier')).read()):
                    rx = int(open(j(statdir, 'rx_bytes')).read())
                    tx = int(open(j(statdir, 'tx_bytes')).read())
                    if iface not in self.interfaces:
                        self.interfaces[iface] = (rx, tx)
                    old_rx, old_tx = self.interfaces[iface]
                    self.interfaces[iface] = (rx, tx)
                    rx = rx - old_rx
                    tx = tx - old_tx
                    if rx or tx:
                        idle = False
                        self.idle_ifaces[iface] = 0
                        rx = humanize_bytes(rx)
                        tx = humanize_bytes(tx)
                        text = '<span weight="bold" color="{net_label_foreground}">{iface}:</span>' + \
                          ' <span color="{download_foreground}">{rx}</span> / <span color="{upload_foreground}">{tx}</span>'
                        text = text.format(net_label_foreground=self.net_label_foreground, iface=iface, rx=rx, tx=tx,
                                           upload_foreground=self.upload_foreground, download_foreground=self.download_foreground)
                        interfaces.append(text)
            except:
                pass
            if idle:
                text = '<span weight="bold" color="{net_label_foreground}">{iface}:</span>' + \
                    ' <span color="{download_foreground}">{rx}</span> / <span color="{upload_foreground}">{tx}</span>'
                text = text.format(net_label_foreground=self.net_label_foreground, iface=iface, rx=humanize_bytes(0), tx=humanize_bytes(0),
                                   upload_foreground=self.upload_foreground, download_foreground=self.download_foreground)
                interfaces.append(text)
                self.idle_ifaces[iface] += 1
                if self.idle_ifaces[iface] > 30:
                    del self.idle_ifaces[iface]
        return ('<span color="%s"> | </span>' % (self.separator_color)).join(interfaces)

    def poll(self):
        text = ""
        stat = []
        # sensors_output = self.read_sensors()
        stat = [self.get_cpu_usage(),  # self.format_cpu_temp(sensors_output), self.format_fan_speed(sensors_output),
                self.get_mem_usage(), self.get_load_avg()]
        net = self.get_net_usage()
        if net:
            stat.append(net)
        text = ('<span color="%s"> | </span>' % (self.separator_color)).join(stat)

        return text

