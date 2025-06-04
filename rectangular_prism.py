# Drake F
def calculate_volume(length, width, height):
    volume = length * height * width
    return volume


def calculate_surface_area(length, width, height):
    area = 2 * (length * width + length * height + width * height)
    return area


print("Welcome, this program will aid you in finding the volume of a rectangular prism")
length = 0.0
width = 0.0
height = 0.0
while length <= 0.0:
    try:
        length_str = input(" enter the length of the rectangular prism: ")
        length = float(length_str)
        if length <= 0.0:
            print("cannot have non positive side length")
    except:
        print(" cannot have invalid side length", length_str)
while height <= 0.0:
    try:
        height_str = input(" enter the height of the rectangular prism: ")
        height = float(height_str)
        if height <= 0.0:
            print(" cannot have non positive height")
    except:
        print("cannot have invalid height", height_str)
while width <= 0.0:
    try:
        width_str = input(" enter the width of the rectangular prism: ")
        width = float(width_str)
        if width <= 0.0:
            print(" cannot have non positive width")
    except:
        print("cannot have invalid width", width_str)

volume = calculate_volume(length, width, height)
print(" volume of the rectangular prism is", volume)

area = calculate_surface_area(length, width, height)
print(" surface area of the rectangular prism is", area)
