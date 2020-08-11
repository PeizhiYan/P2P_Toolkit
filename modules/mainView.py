import tkinter as tk
import hostView

def exitBtnHandler(event):
	print('exit button clicked')
	exit(0)

def hostBtnHandler(event):
	print('host button clicked')
	hv = hostView.View()

def joinBtnHandler(event):
	print('join button clicked')
	pass


##########
## GUI ###
##########

def start():
	HEIGHT = 400; WIDTH = 300; X_OFFSET = 300; Y_OFFSET = 300
	BG_COLOR = '#A37F6F'
	mainViewInstance = tk.Tk()
	mainViewInstance.geometry(str(WIDTH)+'x'+str(HEIGHT)+'+'+str(X_OFFSET)+'+'+str(Y_OFFSET))
	mainViewInstance.configure(background=BG_COLOR)
	mainViewInstance.title('P2P Toolkit')

	# Title label
	tk.Label(mainViewInstance, text='\nP2P Communication Toolkit\n', background=BG_COLOR, font=("Times New Roman", 12, "bold")).pack()

	# Host button
	hostBtn = tk.Button(mainViewInstance, text='Host (be the server)', width=15, height=2)
	hostBtn.pack(pady=10)
	hostBtn.bind('<Button-1>', hostBtnHandler)

	# Join button
	joinBtn = tk.Button(mainViewInstance, text='Join (be the client)', width=15, height=2)
	joinBtn.pack(pady=10)
	joinBtn.bind('<Button-1>', joinBtnHandler)

	# exit button
	exitBtn = tk.Button(mainViewInstance, text='Exit', width=15, height=2)
	exitBtn.pack(pady=60)
	exitBtn.bind('<Button-1>', exitBtnHandler)

	# Author label
	tk.Label(mainViewInstance, text='\nAuthor: Matthew Peizhi Yan\nhttps://PeizhiYan.github.io', background=BG_COLOR, font=("Times New Roman", 8)).pack()


	mainViewInstance.mainloop()

