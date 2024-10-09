from factory.my_class import MyClass
from factory.null_class import NullClass


class ObjectFactory(object):
    @staticmethod
    def create_object(value):
        if value == "MyClass":
            return MyClass()
        else:
            return NullClass()