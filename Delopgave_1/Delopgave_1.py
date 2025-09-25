import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import wordcloud as wc


if __name__ == "__main__":
    #read data
    Navne = open("Data/Navneliste.txt", "r").readlines()

    #Convert data to a list where each name is it's own element
    Navne_split = Navne[0].split(",")

    #Removes whitespace from around each name
    Navne_split = [navn.strip() for navn in Navne_split]
    print(Navne_split)

    #Sorts names alphebetically
    Navne_sorteret = sorted(Navne_split)
    print(Navne_sorteret)

    #Sorts names by length
    Navne_sorteret_længde = sorted(Navne_split, key=len)
    print(Navne_sorteret_længde)


    #Empty dict to store the count for each letter
    bogstav_tæller = {}
    #Loop for each name in data
    for navn in Navne_sorteret:
        #Loop for each letter in name
        for bogstav in navn.lower():
            #if statements to add or create count for letter
            if bogstav in bogstav_tæller:
                bogstav_tæller[bogstav] += 1 
            else:
                bogstav_tæller[bogstav] = 1


    #Function to sort dict keys alphabetically (for plot purpose)
    def sort_dict(Dict: dict):
        Dict_keys = list(Dict.keys())
        Dict_keys.sort()
        Dict_sorted = {i: Dict[i] for i in Dict_keys}
        return(Dict_sorted)

    bogstav_tæller_sorted = sort_dict(bogstav_tæller)
    bogstav_tæller_sorted

    # skal have lavet et pænere plot.
    plt.bar(bogstav_tæller_sorted.keys(), bogstav_tæller_sorted.values(), width = 1, edgecolor="white", linewidth=0.7)
    plt.xlabel("Bogstaver") #Sætter label på x-aksen
    plt.ylabel("Forekomster") #Sætter label på y-aksen
    plt.title("Forekomster af bogstaver i navne") #Sætter titel på grafen
    plt.show()


    #Generate word cloud
    WC_test = wc.WordCloud(width = 1000, height = 500).generate_from_frequencies(bogstav_tæller_sorted)
    plt.figure(figsize=(15,8))
    plt.imshow(WC_test)
    plt.show()


    #List with Name length for each name
    Word_count_list = [int(len(element)) for element in Navne_sorteret]


    #Calculate mean and median
    Word_Count_mean = float(np.mean(Word_count_list))
    Word_count_median = float(np.median(Word_count_list))
    Word_Count_mean
    Word_count_median


    #Create a dict with count of namelenghts
    Dict_nl = {}
    for count in Word_count_list:
        if count in Dict_nl:
            Dict_nl[count] += 1 
        else:
            Dict_nl[count] = 1

    Dict_nl_sorted = sort_dict(Dict_nl)

    #Plot
    plt.grid()
    plt.bar(Dict_nl_sorted.keys(), Dict_nl_sorted.values(), width = 1, edgecolor="white", linewidth=0.7)
    plt.xlim(1,11)
    plt.xticks(np.arange(1,11))
    plt.show()


    #test for duplicate
    #Can use Dict since they can't store duplicate keys
    Name_dict = {}
    for name in Navne_sorteret:
        Name_dict[name]=1

    #Check if any duplicates
    len(Name_dict)-len(Navne_split)
    print("since there are the same amount of elements in the dictionary there are no duplicate names")