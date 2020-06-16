class MyClass:
    n_objects = 0

    def __new__(cls):
        if MyClass.n_objects < 5:
            MyClass.n_objects += 1
            return object.__new__(cls)
        return None

    def __str__(self):
        return "An object of MyClass"