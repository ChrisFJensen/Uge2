import numpy as np
import pandas as pd
import matplotlib as mlb
import matplotlib.pyplot as plt


#Indlæser Dataframen
Hus_data_df = pd.read_csv("Data/DKHousingPricesSample100k.csv")
Hus_data_df.head(10) #Printer 10 første linjer

Region_data = Hus_data_df.groupby("region") #Grupperer efter region
Reg_avg_purchase = Region_data["purchase_price"].mean() # Tager den gennemsnitlige værdi for hver region

House_type_df = Hus_data_df.groupby("house_type")["purchase_price"]

Hus_data_df.groupby("house_type")["purchase_price"].plot(legend=True)
