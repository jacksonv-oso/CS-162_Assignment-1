'''
# CS-162 Assignment 1
# Vernon Jackson Smith
# 04/07/2024
'''

'''
Functions Reuse Exercise

Write a function named "rect_area" that computes the area of a rectangle.
This function will take 2 parameters - length and width.

Write a second function named "rect_surface_area" that calls the first function
- "rect_area" - to compute the surface area of a rectangular solid.
This function will take three parameters - length, width and height.

The main program will call the "rect_surface_area" with three parameters length, width and height.

The user input to the program will be three integers - length, width and height of a rectangular solid.

The program will print the length, width and height as input and the surface area of the entire rectangular 
solid.
'''


# Function 1.0
def rect_area(rectLength, rectWidth):
    rectLength = int(rectLength)
    rectWidth = int(rectWidth)
    '''
    Mental Note,
    To avoid "Type error" when dealing with strings and integers, designate incoming parameters
    to required datatypes.
    '''
    return rectLength*rectWidth

# Function 2.0
def rect_surface_area(rectLength, rectWidth, rectHeight):
    return 2*( (rect_area(rectLength, rectWidth)) + (rectLength*rectHeight) + (rectHeight*rectWidth) )

# Function 2.1
def rect_surface_area_2(rectLength, rectWidth, rectHeight):
    return 2*( (rect_area(rectLength, rectWidth)) + (rect_area(rectLength, rectHeight)) + (rect_area(rectHeight, rectWidth)) )

'''
print(rect_area(2,4))
print(rect_surface_area(2,4,6))
print(rect_surface_area_2(2,4,6))
'''

# Main Function
def main():
    length = input("Enter the length of the object as an integer: ")
    width = input("Enter the width of the object as an integer: ")
    height = input("Enter the height of the object as an integer: ")
    print("Length = ", length, " Width = ", width, "Height = ", height)
    print("Total Surface Area = ", rect_surface_area_2(length, width, height), "\n")

main()