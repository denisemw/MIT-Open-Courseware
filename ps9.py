# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
            h: length of side of the square
            """
        self.side = float(h)
    def area(self):
        """
            Returns area of the square
            """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
            Two squares are equal if they have the same dimension.
            other: object to check for equality
            """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
            radius: radius of the circle
            """
        self.radius = float(radius)
    def area(self):
        """
            Returns approximate area of the circle
            """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
            Two circles are equal if they have the same radius.
            other: object to check for equality
            """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def area(self):
        return (self.height*self.base) / 2

    def __str__(self):
        return 'Triangle with base ' + str(self.base) +' and height ' + str(self.height)

    def __eq__(self, other):
        return type(other) == Triangle and self.height == other.height and self.base == other.base
    

#
# Problem 2: Create the ShapeSet class
#

class ShapeSet:
    def __init__(self):
        """
            Initialize any needed variables
            """

        self.set = []
        
    def addShape(self, sh):
        """
            Add shape sh to the set; no two shapes in the set may be
            identical
            sh: shape to be added
            """

        for s in self.set:
            if s == sh:
                return
            
        self.set.append(sh)
        
    def __iter__(self):
        """
            Return an iterator that allows you to iterate over the set of
            shapes, one shape at a time
            """

        for s in self.set:
            yield s
        
    def __str__(self):
        """
            Return the string representation for a set, which consists of
            the string representation of each shape, categorized by type
            (circles, then squares, then triangles)
            """
        circles = []
        squares = []
        triangles = []

        for s in self.set:
            if type(s)==Circle:
                circles.append(s)
            if type(s)==Square:
                squares.append(s)
            if type(s)==Triangle:
                triangles.append(s)

        text = ''
        for c in circles:
            text += (str(c) + '\n')
        for s in squares:
            text += (str(s) + '\n')
        for t in triangles:
            text += (str(t) + '\n')

        return text

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
        Returns a tuple containing the elements of ShapeSet with the
        largest area.
        shapes: ShapeSet
        """
    maxArea = 0
    for s in shapes:
        if s.area() >= maxArea:
            maxArea = s.area()
    largest = ()
    for s in shapes:
        if s.area() >= maxArea:
            largest += (s,)
    return largest


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
        Retrieves shape information from the given file.
        Creates and returns a ShapeSet with the shapes found.
        filename: string
        """

    inputFile = open(filename)
    shapes = ShapeSet()
    for line in inputFile:
        line = line.strip()
        s = line.split(',')
        name = s[0]
        if name=='triangle':
            t = Triangle(s[1], s[2])
            shapes.addShape(t)
        elif name=='circle':
            c = Circle(s[1])
            shapes.addShape(c)
        else:
            square = Square(s[1])
            shapes.addShape(square)
    return shapes


ss = readShapesFromFile('shapes.txt')
largest = findLargest(ss)
print 'largest:'
for shape in largest:
    print shape


