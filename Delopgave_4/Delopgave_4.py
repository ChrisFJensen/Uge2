import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #Reads the dataframe
    House_data_df = pd.read_csv("Data/DKHousingPricesSample100k.csv")
    House_data_df.head(10) #Prints first 10 lines

    Region_data = House_data_df.groupby("region") #Group by region
    Reg_avg_purchase = Region_data["purchase_price"].mean() # Gets avg purchase prise for each region


    House_type_df = House_data_df.groupby("house_type") #Groupsdata by housetype

    House_data_df.groupby("house_type")["purchase_price"].plot(legend=True)
    House_type_df.head(10)

    Reg_avg_purchase.plot(kind="bar")
    plt.title("Avg Price by Region")
    plt.xlabel("Regions")
    plt.xticks(rotation = 0)
    plt.show()


    #Creates DF to calcute the avg purchase price in each region
    House_region_df = House_data_df.groupby(["region","house_type"])
    House_region_avg = House_region_df["purchase_price"].mean().reset_index()#Uses reset.index() to keep it as a DF rather than a series

    #Uses pandas pivot to get a DF with only data we are interested in
    pivot_house_region_avg = House_region_avg.pivot(index="region", columns="house_type", values="purchase_price")

    # Define positions
    x = np.arange(len(pivot_house_region_avg.index))
    width = 0.1 #Sets bar width


    fig, ax = plt.subplots()

    for i, house_type in enumerate(pivot_house_region_avg.columns):
        ax.bar(
            x + i * width,
            pivot_house_region_avg[house_type],
            width,
            label=house_type
        )

    # Formatting
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(pivot_house_region_avg.index)
    ax.set_ylabel("Avg puchase price")
    ax.set_title("Avg purchase price for each house type in each region")
    ax.legend(title="House_type")
    plt.show()

    #Creates a dataframe for only Zealand and removes Farm and Sommerhouse data
    Zealand_data = House_data_df[House_data_df["region"]=="Zealand"]
    Zealand_data = Zealand_data[Zealand_data["house_type"]!="Farm"]
    Zealand_data = Zealand_data[Zealand_data["house_type"]!="Summerhouse"]

    # Gets the avg purchase price for the whole region and for each area in the region
    Zealand_avg_data = Zealand_data.groupby("house_type")["purchase_price"].mean()
    Zealand_avg_by_area = Zealand_data.groupby(["house_type","area"])["purchase_price"].mean().reset_index()

    Zealand_avg_data.items()

    Pivot_ZABA = Zealand_avg_by_area.pivot(index="area",columns="house_type",values="purchase_price")

    palette = plt.get_cmap("tab10")
    housetypes = Pivot_ZABA.columns
    color_map = {sg: palette(i) for i,sg in enumerate(housetypes)}


    x = np.arange(len(Pivot_ZABA.index))
    width = 0.1 
    fig, ax = plt.subplots()

    for i, house_type in enumerate(housetypes):
        ax.bar(
            x + i * width,
            Pivot_ZABA[house_type],
            width,
            label=house_type,
            color=color_map[house_type]
        )

    # Formatting
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(Pivot_ZABA.index)
    ax.set_ylabel("Avg puchase price")
    ax.set_title("Avg purchase price for each house type in each region")
    ax.legend(title="House_type")
    for label, y in Zealand_avg_data.items():
        ax.axhline(y=y, color=color_map[label], linestyle="--", linewidth = 1, label="f{label} mean")
    plt.show()