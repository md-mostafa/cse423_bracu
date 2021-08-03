# Python program to implement Cohen Sutherland algorithm
# for line clipping.

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_min, y_min = [int(x) for x in input('Enter xmin, ymin : ').split()]
x_max, y_max = [int(x) for x in input('Enter xmax, ymax : ').split()]


def findOutCode():
    x, y = [int(x) for x in input('Enter x, y  to find outcode : ').split()]
    out = computeCode(x, y)
    print('OutCode : ', bin(out)[2:].zfill(4))


# Function to compute region code for a point(x, y)
def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohenSutherlandClip(x1, y1, x2, y2):
    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    print('\nOutcode 1 for (%.2f, %.2f) = %s' % (x1, y1, bin(code1)[2:].zfill(4)))
    print('Outcode 2 for (%.2f, %.2f) = %s' % (x2, y2, bin(code2)[2:].zfill(4)))
    print('Outcode 1 AND Outcode 2 = %s\n'% bin(code1&code2)[2:].zfill(4))
    accept = False

    while True:

        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            print('Line is Completely inside')
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            print('Line is Completely outside')
            break

        # Some segment lies within the rectangle
        else:

            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_min - x1) / (x2 - x1)
                x = x_min

            # Now intersection point x, y is found
            # We replace point outside clipping rectangle
            # by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
                print('Outcode 1 for (%.2f, %.2f) = %s [recalulated]' %(x1, y1, bin(code1)[2:].zfill(4)))
                print('Outcode 2 for (%.2f, %.2f) = %s' % (x2, y2, bin(code2)[2:].zfill(4)))
                print('Outcode 1 AND Outcode 2 = %s\n' % bin(code1 & code2)[2:].zfill(4))

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
                print('Outcode 1 for (%.2f, %.2f) = %s' % (x1, y1, bin(code1)[2:].zfill(4)))
                print('Outcode 2 for (%.2f, %.2f) = %s [recalculated]' % (x2, y2, bin(code2)[2:].zfill(4)))
                print('Outcode 1 AND Outcode 2 = %s\n' % bin(code1 & code2)[2:].zfill(4))

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))

    # Here the user can add code to display the rectangle
    # along with the accepted (portion of) lines

    else:
        print("Line rejected")

x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]
x2, y2 = [int(x) for x in input('Enter x2, y2 : ').split()]

cohenSutherlandClip(x1, y1, x2, y2)

#findOutCode()
