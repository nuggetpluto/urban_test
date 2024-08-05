def introsppection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]
    info['attributes'] = attributes
    info['methods'] = methods
    info['module'] = obj.__class__.__module__

    return info
# Example usage:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)



print(introsppection_info(person))
