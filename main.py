from object_factory.object_factory import ObjectFactory

# A valid class example is MyClass. Use any other class name to test the unknown class

obj = ObjectFactory.create_object("MyClass")
obj.do_something("my input")