# run the file to understand it more


class M(type):
    def __call__(cls, *args, **kwargs):
        """
        This method will be called when you try to create an instance of the class that has M as metaclass
        """
        print("\n\nMetaclass __call__ pre super\n\tClass is:", cls)
        res = super().__call__(*args, **kwargs)  # here will be called __new__ of class A
        print("\nMetaclass __call__ post super\n\tResult of super is", res)
        return res

    def __new__(cls, *args, **kwargs):
        """
        This pretty function will be called when you define a class with M as metaclass
        (in the example this class is A)
        """
        print("\n\nMetaclass __new__ pre super\n\tClass is:", cls)
        print("\targs:", args)
        print("\tkwargs:", kwargs)
        res = super().__new__(cls, *args, **kwargs)
        print("\nMetaclass __new__ post super\n\tResult of super is:", res)
        return res

    def __init__(self, *args, **kwargs):
        """
        This will be called by M class __new__ function
        """
        print("\n\nMetaclass __init__\n\tSelf is:", self)
        print("\targs:", args)
        print("\tkwargs:", kwargs)
        super().__init__(*args, **kwargs)


class A(metaclass=M):
    """
    WHEN you DEFINE a CLASS with metaclass - it calls METACLASSES __new__ method.
    Think about it like "When I write `class MyClass: pass` it calls __new__ method of metaclass"
    """
    def __new__(cls,  *args, **kwargs):
        print("\n\t\tOur class __new__")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print("\t\tOur class __init__")


# try to comment and compare to original messages
A()
