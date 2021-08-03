import math
from prettytable import PrettyTable

xmin, ymin = [int(x) for x in input('Enter xmin, ymin : ').split()]
xmax, ymax = [int(x) for x in input('Enter xmax, ymax : ').split()]

def tLeft(x0, x1, xmin):
    r = -1*(x0-xmin)
    r = r/(x1-x0)
    return r

def tRight(x0, x1, xmax):
    r = -1*(x0-xmax)
    r = r/(x1-x0)
    return r

def tTop(y0, y1, ymax):
    r = -1*(y0-ymax)
    r = r/(y1-y0)
    return r

def tBottom(y0, y1, ymin):
    r = -1*(y0-ymin)
    r = r/(y1-y0)
    return r

nilist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
nidList = []


def cyrus_beck():
    x0, y0 = [int(x) for x in input('Enter x0, y0 : ').split()]
    x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]

    table = PrettyTable()
    table.field_names = ['Ni', 'NiD', 't', 'PE/PL','tE', 'tL', 'tE-tL', 'tL-tE']
    D = ((x1-x0), (y1-y0))
    print('\nD =',D)

    for i in range(4):
        if i < 2:
            nidList.append(nilist[i][0] * D[0])
        else:
            nidList.append(nilist[i][1] * D[1])


    if(x1==x0 and y1==y0):
        print('line is degenerated, so clip as a point')
    else:
        tE = 0
        tL = 1
        t=0
        PE_PL=''

        for (nid, ni) in zip(nidList, nilist):
            if nid != 0:    #ignore edges parallel to line
                if ni[0] == -1:
                    t = float("{:.3f}".format(tLeft(x0, x1, xmin)))
                elif ni[0] ==1 :
                    t = float("{:.3f}".format(tRight(x0, x1, xmax)))
                elif ni[1] == -1:
                    t = float("{:.3f}".format(tBottom(y0, y1, ymin)))
                elif ni[1] == 1:
                    t = float("{:.3f}".format(tTop(y0, y1, ymax)))

            PE_PL = nid < 0 and 'PE' or 'PL'
            if PE_PL == 'PE':
                tE = max(tE, t)
            elif PE_PL == 'PL':
                tL = min(tL, t)
            tE_minus_tL = float("{:.3f}".format(tE-tL))
            tL_minus_tE = float("{:.3f}".format(tL-tE))
            table.add_row([ni, nid, t, PE_PL, tE, tL, tE_minus_tL, tL_minus_tE])
        if(tE > tL):
            print('Since tE > tL line segment is outside clip window')
            print(table)
            return None
        else:
            print('\nP(tE)=%.2f and P(tL)=%.2f true intersection' %(tE, tL))
            ptE = (float("{:.3f}".format(x0+tE*D[0])), float("{:.3f}".format(y0+tE*D[1])))
            ptL = (float("{:.3f}".format(x0+tL*D[0])), float("{:.3f}".format(y0+tL*D[1])))
            print('p(tE) = ',ptE)
            print('p(tL) = ',ptL)


            print('\n{0} and {1} are the endpoints of the clipped line'.format(ptE, ptL))
            l = (((float(ptL[0]) - float(ptE[0]))**2) + ((float(ptL[1])-float(ptE[1]))**2))**0.5
            l = float("{:.3f}".format(l))

            print('The length of the line {0}'.format(l))

        print(table)




def findParametricEquation():
    print('Parametric Equation : ')
    x0, y0 = [int(x) for x in input('Enter x0, y0 : ').split()]
    x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]

    xc = '{0} {1} {2}t'.format(x0, '+' if x1>x0 else '-',abs(x1-x0))
    yc = '{0} {1} {2}t'.format(x0, '+' if y1>y0 else '-',abs(y1-y0))

    print('p(t) = ({0}, {1})'.format(xc, yc))

    t = float(input('Enter t : '))
    if t:
        xt = x0+t*(x1-x0)
        #xt = float('{:.2f}'.format(xt))
        yt = y0+t*(y1-y0)
        #xt = float('{:.2f}'.format(yt))
        pt = (xt, yt)
        print('p({0}) = {1}'.format(t, pt))
    else:
        print('nothing')


# x0, y0 =[int(x) for x in input('Enter x0, y0 : ').split()]
# x1, y1 = [int(x) for x in input('Enter x1, y1 : ').split()]
#
cyrus_beck()

findParametricEquation()


