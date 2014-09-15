import curses
import time 
from random import randint

screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()
x,y = 5,5
b_width, b_height = 20, 10
q = -1
character = 'o';
vertical = 1
horizontal = 1
is_eaten = True
nom_counter = 0

def random_coord(x_min, x_max, y_min, y_max):
	x_rand = randint(x_min, x_max)
	y_rand = randint(y_min, y_max)
	return x_rand, y_rand

while q != ord('q'):
	screen.clear()
	border1 = curses.newwin(b_height,b_width - len(character) ,5,5)
	border1.box()
	border1.addstr(0,0, str(nom_counter), curses.A_DIM)
	border1.addstr(y,x, character, curses.A_BOLD)

	if(is_eaten == True):
		xy_rand = random_coord(2, b_width - 3, 2, b_height - 2);
		x_rand = xy_rand[0]
		y_rand = xy_rand[1]
		is_eaten = False

	border1.addstr(y_rand, x_rand, 'x')
	screen.refresh()
	border1.refresh()

	q = screen.getch()
	if q == ord('k') and y > 1:
		y -= 1
	elif q == ord('j') and y < b_height - 2:
		y += 1
	elif q == ord('h') and x > 1:
		x -= 1
	elif q == ord('l') and x < b_width - 3 :
		x += 1
	
	if x == x_rand and y == y_rand:
		border1.addstr(y_rand, x_rand, '')
		nom_counter += 1
		is_eaten = True
		time.sleep(0.2)

	time.sleep(0.1)

curses.endwin()
