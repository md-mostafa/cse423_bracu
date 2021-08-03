from prettytable import PrettyTable
from eightWaySymmetryM import *

table1 = PrettyTable()



def midPointCircle(radius,value):
    sum = 0
    totalSE = 0
    totalE =0
    table1.field_names = ['x', 'y', 'd', 'E/SE', 'd update', 'zone']
    d = 1-radius
    x =0
    y = radius


    print('x = ',x, 'y = ',y,'zone ',value)


    circlePoints = []



    while x < y:
        if d < 0:
            # choose E
            beforeupdatedd = d
            totalE = totalE+1

            d = d + 2 * x + 3
            table1.add_row([x, y, beforeupdatedd, 'E  ({0})'.format(totalE), d, value])
            circlePoints.append((x, y, value))
            x = x + 1
            sum = sum + 1

        else:
            # chose SE
            totalSE = totalSE + 1
            beforeupdatedd = d

            d = d + 2 * x - 2 * y + 5
            table1.add_row([x, y, beforeupdatedd, 'SE ({0})'.format(totalSE), d, value])
            circlePoints.append((x, y, value))
            x = x + 1
            y = y - 1

            sum = sum + 1



    #print(circlePoints)
    print(table1)
    print('-----------------------------------------------------')
    print('sum= ', sum)
    print('total SE = ', totalSE)
    print('total E = ', totalE)
    findAllEightZonePointsOfCircle(circlePoints)


def midPointCircleWithCenter(radius,xc, yc, value):

    totalSE = 0
    totalE =0
    table1.field_names = ['x+{0}'.format(xc), 'y+{0}'.format(yc), 'd', 'E/SE', 'd update', 'zone']
    d = 1-radius
    x =0
    y = radius


    #print('x = ',x, 'y = ',y,'zone ',value)


    circlePoints = []



    while x < y:

        if d < 0:
            # choose E
            beforeupdatedd = d
            totalE = totalE+1

            d = d + 2 * x + 3
            table1.add_row([x+xc, y+yc, beforeupdatedd, 'E', d, value])
            circlePoints.append((x+xc, y+yc, value))

            x = x + 1

        else:
            # chose SE
            beforeupdatedd = d

            d = d + 2 * x - 2 * y + 5
            table1.add_row([x+xc, y+yc, beforeupdatedd, 'SE', d, value])
            circlePoints.append((x+xc, y+yc, value))

            x = x + 1
            y = y - 1
            totalSE = totalSE+1


        sum = len(circlePoints)



    #print(circlePoints)
    print(table1)
    print('-----------------------------------------------------')
    print('sum= ', sum)
    print('totalse = ', totalSE)
    print('totale = ', totalE)
    findAllEightZonePointsOfCircle(circlePoints)








midPointCircle(int(input('Enter radius : ')), 1) #kaj kore
#midPointCircleWithCenter(29, -19, -29, 1)


