import PySimpleGUI as sg  
import os.path


file_list_colum = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
        )
    ],
]

#this^ creates a verticle column in the user interface which will make a browse button to search for images.

image_viewer_colum = [#will only show name of file for now
        [sg.Text("Choose an image from list on left:")],#tells user to pick
        [sg.Text(size=(40, 1), key="-TOUT-")],#displays name of file
        [sg.Image(key="-IMAGE-")],#displays image chosen
]

layout = [#controls layout of items on screen
    [
        sg.Column(file_list_colum),
        sg.VSeperator(),
        sg.Column(image_viewer_colum),
    ]
]

window = sg.Window("Image Viewer", layout) #adds my layout ^^ to the window

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":#list of files in folder, if user clicks folder, FOLDER event is activated 
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-": #a file was chosen from listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()  
