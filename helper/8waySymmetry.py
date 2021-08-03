import matplotlib.pyplot as plt
from prettytable import PrettyTable
from eightWaySymmetryM import *

def drawMidPointLine(x1,y1, x2, y2):
    table = PrettyTable()
    table.field_names = ['xp', 'yp', 'D', 'X', 'Y']

    convertedxylist = []
    zone = findZone(x1, y1,x2, y2)

    drawxylist =[]
    dlist = []

    converted_x1, converted_y1 = convertToZone0(x1, y1, zone)
    converted_x2, converted_y2 = convertToZone0(x2, y2, zone)

    x = converted_x1
    y = converted_y1

    dx = converted_x2 - converted_x1
    dy = converted_y2 - converted_y1


    d = (2*dy) - dx
    dE = 2*dy
    dNE = 2*dy - 2*dx

    xp, yp = originalZone(x, y, zone)
    drawxylist.append((xp, yp))
    dlist.append(d)
    table.add_row([x, y, d, xp, yp])        #x, y = converted to zone zero #xp, yp = converted to original zone
    while(x<=converted_x2):
        convertedxylist.append((x, y))

        if d<0:
            x = x+1
            d = d+dE
        else:
            x = x+1
            y = y+1
            d = d+dNE
        xp, yp = originalZone(x, y, zone)
        dlist.append(d)
        drawxylist.append((xp, yp))
        table.add_row([x, y,d, xp, yp])

    #print(drawxylist)
    print(table)


def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy): #zone = 0, 3, 4, 7
        if dx >=0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        else:
            zone = 6
    return zone


def convertToZone0(X, Y, zone):
    if zone == 1:
        x = Y
        y = X

    elif zone == 2:
        x = Y
        y = -X

    elif zone == 3:
        x = -X
        y = Y

    elif zone == 4:
        x = -X
        y = -Y

    elif zone == 5:
        x = -Y
        y = -X

    elif zone == 6:
        x = -Y
        y = X

    elif zone == 7:
        x = X
        y = -Y
    else:
        x = X
        y = Y
    return x, y



def originalZone(X, Y, zone):
    drawxylist = []
    if zone == 1:
        x = Y
        y = X

    elif zone == 2:
        x = -Y
        y = X

    elif zone == 3:
        x = -X
        y = Y

    elif zone == 4:
        x = -X
        y = -Y

    elif zone == 5:
        x = -Y
        y = -X

    elif zone == 6:
        x = Y
        y = -X

    elif zone == 7:
        x = X
        y = -Y
    else:
        x = X
        y = Y
    drawxylist.append((x, y))
    return x, y






#(-10, -20) to (-20, 70)
x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]
x2, y2 = [int(x) for x in input('Enter x2, y2 : ').split()]
drawMidPointLine(x1, y1, x2, y2)

