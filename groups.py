import re  # NOQA
from libqtile.config import Group, Match  # NOQA
from layouts import Layouts  # NOQA


class Groups(object):

    ##### GROUPS #####

    def init_groups(self):
        layout = Layouts()

        return [
            Group("1",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ]
                  ),
            Group("2",
                  layouts=[
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.ten_monadWide(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()

                  ],
                  ),
            Group("3",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],
                  ),
            Group("4",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],

                  ),
            Group("5",
                  layouts=[
                      layout.max()
                  ],

                  ),
            Group("6",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ]
                  ),
            Group("7",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],

                  ),
            Group("8",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],

                  ),
            Group("9",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],

                  ),
            Group("0",
                  layouts=[
                      layout.max(),
                      layout.two_stackWide(),
                      layout.two_stackTall(),
                      layout.monadWide(),
                      layout.monadTall(),
                      layout.two_stackTall(),
                      layout.monadTall(),
                      layout.five_monadTall(),
                      layout.two_stackTall(),
                      layout.two_stackWide(),
                      layout.floating()
                  ],
                  ),
            Group("",
                  layouts=[
                      layout.floating()
                  ]
                  )
        ]

# vim: tabstop=4 shiftwidth=4 noexpandtab
