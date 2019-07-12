# brownian_motion
A Python script with GUI using Tkinter tracking particles from microscope video file.

## Description
This project was created in a week for a school project aimed at studying different scientific phenonomenons. The script tracks particles on a given video file from a microscope. It allows to study the behavior of particles and thus to determine if their motion can be qualified as brownian. The GUI return an image file featuring the path of each of the particles
selectioned in the video as well as different graphs. The user has the possibility of creating his own functions in the GUI in 
the menu "Custom function". Many menus and options are available to change the presentation of the tracking. 

## Setup
Dowload or clone the repository. Run the following bash command to install all the packages needed. Those packages are listed in the requirements.txt file.

```pip3 install -r requirements.txt```

## Features

* User friendly GUI
* Multi object tracking
* Customable tracking info
  * Distance as radius
  * Current distance label
  * Max distance label
  * Path
  * Frame number
  * Drift warning 
 * Multiple data analysis function built-in
 * Write your own data analysis function 
 * Save each graphs separatly 
 * Save an image file of the particles path
 
 ## Usage
 
 Open a microscope video file: File > Open and select a file using the filebrowser.
 <img width="1439" alt="Screenshot 2019-07-12 at 22 07 21" src="https://user-images.githubusercontent.com/51379148/61155623-a7c09300-a4f1-11e9-8715-9220aa99d2e0.png">
 
 Select the tracking options you want in the Settings menu. Those options will appear on the screen during tracking and on the final image file. By default, all the options are selected. Feel free to unselect some of them if you find the screen overloaded. The selected options appear in blue in the up right hand corner of the screen.
 <img width="1440" alt="Screenshot 2019-07-12 at 22 14 06" src="https://user-images.githubusercontent.com/51379148/61156096-f1f64400-a4f2-11e9-8f80-9f1715e3c4c2.png">
 The treshold for the drift warning as well as the frame rate can be changed in this menu.
 
 To start the acquisition, click the Start button on the right of the screen. An info message will appear explaining how to select particles. To select a particle, drawn a rectangle over it with your mouse. Make sure the entierty of the particle fits instide the rectangle, then press the ENTER key. To select another particle, press any key and repeat the same process. When the selection is done, press the Q key to quit the acquisition mode.
 The tracking will then begin
 <img width="1438" alt="Screenshot 2019-07-12 at 22 27 20" src="https://user-images.githubusercontent.com/51379148/61156705-54037900-a4f4-11e9-8e04-816d6a3465d0.png">

To save the image file, go to File > Save as and select a directory.

Close the tracking window and go to the Data menu. Select the dataset you want to work with. Each dataset correspond to one of the particles tracked and follow the same order as when the were selected. Then select a function. Many buit-in functions are available. You can check what the exacly does in the ```plotter.py``` file.
You can create different graphs at the same time with different dataset or function for comparaisons purposes.

<img width="1439" alt="Screenshot 2019-07-12 at 22 41 24" src="https://user-images.githubusercontent.com/51379148/61157396-536be200-a4f6-11e9-8f21-eb4e264f2496.png">
Save each graph individualy by clicking the save button underneath it.

Finally, you can create your own function by going to Data > Edit custom functions
This will open a text editor in which you can add or modify function. Those function will be available in the Data menu.
You can also directly edit the file ```Custom_functions.py```.

