import time
import subprocess
import os

bContinue = True

while bContinue:
	choice = input("""
1.Time Lapse
2.Stop process
3.Exit/Quit
Please enter choice: """)
	if choice == '1':
		print("choice 1")
		#subprocess.run(["python","blinkdot.py"])
		subprocess.call("python blinkdot.py", shell=True)
	elif choice == '2':
		print("choice 2")
	elif choice == '3':
		print("choice 3")
		bContinue = False
