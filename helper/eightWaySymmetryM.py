import matplotlib.pyplot as plt
from prettytable import PrettyTable


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

def findZoneSinglePoint(x, y):
    dx = x
    dy = y

    if abs(dx) >= abs(dy):  # zone = 0, 3, 4, 7
        if dx >= 0 and dy >= 0:
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
    # table = PrettyTable()
    # table.field_names = ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 1])
    # print(table)
    return x, y

def convertToZone1(X, Y, zone):
    if zone == 1:
        x = X
        y = Y


    elif zone == 2:
        x = -X
        y = Y

    elif zone == 3:
        x = Y
        y = -X

    elif zone == 4:
        x = -Y
        y = -X

    elif zone == 5:
        x = -X
        y = -Y

    elif zone == 6:
        x = X
        y = -Y

    elif zone == 7:
        x = -Y
        y = X
    else:
        x = Y
        y = X
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 1])
    # print(table)
    return x, y

def convertToZone2(X, Y, zone):
    if zone == 1:
        x = -X
        y = Y

    elif zone == 2:
        x = X
        y = Y

    elif zone == 3:
        x = -Y
        y = -X

    elif zone == 4:
        x = Y
        y = -X

    elif zone == 5:
        x = X
        y = -Y

    elif zone == 6:
        x = -X
        y = -Y

    elif zone == 7:
        x = Y
        y = X
    else:
        x = -Y
        y = X
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 2])
    # print(table)
    return x, y

def convertToZone3(X, Y, zone):
    if zone == 1:
        x = -Y
        y = X

    elif zone == 2:
        x = -Y
        y = -X

    elif zone == 3:
        x = X
        y = Y

    elif zone == 4:
        x = X
        y = -Y

    elif zone == 5:
        x = Y
        y = -X

    elif zone == 6:
        x = Y
        y = X

    elif zone == 7:
        x = -X
        y = -Y
    else:
        x = -X
        y = Y
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 3])
    # print(table)
    return x, y

def convertToZone4(X, Y, zone):
    if zone == 1:
        x = -Y
        y = -X

    elif zone == 2:
        x = -Y
        y = X

    elif zone == 3:
        x = X
        y = -Y

    elif zone == 4:
        x = X
        y = Y

    elif zone == 5:
        x = Y
        y = X

    elif zone == 6:
        x = Y
        y = -X

    elif zone == 7:
        x = -X
        y = Y
    else:
        x = -X
        y = -Y
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 4])
    # print(table)
    return x, y

def convertToZone5(X, Y, zone):
    if zone == 1:
        x = -X
        y = -Y

    elif zone == 2:
        x = X
        y = -Y

    elif zone == 3:
        x = -Y
        y = X

    elif zone == 4:
        x = Y
        y = X

    elif zone == 5:
        x = X
        y = Y

    elif zone == 6:
        x = -X
        y = Y

    elif zone == 7:
        x = Y
        y = -X
    else:
        x = -Y
        y = -X
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 5])
    # print(table)
    return x, y

def convertToZone6(X, Y, zone):
    if zone == 1:
        x = X
        y = -Y

    elif zone == 2:
        x = -X
        y = -Y

    elif zone == 3:
        x = Y
        y = X

    elif zone == 4:
        x = -Y
        y = X

    elif zone == 5:
        x = -X
        y = Y

    elif zone == 6:
        x = X
        y = Y

    elif zone == 7:
        x = -Y
        y = -X
    else:
        x = Y
        y = -X
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 6])
    # print(table)
    return x, y

def convertToZone7(X, Y, zone):
    if zone == 1:
        x = Y
        y = -X

    elif zone == 2:
        x = Y
        y = X

    elif zone == 3:
        x = -X
        y = -Y

    elif zone == 4:
        x = -X
        y = Y

    elif zone == 5:
        x = -Y
        y = X

    elif zone == 6:
        x = -Y
        y = -X

    elif zone == 7:
        x = X
        y = Y
    else:
        x = X
        y = -Y
    # table = PrettyTable()
    # table.field_names =  ['x', 'y', 'orignalZone', 'x_converted', 'y_converted', 'convertedZone']
    # table.add_row([X, Y, zone, x, y, 7])
    # print(table)
    return x, y


