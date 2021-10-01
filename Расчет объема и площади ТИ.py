import PySimpleGUI as sg

# GUI
sg.theme('Dark Green')

layout = [[sg.Text('Расчет теплоизоляции', font='Courier 12', text_color='yellow', size=(80, 1),
                   justification='center', relief=sg.RELIEF_RIDGE, border_width=10)],
          [sg.Text()],
          [sg.Image(filename='Tube.png', size=(1000, 320))],
          [sg.Text()],
          [sg.Text("   Диаметр трубы: D,мм"), sg.Input(k='-DIAM-')],
          [sg.Text()],
          [sg.Text("Толщина изоляции: H,мм"), sg.Input(k='-THICK-')],
          [sg.Text()],
          [sg.Text("      Длина трубы: L,м"), sg.Input(k='-LENGTH-')],
          [sg.Text()],
          [sg.Text("Объем\nтеплоизоляции: V,м3"), sg.Text('_____________', k='-VOL-', background_color='grey')],
          [sg.Text("Площадь покрытия\nтеплоизоляции: S,м2"), sg.Text('_____________', k='-SQR-',
                                                                     background_color='grey')],
          [sg.Text()],
          [sg.Button("Расчет", tooltip='Нажми меня!'), sg.Button("Очистить"), sg.Button("Выход")]]

#  Screen with Title
#  window = sg.Window('Теплоизоляция трубопровода', layout, location=(0, 0), size=(1000, 2060), font='Courier 8')

#  Full Screen
window = sg.Window('Теплоизоляция трубопровода', layout, font='Courier 9', finalize=True,
                   element_justification='center')
window.Maximize()

#  event, values = window.read()
#  window.close()

# CODE
while True:
    event, values = window.read()

    if event in (None, sg.WIN_CLOSED, "Выход"):
        break
    elif event == "Расчет":
        try:
            diam = float(values['-DIAM-'])
            thick = float(values['-THICK-'])
            length = float(values['-LENGTH-'])
            vol = 3.14 / 1000 * (diam + thick) * thick / 1000 * length
            sqr = 3.14 / 1000 * (diam + 2 * thick) * length
            window['-VOL-'].update(str(round(vol, 4)), background_color='light green')
            window['-SQR-'].update(str(round(sqr, 2)), background_color='gold')
        except ValueError:
            window['-VOL-'].update('Ошибка ввода!', background_color='red')
            window['-SQR-'].update('Ошибка ввода!', background_color='red')
    elif event == "Очистить":
        window['-DIAM-'].update('')
        window['-THICK-'].update('')
        window['-LENGTH-'].update('')
        window['-VOL-'].update('_____________', background_color='grey')
        window['-SQR-'].update('_____________', background_color='grey')

window.close()
