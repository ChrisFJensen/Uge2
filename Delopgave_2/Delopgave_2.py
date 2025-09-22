import os as os
import re as re

if __name__ == "__main__":
    def Log_analysis(Log_fil: str, output_dir_name: str):
        with open(Log_fil,"r") as file:
            Log_data = file.readlines()
        #Bruger OS til at få path til nuværende mappe og output mappe
        Cur_dir = os.getcwd()
        Log_lists_path = os.path.join(Cur_dir,output_dir_name) #Mangler noget implementation ift manglende mappe
        for line in Log_data: # Kører et loop for hver log og sorterer dem i tilsvarende dokument
            #Hvert if statement er TRUE FALSE IFT log typen
            if re.search("INFO",line):
                list_path = os.path.join(Log_lists_path,"INFO_list.txt")
                with open(list_path, "a") as f:
                    f.write(f"{line}\n")
            elif re.search("ERROR",line):
                list_path = os.path.join(Log_lists_path,"ERROR_list.txt")
                with open(list_path, "a") as f:
                    f.write(f"{line}\n")
            elif re.search("WARNING",line):
                list_path = os.path.join(Log_lists_path,"WARNING_list.txt")
                with open(list_path, "a") as f:
                    f.write(f"{line}\n")
            elif re.search("SUCCESS",line):
                list_path = os.path.join(Log_lists_path,"SUCCESS_list.txt")
                with open(list_path, "a") as f:
                    f.write(f"{line}\n")
            else:
                #Implementeret other liste hvis jeg støder på nye log typer
                list_path = os.path.join(Log_lists_path,"OTHER_list.txt")
                with open(list_path, "a") as f:
                    f.write(f"{line}\n")
     
Log_analysis("Data/app_log (logfil analyse) - random.txt","Delopgave_2/Lister")