import math

def r_perimeter(length, width):
    return 2*length + 2*width

def r_area(length, width):
    return length*width

def c_perimeter_radius(radius):
    return 2*math.pi*radius

def c_perimeter_diameter(diameter):
    return c_perimeter_radius(diameter/2)

def c_area_radius(radius):
    return math.pi*(radius**2)

def c_area_diameter(diameter):
    return c_area_radius(diameter/2)

def how_much_paint(width, height, paintSqrFt):
    wallSqrFt = width*height
    return wallSqrFt/paintSqrFt

def how_many_paint_cans(width, height, paintSqrFt):
    paintGallons = how_much_paint(width,height,paintSqrFt)
    if (paintGallons % 1.0 != 0):
        return int(paintGallons +1)
    return int(paintGallons)
