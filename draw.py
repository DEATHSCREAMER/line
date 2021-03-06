from display import *

#d0 is pixel to the up-right
#d1 if pixel to the right

# octants 1 and 5 : 0 < m < 1
# octants 2 and 6 : 1 < m < undefined
# octants 3 and 7 : undefined < m < -1
# octants 4 and 8 : -1 < m < 0

def draw_line( x0, y0, x1, y1, screen, color ):
    slope = None
    currentx = x0
    currenty = y0

    #mx - y + b = 0
    #deltay x - dealtax y + deltax b = 0
    #Ax + By + C = 0
    a = y1 - y0
    b = -1 * (x1 - x0)
    c = None

    if (b != 0):
        slope = (y1-y0) / (x1-x0)
        c = -1 * b * ((a / b) * (0 - x0) + y0)

    if (a == 0):
        while currentx <= x1:
            plot(screen,color,int(currentx),int(currenty))
            currentx += 1
    elif (b == 0):
        while currenty <= y1:
            plot(screen,color,int(currentx),int(currenty))
            currenty += 1

    #OCTANT 1 AND 5
    elif (0 <= slope and slope <= 1):
        #midpoint times 2
        d2 = 2 * a + b
        #loop to make line

        if (currentx <= x1):
            #d2 = 2 * a + b
            while currentx <= x1:
                plot(screen,color,currentx,currenty)
                d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + 2*c
                if abs(d0) < abs(d2):
                    currenty += 1
                    d2 += (2*b)
                currentx += 1
                d2 += (2*a)
        else:
            d2 = -2 * a - b + x0
            while currentx >= x1:
                plot(screen,color,currentx,currenty)
                d0 = 2*a*(currentx-1) + 2*b*(currenty-1) + 2*c
                if abs(d0) > abs(d2):
                    currenty -= 1
                    d2 -= (2*b)
                currentx -= 1
                d2 -= (2*a)

    #OCTANT 2 AND 6
    elif (1 <= slope):
        #midpoint times 2
        d2 = 2 * b + a
        #loop to make line
        while currenty <= y1:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty+1) + c
            if abs(d0) < abs(d2):
                currentx += 1
                d2 += (2*a)
            currenty += 1
            d2 += (2*b)

    #OCTANT 3 AND 7
    elif (slope <= -1):
        #midpoint times 2
        d2 = 2 * b - a
        #loop to make line
        while currenty >= y1:
            plot(screen,color,currentx,currenty)
            d0 = 2*a*(currentx+1) + 2*b*(currenty-1) + c
            if abs(d0) > abs(d2):
                currentx += 1
                d2 += (2*a)
            currenty -= 1
            d2 -= (2*b)

    #OCTANT 4 AND 8
    elif (-1 <= slope and slope <= 0):
        #midpoint times 2
        d2 = 2 * a - b
        #loop to make line

        if (currentx <= x1):
            #d2 = 2 * a + b
            while currentx <= x1:
                plot(screen,color,currentx,currenty)
                d0 = 2*a*(currentx+1) + 2*b*(currenty-1) + 2*c
                if abs(d0) > abs(d2):
                    currenty -= 1
                    d2 -= (2*b)
                currentx += 1
                d2 += (2*a)
        else:
            d2 = -2 * a - b + x0
            while currentx >= x1:
                plot(screen,color,currentx,currenty)
                d0 = 2*a*(currentx-1) + 2*b*(currenty+1) + 2*c
                if abs(d0) > abs(d2):
                    currenty += 1
                    d2 += (2*b)
                currentx -= 1
                d2 -= (2*a)
