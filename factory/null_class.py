from factory.abs_class import AbsClass


class NullClass(AbsClass):
    def do_something(self, value="No value provided"):
        print("Cannot execute with: {}".format(value))