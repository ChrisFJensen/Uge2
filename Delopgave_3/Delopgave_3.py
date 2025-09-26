import os
import re

def read_file(file_name: str, seperator=","):
    #Read the given file
    try:
        with open(file_name,"r") as file:
            data_string = file.readlines()
            #Checks if different different number of variables is given
            Var_numbers= len(data_string[0].split(seperator))
            data = list(map(lambda x: x.strip("\n").split(seperator), data_string))
            return data
    #Adds specific text for file not existing
    except FileNotFoundError:
        print("File does not exist")
        #Add option to attempt a different name
        New_name = input("Please type an existing file read or type q to quit:" )
        return(New_name)
    # Other potential errors
    except:
        print("We encountered an error while attempting to read file")
        return("NEWERROROCCURREDCFJ")

def clean_data(data: list):
    # Creates an empty list of useable and running total of removed lines
    Good_data = []
    Unknow_error_data = []
    Missing_data = []
    Var_Numbers = len(data[0])
    removed_lines = 0
    #Uses rowline to fix customer_id
    row_line = 1
    for line in data[1:]:
        line[0] = str(row_line)
        row_line += 1
        #Checks if too many columns
        while len(line) > Var_Numbers:
            try:
                HV = float(line[1])
                line.pop(1)
            except:
            #Removes whitespace
                if "" in line:
                    line.remove("")
            #Print rownumbers of problematic entries in data that i didn't catch
                else:
                    Unknow_error_data.append(line)
                    break
        if len(line)==Var_Numbers:
            # Checks if data is missing
            if "" in line:
                removed_lines += 1
            # Checks if nan is a data point
            elif "nan" in line:
                removed_lines += 1
            #Check if emails contains @
            elif re.search("@",line[2])==None:
                removed_lines += 1
            # appends if no fault is found
            else:
                try:
                    HV = float(line[3])
                    Good_data.append(line)
                except:
                    removed_lines +=1
        elif len(line)<Var_Numbers:
            Missing_data.append(line)
            removed_lines += 1
        else:
            removed_lines += 1
    #Printer antallet af linjer der er blevet fjernet
    print(f"removed:" + str(removed_lines) +" lines."  )
    #In case every line is removed due to clean_data being custom for source_data.csv
    if (removed_lines-len(data)+1)==0:
        print("All lines have been removed. Data is likely uncompatible with function")
    #Returns a list with non-empty data with correct amount of variables per row
    return(Good_data)

#Function that writes to a csv formatted file
def write_to_file(data: list, Destination_name: str):
    #Gets current directory and wanted destination
    cur_dir = os.getcwd()
    Dest_path = os.path.join(cur_dir,Destination_name+".csv")
    #Checks if file already exists, and how to handle it
    #Missing directory error
    while os.path.isfile(Dest_path):
        print("File already exists.")
        print("To replace type r or replace.")
        New_dest = input("Please type a new file name(.csv is automatically added):")
        #Checks if user want to replace
        if New_dest in ["r","replace"]:
            break
        else:
            Dest_path = os.path.join(cur_dir,New_dest+".csv")
    New_dest_path = Dest_path
    try:
         with open(New_dest_path, "w") as file:
            for line in data:
                #Formats it so it corresponds to a .csv format
                file.write(f",".join(line)+"\n")
    #If received permission ask for different output
    except PermissionError:
            print("Don't have required permission to write file")
            New_dest = input("Please input a new destination: ")
            return New_dest
    # If received a path that contains a nonexistent folder, ask for different output
    except FileNotFoundError:
            print("Invalid directory given")
            New_dest = input("Please input a new destination: ")
            return New_dest


#Function that combines all other functions
def All_together(file_name: str, Destination_name: str, seperator=","):
    Data_loaded = read_file(file_name,seperator)
    #Handles if a nonexisting file is received
    while type(Data_loaded)==str:
        match Data_loaded:
            case "q":
                print("Recieved invalid file to read, quitting program")
                return
            case "NEWERROROCCURREDCFJ":
                print("Ran into a unkown error when reading file. Quitting program")
                return
            case _:
                New_file_name = Data_loaded
                Data_loaded = read_file(New_file_name,seperator)
    #Runs the data cleaning function
    Data_cleaned = clean_data(Data_loaded)
    #Option to handle new errors that i am not familiar with, or how to test for.
    output_file = write_to_file(Data_cleaned,Destination_name)
    # if write_to_filed failed to write
    # Allows user to change output path
    while type(output_file)==str:
        match output_file:
            case "q":
                print("Couldn't write file, exiting program")
                return
            case _:
                New_dest = output_file
                output_file = write_to_file(Data_cleaned,New_dest)

if __name__ == "__main__":
    All_together("Data/source_data.csv","Delopgave_3/Clean_data")
