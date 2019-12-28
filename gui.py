import sys,time,os,serial,struct,serial.tools.list_ports
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
# sg.change_look_and_feel('DefaultNoMoreNagging')
layout = [					# Here's for the GUI window
	[sg.Text('Desired yükseklik:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='desired')],
	[sg.Text('Kp:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='kp')],
	[sg.Text('Kd:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='kd')],
	[sg.Text('Ki:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='ki')],
	[sg.Text('Direct:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='direct')],
	[sg.Text('Summax:')],
	[sg.Slider(range=(1,500), default_value=10, size=(20,15), orientation='horizontal', font=('Helvetica', 12),key='summax')],
	[sg.Button('Save to csv'), sg.Checkbox('Enable PWM', default=True,key='pwm')],
	[sg.Text('Always quit using here ->	 '),sg.Quit()]]
window	= sg.Window('EE407 Term Project GUI', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)
pi = np.pi
ports = serial.tools.list_ports.comports()
try:
	default_port = [p[0] for p in ports if 'CH340' in p[1] or 'Arduino' in p[1]][0]
except:
	print('Arduino is not connected! ')
	sys.exit()
port = default_port
class GUI():
	def __init__(self,arduino):
		self.save_arr = np.zeros(4).reshape(1,4)						# Change this if you have different # of arrays
		self.number_of_csv_files = len(os.listdir('csv/'))
		self.errorArray = self.angleArray = self.motorArray = self.timeArray = np.empty(0)
		self.arduino = arduino
		self.arduino.reset_input_buffer()
		self.time_init = 0
		self.first = True
		# plt.ion()
		# self.fig, self.ax = plt.subplots()
		# self.line, = self.ax.plot([],[])
		# self.line, = ax.plot(np.append(goster,self.timeArray)[-100:],np.append(goster,self.motorArray[-100:]))
	def update(self):
		self.event, self.values = window.Read(timeout=0) #timeout=50)
		self.arduino_read(self.arduino)
		self.save_or_not()
		# goster = np.zeros(100)
		# self.line.set_ydata(np.append(goster,np.array(self.motorArray,dtype=float))[-100:])  # update the data
		# goster2 = np.append(goster,np.array(self.timeArray,dtype=float))[-100:]
		# self.ax.set_xlim(goster2[-1]-5,goster2[-1])  # update the data 
		# self.fig.canvas.draw()
		# self.fig.canvas.flush_events()
		self.data_prep()
	def data_prep(self):
		self.kp = int(self.values['kp'])
		self.kd = int(self.values['kd'])
		self.ki = int(self.values['ki'])
		self.desired = int(self.values['desired'])
		self.Direct =  int(self.values['direct'] )
		self.sumMAX =  int(self.values['summax'] )
		self.enable_pwm = 1 if self.values['pwm'] == True else 0
		print('event: ',self.event)
		if self.event in ('Quit', None):
			self.event = 'Save to csv'
			self.save_or_not()
			window.Close()
			arduino.close()
			sys.exit()
		try:
			self.arduino.write(struct.pack('>7B',self.kp,self.kd,self.ki,self.desired,self.Direct,self.sumMAX,self.enable_pwm))
			# https://docs.python.org/2/library/struct.html - bilgisayardaki doclarda da vardır aslında
		except:
			print(self.kp,self.kd,self.ki,self.desired,self.Direct,self.sumMAX,self.enable_pwm)
			print('arduino.write(struct.pack ÇALIŞMADI')
	def save_or_not(self):
		if self.event == 'Save to csv':
			self.save_arr = np.concatenate((self.timeArray.reshape(len(self.timeArray),1), self.errorArray.reshape(len(self.errorArray),1),
				self.angleArray.reshape(len(self.angleArray),1), self.motorArray.reshape(len(self.motorArray),1)), axis=1)
			self.save_arr = np.array(self.save_arr,dtype=float)	
			if os.path.isfile("csv/"+str(self.number_of_csv_files)+".csv") :
				self.number_of_csv_files = self.number_of_csv_files + 1
				np.savetxt("csv/"+str(self.number_of_csv_files)+".csv", self.save_arr, fmt='%5.4f',delimiter=",", header="Time,Error,MotorSpeed,MotorCommand")
			else:
				np.savetxt("csv/"+str(self.number_of_csv_files)+".csv", self.save_arr, fmt='%5.4f', delimiter=",", header="Time,Error,MotorSpeed,MotorCommand")
	def arduino_read(self,arduino):
		arduinoString = arduino.readline() 
		print('arduino: ',arduinoString.decode())
		A = arduinoString.decode().split(',') 
		while np.size(A) == 1:
			print("Please check if the serial monitor(Serial Port Ekranı) is open or not. If it is open, close it.")
			arduinoString = arduino.readline() 
			A = arduinoString.decode().split(',') 
		if self.first:
			self.first = False
			self.time_init = float(A[0])
		# print(A)
		self.timeArray	= np.append(self.timeArray, (float(A[0]) - self.time_init) )
		self.errorArray = np.append(self.errorArray, A[1])
		self.angleArray = np.append(self.angleArray, A[2])
		self.motorArray = np.append(self.motorArray, A[3])
if __name__ == '__main__':
	try:
		arduino = serial.Serial(port, 19200)
		if arduino.name not in [p[0] for p in ports if 'CH340' in p[1] or 'Arduino' in p[1]]:
			raise serial.SerialException
	except serial.SerialException:
		print('Cannot find the arduino board. Probably the usb port entered is wrong(--port).')
	else:
		gui = GUI(arduino)
		# ani = animation.FuncAnimation(fig, animate, np.append(, interval=25, blit=True)
		# plt.show(block=False)
		while True:
			gui.update()
		
		
		
		