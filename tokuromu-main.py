try:
	from tkinter import *
	from playsound import *
	from threading import *
	from PIL import Image, ImageTk
	import socket
	import os
	from tkinter import Toplevel
	from time import sleep
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	def btsnd():
		playsound('assets/btsnd.wav')

	def writecache(filename, content):
		filepath = os.path.join(os.environ["HOME"], ".cache/tokuromu", filename)
		with open(filepath, "w") as cachefile:
			cachefile.write(content)

	def loginwindow():
		logwin = Toplevel()
		logwin.title("Tokuromu Online - Sign In")
		logwin.geometry("400x75")
		usertxtbox = Entry(logwin, width=50)
		usertxtbox.pack()
		pwdtxtbox = Entry(logwin, width=50)
		pwdtxtbox.pack()
		loginbutton = Button(logwin, text="Login", command=lambda: [writecache("logincache.txt", f"{usertxtbox.get()}\n{pwdtxtbox.get()}"), sleep(1), loginproc(), logwin.destroy()])
		loginbutton.pack()
		logwin.mainloop()
		# Keep the window open until the user logs in

	def loginproc():
		# Check if the login cache exists
		if os.path.exists(os.path.join(os.environ["HOME"], ".cache/tokuromu/logincache.txt")):
			# Get login data from cache
			with open(os.path.join(os.environ["HOME"], ".cache/tokuromu/logincache.txt"), "r") as logincache:
				# Split the lines of the file
				logindata = logincache.read().splitlines()
				# Get the username
				username = logindata[0]
				# Get the password
				password = logindata[1]
				# Create socket object
				loginobj = socket.Socket()
				
		else:
			# Create the cache
			os.makedirs(os.path.join(os.environ["HOME"], ".cache/tokuromu"), exist_ok=True)
			# Open the login window with delay so the login windows appears on top instead of the logging in window, which covers up the login window (common bug)
			sleep(0.5)
			loginwindow()

	root = Tk()

	root.title("Tokuromu Online - Signing You In...")
	root.geometry("400x580")

	pfpborder = Image.open("assets/pfpborder64.png")
	pfpborderimg = ImageTk.PhotoImage(pfpborder)
	image_label = Label(root, image=pfpborderimg)
	image_label.pack()
	image_label.configure(anchor='center')
	btsndstart = Thread(target=btsnd, daemon=True)
	btsndstart.start()
	loginprocstart = Thread(target=loginproc, daemon=True)
	loginprocstart.start()

	mainloop()	

# Error handler

except MemoryError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Tokuromu ran out of memory to preform any more operations.")
except OverflowError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nSomething happened to a variable that threw something out of whack.")
except IndexError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nSomething happened to a variable that threw something out of whack.")
except AttributeError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nSomething happened to a variable that threw something out of whack.")
except ConnectionError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nTokuromu couldn't connect to the servers correctly. Please try again.")
except TypeError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nSomething happened to a variable that threw something out of whack.")
except ValueError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nSomething happened to a variable that threw something out of whack.")
except ImportError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nTokuromu couldn't find a module that was important.\n\nPlease reinstall tokuromu.")
except PermissionError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nTokuromu didn't have the necessary permissions to preform an action. Try running this chunk of code in a terminal.\n\nLinux or MacOS: sudo tokuromu\n\nWindows: runas /user:Administrator tokuromu.exe\nOr:\nRight click tokuromu.exe and run it as an administrator.")
except IOError as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nTokuromu had a problem accessing a file that was important.\n\nFile trying to be accessed: {str(e).split(': ', 1)[1]}\n\n\nPlease reinstall Tokuromu.")
except Exception as e:
	from tkinter import messagebox
	messagebox.showerror(f"Oops! Something went wrong!", f"Something went wrong and Tokuromu needs to close. We're sorry!\n\nPlease contact Shamton with the following error info, with the OS and specs of your computer.\n--------------\nError info:\n{e}")
