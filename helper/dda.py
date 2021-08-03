import matplotlib.pyplot as plt
from prettytable import PrettyTable


def DDALine(x1, y1, x2, y2, color):
    dx = x2-x1
    dy = y2-y1

    if(dx==0 or dy==0):
        m = 0
    else:
        m = dy / dx
        minvers = 1 / m

    totalPoints = 1

    print("\nm = %.2f" %m,"-1<m<1 =",(m>-1 and m<1))
    pixels = []

    xk = x1
    yk = y1

    if(not m):
        if(dx==0):
            table = PrettyTable()
            print('The line is a vertical line')
            table.field_names = ['x', 'y(+1)', 'pixel']

            while(yk!=y2):
                totalPoints = totalPoints + 1
                table.add_row([xk, yk, (xk, yk)])
                #pixels.append((xk, yk))
                yk = yk-1 if y1 > y2 else yk+1
        else:
            table = PrettyTable()
            table.field_names = ['x(+1)', 'y', 'pixel']
            print('The line is a horizontal line')
            while(xk!=x2):
                totalPoints = totalPoints + 1
                table.add_row([xk, yk, (xk, yk)])
                pixels.append((xk, yk))

                xk = xk-1 if x1 > x2 else xk + 1

    elif(m > -1 and m < 1):
        print('The Line is not steep')
        table = PrettyTable()
        table.field_names = ['x(+1)', 'y(+m)', 'y(round off)', 'pixel']
        while(xk != x2 and yk != y2):
            totalPoints = totalPoints + 1
            table.add_row([xk, float("{:.1f}".format(yk)), int(round(yk)), (xk, int(round(yk)))])
            #pixels.append((xk, (int(round(yk)))))
            xk = xk+1
            yk = yk+m


    else:
        print('The Line is steep')
        table = PrettyTable()
        table.field_names = ['y(+1)', 'x(+1/m)', 'x(round off)', 'pixel']
        while(xk != x2 and yk != y2):
            totalPoints = totalPoints + 1
            table.add_row([yk, float("{:.1f}".format(xk)), int(round(xk)), (int(round(xk)), yk)])
            #pixels.append((int(round(xk)), yk))
            yk = yk+1
            xk = xk + minvers


    #print(pixels)
    print('\nTotal pixels : {}'.format(totalPoints))
    print(table)
    '''
    for points in pixels:
        plt.plot(points[0], points[1], color)
    plt.show()
    '''


def DDALineOnPoint(x1, y1, slope, color, steps):
    m = slope
    minvers = 1/m
    s = steps

    print("m = %.2f" %m,"-1<m<1 =",(m>-1 and m<1))
    pixels = []

    xk = x1
    yk = y1
    totalPoints = 0


    if(m > -1 and m < 1):
        while(s>0):
            totalPoints = totalPoints+1
            pixels.append((xk, (((yk)))))
            xk = xk+1
            yk = yk+m
            s = s-1

    else:
        while(s>0):
            totalPoints = totalPoints + 1
            pixels.append((((xk)), yk))
            yk = yk+1
            xk = xk + minvers
            s= s-1

    print(pixels)

    for points in pixels:
        plt.plot(points[0], points[1], color)
    plt.show()

def DDAvTsT(x1, y1, x2, y2, color):
    pixels = []
    dx = x2-x1
    dy = y2-y1

    #calculate steps required for generating pixels
    steps = abs(dx) > abs(dy) and abs(dx) or abs(dy)

    #calculate increment in x & y for each steps
    xinc = dx/ float(steps)
    yinc = dy/ float(steps)

    x = x1
    y = x2
    for i in range(0, steps+1):
        pixels.append((float(x), float(y)))
        plt.plot(float(x), float(y))
        x = x+xinc
        y = y+yinc

    print(pixels)
    plt.show()


def main():
    x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]
    x2, y2 = [int(x) for x in input('Enter x2, y2 : ').split()]
    color='r.'
    DDALine(x1, y1, x2, y2, color)
    #DDALineOnPoint(127, 61, 0.75, color, 5)
    #DDAvTsT(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()