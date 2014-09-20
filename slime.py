import curses
import time 

screen = curses.initscr()
screen.nodelay(1)
curses.noecho()
dims = screen.getmaxyx()
x,y = 0,5
q = -1
sp_counter = 0 #goes from 0,1,2,0,1,2
add_vert, add_horiz = 1, 1


sprite0 = [" ##########", "  # >  < #", " ########"]
sprite1 = ["  ######"," # o  o #"," ########"]
sprite2 = ["  ######"," # >  < #","##########" ]

sprites = [ sprite0, sprite1, sprite2 ]
while q < 0:
	screen.clear()
	screen.addstr(y,x, sprites[sp_counter][0])
	screen.addstr(y+1,x, sprites[sp_counter][1])
	screen.addstr(y+2,x, sprites[sp_counter][2])
	screen.refresh()

	y += add_vert
	x += add_horiz

	if y == dims[0] - 3 or y == dims[0] - 2 or y == dims[0] -1 or y == dims[0]:
		# hit the bottom
		add_vert = -1
		sp_counter = 2
	elif y > 0 and y <= 3:
		# hit the top
		add_vert = 1
		sp_counter = 0
	if x == dims[1] - 10:
		# hit the right 
		add_horiz = -1
		sp_counter = 1
	elif x == 0:
		# hit the left
		add_horiz = 1
		sp_counter = 1

	q = screen.getch()
	time.sleep(0.1)

curses.endwin()