def convertToGivenZoneSinglePoint(x, y, zoneToConvert):
    orignal_zone = findZoneSinglePoint(x, y)

    if zoneToConvert == 0:
        X, Y = convertToZone0(x, y, orignal_zone)
    elif zoneToConvert == 1:
        X, Y = convertToZone1(x, y, orignal_zone)
    elif zoneToConvert == 2:
        X, Y = convertToZone2(x, y, orignal_zone)
    elif zoneToConvert == 3:
        X, Y = convertToZone3(x, y, orignal_zone)
    elif zoneToConvert == 4:
        X, Y = convertToZone4(x, y, orignal_zone)
    elif zoneToConvert == 5:
        X, Y = convertToZone5(x, y, orignal_zone)
    elif zoneToConvert == 6:
        X, Y = convertToZone6(x, y,  orignal_zone)
    elif zoneToConvert == 7:
        X, Y = convertToZone7(x, y, orignal_zone)


def convertToGivenZone(x, y, originalZone, zoneToConvert):
    orignal_zone = originalZone

    if zoneToConvert == 0:
        X, Y = convertToZone0(x, y, orignal_zone)
    elif zoneToConvert == 1:
        X, Y = convertToZone1(x, y, orignal_zone)
    elif zoneToConvert == 2:
        X, Y = convertToZone2(x, y, orignal_zone)
    elif zoneToConvert == 3:
        X, Y = convertToZone3(x, y, orignal_zone)
    elif zoneToConvert == 4:
        X, Y = convertToZone4(x, y, orignal_zone)
    elif zoneToConvert == 5:
        X, Y = convertToZone5(x, y, orignal_zone)
    elif zoneToConvert == 6:
        X, Y = convertToZone6(x, y,  orignal_zone)
    elif zoneToConvert == 7:
        X, Y = convertToZone7(x, y, orignal_zone)

    table = PrettyTable()
    table.field_names = ['x', 'y', 'originalZone', 'x_converted', 'y_converted', 'zoneToConvert']
    table.add_row([x, y, orignal_zone, X, Y, zoneToConvert])
    print(table)


def findAllZoneGivenPoint(x, y):
    originalZone = findZoneSinglePoint(x, y)
    table = PrettyTable()
    table.align ="c"

    table.field_names = ['(x, y)', 'orignalZone', 'converted(x, y)', 'convertedZone']

    X, Y = convertToZone0(x, y, originalZone)
    table.add_row([(x, y),originalZone, (X, Y), '0'])

    X, Y = convertToZone1(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '1'])

    X, Y = convertToZone2(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '2'])

    X, Y = convertToZone3(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '3'])

    X, Y = convertToZone4(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '4'])

    X, Y = convertToZone5(x, y, originalZone)
    table.add_row([(x, y), originalZone,(X, Y), '5'])

    X, Y = convertToZone6(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '6'])

    X, Y = convertToZone7(x, y, originalZone)
    table.add_row([(x, y), originalZone, (X, Y), '7'])


    print(table)




def findAllEightZonePointsOfCircle(crPoints):
    table = PrettyTable()
    table.field_names = ['Zone 0', 'Zone 1', 'Zone 2 ', 'Zone 3', 'Zone 4', 'Zone 5', 'Zone 6', 'Zone 7']

    for point in crPoints:
        X0, Y0 = convertToZone0(point[0], point[1], point[2])
        X1, Y1 = convertToZone1(point[0], point[1], point[2])
        X2, Y2 = convertToZone2(point[0], point[1], point[2])
        X3, Y3 = convertToZone3(point[0], point[1], point[2])
        X4, Y4 = convertToZone4(point[0], point[1], point[2])
        X5, Y5 = convertToZone5(point[0], point[1], point[2])
        X6, Y6 = convertToZone6(point[0], point[1], point[2])
        X7, Y7 = convertToZone7(point[0], point[1], point[2])

        table.add_row([(X0, Y0), (X1, Y1), (X2, Y2), (X3, Y3), (X4, Y4), (X5, Y5), (X6, Y6), (X7, Y7)])


    print(table)





