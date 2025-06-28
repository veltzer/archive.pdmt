"""
This is an arguments object to be given to be executed
(to run a compiler, linker, whatever)

Why do we need such an object?
- to allow to easily add configs to the command line
- to help quoting various things
- to help explain on the command line which parts are important and which
  are not.
- help us to invoke the compiler just once if multiple files need to
    be built? Compilers currently dont support this but maybe
    in the future they will.
"""


class Arguments:
    def __init__(self, mgr=None):
        super().__init__()
        self.mgr = mgr
        self.args = []

    def getConfigValue(self, cfgname):
        return self.mgr.get_node_by_name('cfg://' + cfgname).get_value()

    def append(self, arg):
        self.args.append(arg)

    def appendConfig(self, cfgname):
        self.args.append(self.getConfigValue(cfgname))

    def appendConfigIfNotEmpty(self, cfgname):
        val = self.getConfigValue(cfgname)
        if val != '':
            self.args.append(val)

    def __str__(self):
        return 'arguments'
