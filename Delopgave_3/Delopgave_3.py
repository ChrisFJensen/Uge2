import os

def read_file(file_name: str, seperator=",", Var_numbers=0):
    #Read the given file
    try:
        with open(file_name,"r") as file:
            data_string = file.readlines()
            #Checks if different different number of variables is given
            if Var_numbers == 0:
                Var_numbers= len(data_string[0].split(","))
            data = list(map(lambda x: x.strip("\n").split(seperator), data_string))
            row_line = 0
            for line in data:
                line[0] = str(row_line)
                row_line += 1
            print(Var_numbers)
            return data
    #Adds specific text for file not existing
    except FileNotFoundError:
        print("File does not exist")
        #Add option to attempt a different name
    # Other potential errors
    except:
        print("We encountered an error")

test = read_file("Data/source_data.csv")

def clean_data(data: list):
    # Creates an empty list of useable and running total of removed lines
    Good_data = []
    Var_Numbers = len(data[0])
    removed_lines = 0
    for line in data:
        #Checks if to many columns
        while len(line) > Var_Numbers:
            #Removes whitespace
            if "" in line:
                line.remove("")
            #Checks if 2. column is either a number or Nan
            elif float(line[1]):
                line.pop(1)
            #Print rownumbers of problematic entries in data that i didn't catch
            else:
                print(line[0])
                removed_lines += 1
                break
        if len(line)==Var_Numbers:
            # Checks if data is missing
            if "" in line:
                removed_lines += 1
            # Checks if nan is a data point
            elif "nan" in line:
                removed_lines += 1
            # appends if no fault is found
            else:
                Good_data.append(line)
        else:
            print("missing data")
            removed_lines += 1
    #Printer antallet af linjer der er blevet fjernet
    print(f"removed:" + str(removed_lines) +" lines."  )
    #Returns a list with non-empty data with correct amount of variables per row
    return(Good_data)

test2 = clean_data(test)


#Function that writes to a csv formatted file
def write_to_file(data: list, Destination_name: str):
    #Gets current directory and wanted destination
    cur_dir = os.getcwd()
    Dest_path = os.path.join(cur_dir,Destination_name+".csv")
    #Checks if file already exists, and how to handle it
    if os.path.isfile(Dest_path):
        print("File already exists.")
        print("To replace type r or replace.")
        New_dest = input("Please type a new file name(.csv is automatically added):")
        #Checks if user want to replace
        if New_dest in ["r","replace"]:
            New_dest_path = Dest_path
        else:
            New_dest_path = os.path.join(cur_dir,New_dest+".csv")
        #Opens and writes to new file
        try:
            with open(New_dest_path, "w") as file:
                for line in data:
                    #Formats it so it corresponds to a .csv format
                    file.write(f",".join(line)+"\n")
        # Added for future error handling
        except:
            print("An error occured")
    else:
        #Opens and writes to new file
        try:
            with open(Dest_path, "w") as file:
                for line in data:
                    file.write(f",".join(line)+"\n")
        # Added options for future error handling
        except:
            print("An error occurred")


#Function that combines all other functions
def All_together(file_name: str, Destination_name: str, Var_numbers=0, seperator=","):
    Data_loaded = read_file(file_name,seperator, Var_numbers)
    Data_cleaned = clean_data(Data_loaded)
    write_to_file(Data_cleaned,Destination_name)

if __name__ == "__main__":
    All_together("Data/source_data.csv","We_gamed")