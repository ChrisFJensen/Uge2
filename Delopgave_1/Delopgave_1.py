import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import wordcloud as wc

def open_data(file_name: str):
    # Open file name and convert it to a list of names
    data = open(file_name,"r").readlines()
    data_split = data[0].split(",")
    data_split = [line.strip() for line in data_split]
    return data_split

def sort_data(data: list, sort="alphabetically"):
    if sort=="alphabetically":
        return sorted(data)
    elif sort in ["length","len"]:
        return sorted(data, key=len)
    else:
        print("Unsopported sort type given")
        return data


def letter_counter(data: list):
    #Empty dict to store the count for each letter
    letter_count = {}
    #Loop over each data entry
    for line in data:
        #Loop for each letter in line
        for letter in line.lower():
            # Check whether letter already added to dict.
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return  letter_count

#Function to sort dict keys alphabetically (for plot purpose)
def sort_dict(Dict: dict):
    Dict_keys = list(Dict.keys())
    Dict_keys.sort()
    Dict_sorted = {i: Dict[i] for i in Dict_keys}
    return(Dict_sorted)


def word_count_mean_median(data: list):
    # Convert to list of name lengths
    data_name_length = [int(len(line)) for line in data]
    #Create empty dict to store mean and median of name lenght
    mean_median_dict = {}
    #Uses numpys mean and median to get the values for me
    mean_median_dict["mean"] = float(np.mean(data_name_length))
    mean_median_dict["median"] = float(np.median(data_name_length))
    return mean_median_dict

def word_length_counter(data: list):
    #Convert to list of name lengths
    data_name_length = [int(len(line)) for line in data]
    #Create empty dict to store count for each name length
    lenght_dict = {}
    # Count how many times a length appears
    for length in data_name_length:
        if length in lenght_dict:
            lenght_dict[length] += 1
        else:
            lenght_dict[length] = 1
    return lenght_dict


def check_dupe(data: list):
    #Create a dict to store names as keys since they can't be duplicates
    unique_dict = {}
    for name in data:
        unique_dict[name] = 1
    #Checks if there are the same amount of names in list as in dict
    difference = len(data)-len(unique_dict)
    #Print depend on result
    if difference == 0:
        print("No duplicates were found in the data")
    else:
        print("The data contained duplicates")


if __name__ == "__main__":
    #Read data to a list
    name_data = open_data("Data/Navneliste.txt")
    print("Unsorted:")
    print(name_data[:10])
    
    # Sort alphabetically
    name_data_sorted = sort_data(name_data)
    print("Sorted alphebetically:")
    print(name_data_sorted[:10])

    #Sort by length
    name_data_sorted_len = sort_data(name_data,"len")
    print("Sorted by length: ")
    print(name_data_sorted_len[:10])

    #Counts the letters
    letter_count = letter_counter(name_data)

    #Sorts the keys alphabetically
    letter_count = sort_dict(letter_count)
    print(f"a appears: {letter_count.get("a",0)} times")
    print(f"æ appears: {letter_count.get("æ",0)} times")

    # Plot letter usage as a bar plot
    plt.bar(letter_count.keys(), letter_count.values(), width = 1, edgecolor="white", linewidth=0.7)
    plt.xlabel("Bogstaver") #Labels X-axis
    plt.ylabel("Forekomster") #Labels Y-axis
    plt.title("Forekomster af bogstaver i navne") #Adds title to plot
    plt.show()

    #Generate word cloud
    WC_test = wc.WordCloud(width = 500, height = 250, background_color="white").generate_from_frequencies(letter_count)
    plt.imshow(WC_test)
    plt.title("Letter Wordcloud")
    plt.show()

    #Analyse name length
    name_length_mean_median = word_count_mean_median(name_data)
    print(f"Mean is: {name_length_mean_median["mean"]}")
    print(f"Median is: {name_length_mean_median["median"]}")

    # Create dict of name_lengths for plotting purposes
    name_length_count = word_length_counter(name_data)
    name_length_count = sort_dict(name_length_count)
    
    #Plot
    plt.bar(name_length_count.keys(), name_length_count.values(), width = 1, edgecolor="white", linewidth=0.7)
    plt.xlim(1,11)
    plt.xticks(np.arange(1,11))
    plt.title("Distribution of letter length")
    plt.show()

    # Check if there is duplicates in data
    check_dupe(name_data)