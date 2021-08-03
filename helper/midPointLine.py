import matplotlib.pyplot as plt
from prettytable import PrettyTable


def midPointLine(x0, y0, x1, y1, value):
    pixels = []
    color = 'r.'

    dx = x1-x0
    dy = y1-y0
    d = 2*dy - dx
    incrE = 2*dy
    incrNE = 2*(dy-dx)
    x = x0
    y = y0

    totalE = 0
    totalNE = 0
    incre = 1

    table = PrettyTable()
    table.field_names = ['x', 'y', 'd', 'NE(+1,+1)/E(+1,0)', 'd updating', 'pixel']

    while(x<=x1):
        bd = d
        #pixels.append((x, y))
        plt.plot(x, y, color)

        if d<=0:

            d = d + incrE
            table.add_row([x, y, bd, 'E   ({0})'.format(totalE+1), d, (x, y)])
            x = x+1

            incre = incre+1
            totalE = totalE + 1
        else:

            d = d+incrNE
            table.add_row([x, y, bd, 'NE  ({0})'.format(totalNE+1), d, (x, y)])
            x = x+1
            y = y+1

            incre = incre+1
            totalNE = totalNE + 1


        value = value - 1
        if(value==0):
            break

    print(table)
    #print(pixels)
    print('Total E : ',totalE)
    print('Total NE : ', totalNE)

    showPlot = input('Do you want to see th graph : ')
    if showPlot.lower() == 'yes':
        plt.show()


x1, y1 = [int(x) for x in input('Enter x0, y0 : ').split()]
x2, y2 = [int(x) for x in input('Enter x1, y1 : ').split()]

value = int(input('Number of points :  '))

midPointLine(x1, y1, x2, y2, value)