#findAllZoneGivenPoint(45, -50)

#convertToGivenZone(113, -28, 4, 0)

'''

# (-10, -20) to (-20, 70)
x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]
x2, y2 = [int(x) for x in input('Enter x2, y2 : ').split()]
# drawMidPointLine(x1, y1, x2, y2)

'''
'''

x, y = convertToZone0(50, 5, 0)
x, y = convertToZone0(5, 50, 1)
x, y = convertToZone0(-5, 50, 2)
x, y = convertToZone0(-50, 5, 3)
x, y = convertToZone0(-50, -5, 4)
x, y = convertToZone0(-5, -50, 5)
x, y = convertToZone0(5, -50, 6)
x, y = convertToZone0(50, -5, 7)


x, y = convertToZone1(50, 5, 0)
x, y = convertToZone1(5, 50, 1)
x, y = convertToZone1(-5, 50, 2)
x, y = convertToZone1(-50, 5, 3)
x, y = convertToZone1(-50, -5, 4)
x, y = convertToZone1(-5, -50, 5)
x, y = convertToZone1(5, -50, 6)
x, y = convertToZone1(50, -5, 7)

x, y = convertToZone2(50, 5, 0)
x, y = convertToZone2(5, 50, 1)
x, y = convertToZone2(-5, 50, 2)
x, y = convertToZone2(-50, 5, 3)
x, y = convertToZone2(-50, -5, 4)
x, y = convertToZone2(-5, -50, 5)
x, y = convertToZone2(5, -50, 6)
x, y = convertToZone2(50, -5, 7)

x, y = convertToZone3(50, 5, 0)
x, y = convertToZone3(5, 50, 1)
x, y = convertToZone3(-5, 50, 2)
x, y = convertToZone3(-50, 5, 3)
x, y = convertToZone3(-50, -5, 4)
x, y = convertToZone3(-5, -50, 5)
x, y = convertToZone3(5, -50, 6)
x, y = convertToZone3(50, -5, 7)

x, y = convertToZone4(50, 5, 0)
x, y = convertToZone4(5, 50, 1)
x, y = convertToZone4(-5, 50, 2)
x, y = convertToZone4(-50, 5, 3)
x, y = convertToZone4(-50, -5, 4)
x, y = convertToZone4(-5, -50, 5)
x, y = convertToZone4(5, -50, 6)
x, y = convertToZone4(50, -5, 7)

x, y = convertToZone5(50, 5, 0)
x, y = convertToZone5(5, 50, 1)
x, y = convertToZone5(-5, 50, 2)
x, y = convertToZone5(-50, 5, 3)
x, y = convertToZone5(-50, -5, 4)
x, y = convertToZone5(-5, -50, 5)
x, y = convertToZone5(5, -50, 6)
x, y = convertToZone5(50, -5, 7)


x, y = convertToZone6(50, 5, 0)
x, y = convertToZone6(5, 50, 1)
x, y = convertToZone6(-5, 50, 2)
x, y = convertToZone6(-50, 5, 3)
x, y = convertToZone6(-50, -5, 4)
x, y = convertToZone6(-5, -50, 5)
x, y = convertToZone6(5, -50, 6)
x, y = convertToZone6(50, -5, 7)

x, y = convertToZone7(50, 5, 0)
x, y = convertToZone7(5, 50, 1)
x, y = convertToZone7(-5, 50, 2)
x, y = convertToZone7(-50, 5, 3)
x, y = convertToZone7(-50, -5, 4)
x, y = convertToZone7(-5, -50, 5)
x, y = convertToZone7(5, -50, 6)
x, y = convertToZone7(50, -5, 7)

'''




