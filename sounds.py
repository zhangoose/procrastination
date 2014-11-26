import curses
import thread
import time
import subprocess

piano = {'97': 'static/a.wav', '98': 'static/b.wav', '99': 'static/c.wav', '100': 'static/d.wav', '101': 'static/e.wav', '102': 'static/f.wav', '103': 'static/g.wav'}

screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()
q = -1
note = None

def play(key):
    subprocess.call(["afplay",key])

while q != ord('q'):
    screen.clear()
    screen.refresh()
    q = screen.getch()
    if q in range(97,104):
        note = piano[str(q)]
        try:
            thread.start_new_thread(play, (note,))
        except:
            print "nvm"


curses.endwin()
