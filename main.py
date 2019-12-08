#!/usr/bin/env python3
import curses
import csv
import sys

def getColumnWidths(data):
    maxs = [0] * len(data[0])
    for i in range (0,len(data)):
        for j in range(0,len(data[i])):
            if (maxs[j] < len(data[i][j])):
                maxs[j] = len(data[i][j])
    return maxs


def clamp(x , mn , mx):
    if (x < mn ): return mn
    elif (x > mx): return mx
    return x

def main(cScreen):
    xshift = 0
    yshift = 0
    curses.start_color()
    curses.use_default_colors()
    ScreenDimensions = cScreen.getmaxyx()
    maxx = ScreenDimensions[1]
    maxy = ScreenDimensions[0]
    with open (sys.argv[1],"r") as f:
        data = list(csv.reader(f))
        while True:
            cScreen.clear()
            for i in range(0,len(data)) :
                if i >= maxy :
                    continue
                for j in range(xshift,len(data[i])):
                    if sum(getColumnWidths(data)[xshift:j+1])+j+1 > maxx:
                        continue
                    cScreen.addstr(i,sum(getColumnWidths(data)[xshift:j])+j,data[i+yshift][j])
            cScreen.refresh()
            ch = cScreen.getkey()
            if ch == 'q':
                break
            if ch == 'l':
                xshift +=1
            if ch == 'h':
                xshift -=1
            if ch == 'j':
                yshift -=1
            if ch == 'k':
                yshift +=1
            xshift = clamp(xshift,0,len(data[0]))
            yshift = clamp(yshift,0,len(data)-1)
    pass

curses.wrapper(main)
