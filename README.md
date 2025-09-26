# Specialisterne Academy Uge 2

My solutions to the week 2 assignments.

## Description
My solutions to the assignments given for week 2 of the academy. The solution to each assignment can be found under the folder with the corresponding name.
Would appreciate feedback on how to write readmes and documentation since I haven't really worked on that before

### Delopgave 1
Implemented functions to handle the loading of a .txt file and counting each appearence for every letter as well as a count of how long each word is in the text.
Furthermore i added a function that allows me to get the average word length of the text as well as the median word length.
When the program is run it will also perform a basic analysis of the letters and word length distribution for the navneliste.txt file.

Did not struggle too much with this assignment and I found it fairly simple, except for removing duplicates since there were none in the file.
### Delopgave 2
Implemented a function that allows the user to declare a log_file to analyse and then split the logfile into relevant files sorted by type.
Struggled mostly on how i should store each line wrt their error and then getting the code to print all lines to the correct file.
### Delopgave 3
Implemented a function that reads .csv files and outputs them to a user specified file. As part of the function i defined a function that only works for the "source_data.csv" which performs some data cleaning.

Enjoyed and struggled with working to catch and handle errors since it is not something that i am used to from before. But struggled a bit with what the actual goal of our script needed to do when looking into how i should handle different errors.

### Delopgave 4
I have implemented a script that loads the given data into a pandas dataframe and then plots some plots that i found relevant.

I have worked a lot with dataframes and plotting dataframes before and I already have some experience with pandas so i didn't spend too much time on this assignment.

## Getting Started

### Dependencies

* All the prequisite modules can be found and installed from the requirements.txt
* Python version that supports match function

### Installing

* The folder can be downloaded from my github
* Install modules from requirements.txt

### Executing program

#### Delopgave 1
Functions for reading data and performing the counting operations can be imported but to see the analysis and plot the script has to be run.
Most functions requires a list as an input, and a list of the correct form be achieved by running the open_data function
```
open_data(file_name:str)
```
When running the script some plots will pop up that have to be closed before the rest of the code executes.

#### Delopgave 2
The scripts contains a single function "log_analysis" which takes what file to read and output directory as arguments.
```
log_analysis(Log_file: str, output_dir_name: str)
```
The script will output 5 new documents to the directory specified as the argument.

#### Delopgave 3
The script contains 4 functions. A function that reads the file, a data cleaning function designed for the "source_data.csv" file, a function that writes and then a function that combines them all into one. The last function takes input file and output file as arguments as well as an optional seperator argument.
```
All_together(file_name: str, Destination_name: str, seperator=",")
```
Note that if the function might ask for user input if it is unable to read the input file, the output file already exists or you are trying to write to a directory that does not exist.
You do not need to specify ".csv" int the output name since the script automatically adds it and it ensures that the written file is a csv document.

#### Delopgave 4
The script contains no functions and won't do anything unless run directly. It will output some plots that will need to be closed to see the rest of the execution.

## Authors

Contributors names and contact info

Christopher F. Jensen
