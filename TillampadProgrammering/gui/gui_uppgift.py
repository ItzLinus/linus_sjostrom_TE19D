import PySimpleGUI as sg

def start_gui():                                                                # Deklarerar vi funktionen
    sg.ChangeLookAndFeel('Black')                                               # Tema sätts
    sg.SetOptions(text_justification='right')                                   # Texten placeras till höger
    layout = [[sg.Text('Tillämpad programmering', font=('Helvetica', 35))],     # layout, Vi jobbar med listor. Efter detta sätter vi font size.
             [sg.Input(key='-IN-')],                                            # 
             [sg.Button('Counter:')]]

    window = sg.Window('Tillämpad programmering', layout, font=("Helvetica", 22))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Counter:':
            print('This button has now been pressed: ')
    
    event, values = window.read()

start_gui()

