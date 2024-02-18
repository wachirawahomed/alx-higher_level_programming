# 0x0C - Python - Almost a circle

##Task 0
All your files, classes and methods must be unit tested and be PEP 8 validated.

##Task 1
Write the first class `Base`:

##Task 2
Write the class `Rectangle` that inherits from `Base`:

##Task 3
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

##Task 4
Update the class `Rectangle` by adding the public method `def area(self):`

##Task 5
Update the class `Rectangle` by adding the public method `def display(self):`

##Task 6
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

##Task 7
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the Rectangle instance with the character `#` by taking care of `x` and `y`

##Task 8
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:
* 1st argument should be the `id` attribute
* 2nd argument should be the `width` attribute
* 3rd argument should be the `height` attribute
* 4th argument should be the `x` attribute
* 5th argument should be the `y` attribute

##Task 9
Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

##Task 10
Write the class `Square` that inherits from `Rectangle`:

* In the file `models/square.py`
* Class `Square` inherits from `Rectangle`
* Class constructor: `def __init__(self, size, x=0, y=0, id=None):`:
    * Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` must be assigned to the value of `size`
    * You must not create new attributes for this class, use all attributes of `Rectangle` - As reminder: a Square is a Rectangle with the same width and height
    * All `width`, `height`, `x` and `y` validation must inherit from `Rectangle` - same behavior in case of wrong data
* The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`

