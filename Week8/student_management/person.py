class Person:
    """
    A base class for a person with basic attributes like name and age.
    
    Attributes:
    -----------
    name : str
        The name of the person.
    age : int
        The age of the person.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
