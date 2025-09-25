import numpy as np
import pandas as pd
import matplotlib as mlb
import matplotlib.pyplot as plt


#Indlæser Dataframen
Hus_data_df = pd.read_csv("Data/DKHousingPricesSample100k.csv")
Hus_data_df.head(10) #Printer 10 første linjer

Region_data = Hus_data_df.groupby("region") #Grupperer efter region
Reg_avg_purchase = Region_data["purchase_price"].mean() # Tager den gennemsnitlige værdi for hver region

House_type_df = Hus_data_df.groupby("house_type") # Laver igen en groupby

Hus_data_df.groupby("house_type")["purchase_price"].plot(legend=True)
# Er igang med at bruge matplotlib igen.
House_type_df.head(10)

Reg_avg_purchase.plot(kind="bar")
plt.title("Avg Price by Region")
plt.xlabel("region")
plt.xticks(rotation = 45)
plt.show()


#Tilføj plot som viser den gennemsnitlige pris af hver type villa i hver region