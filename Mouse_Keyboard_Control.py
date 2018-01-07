#!/usr/bin/env python2
#import curses for tui, libxdo to send keys/mouse input
import curses
from xdo import Xdo


#initialize curses and xdo
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)

xdo = Xdo()


#Display screen
def main():
	while True:
		try:
			#Display screen & get input
			displayScreen(" ", "[arrow keys: mouse][i: input][r: right click][l: left click][q: quit]")
			kInput = screen.getch()

			#Interpret input
			if kInput == ord('r'): #right click
				xdo.click_window(0, 3)
			elif kInput == ord('l'): #left click
				xdo.click_window(0, 1)
			elif kInput == 261: #Move Right
				xdo.move_mouse_relative(5, 0)
			elif kInput == 260: #Move Left
				xdo.move_mouse_relative(-5, 0)
			elif kInput == 258: #Move Up
				xdo.move_mouse_relative(0, 5)
			elif kInput == 259: #Move Down
				xdo.move_mouse_relative(0, -5)
			elif kInput == ord('i'): #Get input
				userInput = getInput()
				xdo.enter_text_window(0, userInput.encode())
			elif kInput == ord('q'): #Exit
				exitApplication()
		except KeyboardInterrupt:
			exitApplication()


def getInput():
	currentText = ""
	while True:
		displayScreen(currentText, "[ENTER: send text][ESC: return to previous]")
		c = screen.getch()
		if c == 10: #enter
			return currentText
			break
		elif c == 27: #escape
			return ""
			break
		elif c == curses.KEY_BACKSPACE: #backspace
			currentText = currentText[:len(currentText) - 1]
		else:
			currentText += chr(c)


#Display Screen with instructions
def displayScreen(centerScreen, instructions):
	screen.clear()
	screen.border(0)
	screen.addstr(12, 30, centerScreen)
	screen.addstr(22, 1, instructions)
	screen.refresh()


#Clean Up Curses and exit
def exitApplication():
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
	exit()


#Call Main
main()
