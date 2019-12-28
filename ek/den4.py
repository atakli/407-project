import PySimpleGUI as sg

layout = [
            [sg.Input(key='_IN_')],
            [sg.Slider(range=(1,100), key='_SLIDER_')],
            [sg.Button('Button')]
         ]

window = sg.Window('My new window', layout)

while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print(event, values)
    window.Elem('_SLIDER_').SetFocus()

# import PySimpleGUI as pSG

# val = 0
# layout = [
    # [pSG.Slider(range=(0, 1000), default_value=val, size=(50, 10), orientation="h",
                # enable_events=True, key="slider")],
    # [pSG.Spin(values=[i for i in range(1000)], initial_value=val, size=(8, 4),
              # enable_events=True, key="spin")]
# ]
# window = pSG.Window("slider test", layout)
# window.Finalize()

# while True:
    # event, values = window.Read()

    # if event is not None:
        # if event == "slider":
            # val = values["slider"]
            # window.Element("spin").Update(val)
        # elif event == "spin":
            # val = values["spin"]
            # window.Element("slider").Update(val)
			
