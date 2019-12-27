import PySimpleGUI as sg

window = sg.Window('Testing the Debugger', [[sg.Text('Debugger Tester'), sg.In('Input here'), sg.B('Push Me')]])

while True:
    event, values = window.Read(timeout=500)
    if event == sg.TIMEOUT_KEY:
        continue
    if event is None:
        break
    print(event, values)
window.Close()