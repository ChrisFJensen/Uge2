import os as os
import re as re

def Log_analysis(Log_fil: str, output_dir_name: str):
    with open(Log_fil,"r") as file:
        Log_data = file.readlines()
    #Uses OS to get current WD and set destination for lists
    Cur_dir = os.getcwd()
    Log_lists_path = os.path.join(Cur_dir,output_dir_name)
    #Kig på implementation af manglende directory
    #Creates empty lists to sort data into
    INFO_list = []
    ERROR_list = []
    WARNING_list = []
    SUCCESS_list = []
    OTHER_list = []
    #Run a loop to sort each line into correct file
    for line in Log_data:
    #Uses regex search to sort log type
        if re.search("INFO",line):
            INFO_list.append(line)
        elif re.search("ERROR",line):
            ERROR_list.append(line)
        elif re.search("WARNING",line):
            WARNING_list.append(line)
        elif re.search("SUCCESS",line):
            SUCCESS_list.append(line)
        else:
            OTHER_list.append(line)
    #Print each list of logs to their own file
    list_path = os.path.join(Log_lists_path,"INFO_list.txt")
    with open(list_path, "w") as f:
        for line in INFO_list:
            f.write(f"{line}\n")
    list_path = os.path.join(Log_lists_path,"ERROR_list.txt")
    with open(list_path, "w") as f:
        for line in ERROR_list:
            f.write(f"{line}\n")
    list_path = os.path.join(Log_lists_path,"WARNING_list.txt")
    with open(list_path, "w") as f:
        for line in WARNING_list:
            f.write(f"{line}\n")
    list_path = os.path.join(Log_lists_path,"SUCCESS_list.txt")
    with open(list_path, "w") as f:
        for line in SUCCESS_list:
            f.write(f"{line}\n")
    list_path = os.path.join(Log_lists_path,"OTHER_list.txt")
    with open(list_path, "w") as f:
        for line in OTHER_list:
            f.write(f"{line}\n")

if __name__ == "__main__":
    # Run the code
    Log_analysis("Data/app_log (logfil analyse) - random.txt","Delopgave_2")