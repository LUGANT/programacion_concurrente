import curses
from curses import wrapper, window

MINY,MAXY = 1,24
MINX,MAXX = 1,80
PASSES = 1000

def main(stdscr: window):
    stdscr.clear()
    stdscr.addstr("Hello World")

    stdscr.refresh()
    stdscr.getch()

wrapper(main)