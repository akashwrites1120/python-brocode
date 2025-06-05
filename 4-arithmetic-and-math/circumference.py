

#                   ***********************Calculate Circumference of a circle ***************************

import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

# print(f"The circumference is: {circumference:.2f} ")    #F-strings provide a concise way to format numbers within strings.
                                                        # You can use the format specifier :.2f to round a number to two decimal places.

print(f"The curcumference is: {round(circumference,2)}cm ")
