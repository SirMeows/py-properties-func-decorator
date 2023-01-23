# Properties in Python
# --------------------

# Verbose way, not Pythonic
# This was somewhat the way Java did it previously, 
# but now @Getter/@Setter annotations can be used

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

# Even though properties were marked 'private'
# They can still be accessed as normal (bad, don't do)
# both of the below methods work

point = Point(12, 5)

point.get_x() # result: 12
point.get_y() # result: 5

point._x # result: 12
point._y # result: 5

# Short 'Pythonic' version
# still fails to protect the attr

class Point:
     def __init__(self, x, y):
         self.x = x
         self.y = y

point = Point(12, 5)
point.x # result: 12
point.y # result: 5

# property() way

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        return self._radius

    def _set_radius(self, value):
        self._radius = value

    def _del_radius(self):
        del self._radius

    # this is the managed property!
    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

# what happens when we call the radius property now

circle = Circle(42.0)

circle.radius 
# calls fget --> 42
circle.radius = 365 
# calls fset
del circle.radius 
# deletes attribute
circle.radius 
# prints and err, obj. has no attr 'radius'


# property() as Decorator

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius