from pynput.keyboard import Key, Listener, Controller, KeyCode
# remove characters in your copy board
# press left alt(default) to execute
# press right alt(default) to exit
import time
import random
import threading
import pyperclip
import sys
char_to_remove = ["\n", "\r"]
operate_key = Key.ctrl_r
exit_key = Key.alt_r
def on_press_key(key):
	x = 0
def on_release_key(key):
	global char_to_remove
	if key == exit_key:
		# Stop listener
		print("Exit")
		sys.stdout.flush()
		return False
	elif key == operate_key:
		copy_content = pyperclip.paste()
		msg = copy_content + " -> "
		for i in range(0, len(char_to_remove)):
			copy_content = copy_content.replace(char_to_remove[i], " ")
		copy_content = copy_content.replace("  ", " ")
		msg = msg + copy_content
		pyperclip.copy(copy_content)
		print(msg)
		sys.stdout.flush()
		# do
# Collect events until released
with Listener(
		on_press=on_press_key,
		on_release=on_release_key) as listener:
	listener.join()
