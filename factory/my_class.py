from factory.abs_class import AbsClass


class MyClass(AbsClass):
    def do_something(self, value="No value provided"):
        print("Execute with: {}".format(value))