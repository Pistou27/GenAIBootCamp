import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Vous devez mettre un rayon ou diamètre pour ce cercle")
        
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2
        
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"

    def __add__(self, other_circle):
        if not isinstance(other_circle, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other_circle.radius)
    
    def __lt__(self, other_circle):
        if not isinstance(other_circle, Circle):
            return NotImplemented
        return self.radius < other_circle.radius
    
    def __eq__(self, other_circle):
        if not isinstance(other_circle, Circle):
            return NotImplemented
        return self.radius == other_circle.radius
