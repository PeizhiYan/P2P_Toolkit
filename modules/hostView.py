import tkinter as tk
import util



##########
## GUI ###
##########
class View:
	def startBtnHandler(self, event):
		print('start button clicked')

	def __init__(self):
		self.HEIGHT = 500
		self.WIDTH = 600
		self.X_OFFSET = 300
		self.Y_OFFSET = 300
		self.BG_COLOR = '#A37F6F'
		self.hostViewInstance = tk.Tk()
		self.info = tk.Text(self.hostViewInstance, height=15, width=60, background='black', foreground='green')
		self.ipText = tk.Text(self.hostViewInstance, height=1, width=20)
		self.portText = tk.Text(self.hostViewInstance, height=1, width=20)
		self.startBtn = tk.Button(self.hostViewInstance, text='Start', width=15, height=2)

		self.hostViewInstance.geometry(str(self.WIDTH)+'x'+str(self.HEIGHT)+'+'+str(self.X_OFFSET)+'+'+str(self.Y_OFFSET))
		self.hostViewInstance.configure(background=self.BG_COLOR)
		self.hostViewInstance.title('Host A Communication')

		# Network interface information
		tk.Label(self.hostViewInstance, text='\nYour Network Interface:\n', background=self.BG_COLOR, font=("Times New Roman", 9)).pack()
		self.info.pack()
		self.info.insert(tk.END, util.get_ip_info())
		util.print_msg(util.get_ip_info())

		# ip Text box
		tk.Label(self.hostViewInstance, text='\n\nIP:', background=self.BG_COLOR, font=("Times New Roman", 9)).pack(pady=0)
		self.ipText.pack(pady=0)

		# port Text box
		tk.Label(self.hostViewInstance, text='PORT:', background=self.BG_COLOR, font=("Times New Roman", 9)).pack(pady=0)
		self.portText.pack(pady=0)
		self.portText.insert(tk.END, '666') # by default using port number 666

		# Start button
		self.startBtn.pack(pady=30)
		self.startBtn.bind('<Button-1>', self.startBtnHandler)

		self.hostViewInstance.mainloop()



