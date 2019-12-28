import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import sys
layout = [					# Here's for the GUI window
	[sg.Text('Variable you wanna plot: ')],
	[sg.Listbox(values=['errorArray', 'angleArray', 'motorArray'],
	default_values=['motorArray'], size=(20, 4),key='variable')],
	# [sg.Button('Save to csv'), sg.Checkbox('Enable PWM', default=True,key='pwm')],
	[sg.Submit(), sg.Cancel()]]
window	= sg.Window('EE407 Term Project Plotting GUI', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)
while True:
	while True:
		event, values = window.Read()
		if event == 'Submit':
			# window.Close()
			break
		elif event == 'Cancel':
			window.Close()
			sys.exit()
	timeArray,errorArray,angleArray,motorArray = np.genfromtxt(sys.argv[1], delimiter=',').T
	plt.figure()
	plt.plot(timeArray,eval(values['variable'][0]))
	plt.title(values['variable'][0] + ' vs Timearray')
	plt.show(block=False)
	event = None