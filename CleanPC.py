
import PySimpleGUI as sg
import os
import shutil

sg.theme('BluePurple')
layout = [[sg.Text('Press Start to clean useless files of C Drive: ',size=(40, 1), font=("Arial, 17"))],
          [sg.Button('Clean',font=("Arial, 15")),sg.Button('Quit',font=("Arial, 14"))],
          [sg.Text('',size=(30, 1), key='-OUT-', font=("Arial, 25"))]]

window = sg.Window('CleanPC by Samir Gwalia',layout, margins=(40,10))

while True:
    event, values = window.read()
    print(event, values)
    if event == "Clean":

        def cleaner(folder):
            for the_file in os.listdir(folder):  # list file inside folder
                file_path = os.path.join(folder, the_file)
                indexNo = file_path.find('\\')
                itemName = file_path[indexNo + 1:]

                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print('%s file deleted' % itemName)

                    elif os.path.isdir(file_path):
                        if file_path.__contains__('chocolatey'):  continue
                        shutil.rmtree(file_path)
                        print('%s folder deleted' % itemName)

                except Exception as e:
                    print('Access Denied: %s' % itemName)

        temp = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
        cleaner(temp)
        temp2 = 'C:/Windows/Temp'
        cleaner(temp2)
        temp3 = 'C:/Windows/Prefetch'
        cleaner(temp3)
        window["-OUT-"].update("Folders Cleaned!!")

    if event == "Quit" or event == sg.WIN_CLOSED:
        break
window.close()


