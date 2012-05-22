"""

Configuration file for ssexy.

"""

class Api:
    def __init__(self, name, resets=False):
        """Define a new API.

        `name' is the name when linking.
        `resets' indicates if this API resets Xmm Registers, if so,
            registers should be stored temporarily.

        """
        self.name = name
        self.resets = resets

    def __str__(self):
        return self.name

apis = [
    ('SetUnhandledExceptionFilter', '_SetUnhandledExceptionFilter@4'),
    ('MessageBoxA', '_MessageBoxA@16', True),
    (('ws2_32.dll', 1), '_accept'),
    (('ws2_32.dll', 2), '_bind'),
    (('ws2_32.dll', 3), '_closesocket'),
    (('ws2_32.dll', 9), '_htons'),
    (('ws2_32.dll', 0x0d), '_listen'),
    (('ws2_32.dll', 0x10), '_recv'),
    (('ws2_32.dll', 0x17), '_socket'),
    (('ws2_32.dll', 0x73), '_WSAStartup'),
    ]

# convert each definition to an Api instance.
apis = dict([(x[0], Api(*x[1:])) for x in apis])