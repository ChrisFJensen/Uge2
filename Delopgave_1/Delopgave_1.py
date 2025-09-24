import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import wordcloud as wc

#Indlæs filen med navne
Navne = open("Data/Navneliste.txt", "r").readlines()

#Split navne op så de hver især er et element i en liste
Navne_split = Navne[0].split(",")

#Fjern eventuelle mellemrum i starten og slutningen af hvert navn
Navne_split = [navn.strip() for navn in Navne_split]
print(Navne_split)

#Sorter navnene i alfabetisk rækkefølge
Navne_sorteret = sorted(Navne_split)
print(Navne_sorteret)

#Sorter Navne efter længde
Navne_sorteret_længde = sorted(Navne_split, key=len)
print(Navne_sorteret_længde)


#Pythondictionary til at tælle antal forekomster af hvert bogstav
bogstav_tæller = {} #Laver et tomt dictionary
for navn in Navne_sorteret: #Tjekker hvert navn i listen
    for bogstav in navn.lower(): #Tjekker hvert bogstav i navnet, gør det til små bogstaver
        if bogstav in bogstav_tæller: #Tjekker om bogstavet allerede er i dictionary
            bogstav_tæller[bogstav] += 1 #Hvis det er, så øg tælleren med 1
        else:
            bogstav_tæller[bogstav] = 1 #Hvis det ikke er, så sæt tælleren til 1

bogstav_tæller.get("a", 0) #Tjekker om det virker med a
bogstav_tæller.get("æ", 0) #Tjekker om det virker med æ, som ikke burde optræde


## Kig på at få sorteret keys i alfabetisk rækkefølge
plt.hist(bogstav_tæller.keys(), weights=bogstav_tæller.values())
plt.xlabel("Bogstaver") #Sætter label på x-aksen
plt.ylabel("Forekomster") #Sætter label på y-aksen
plt.title("Forekomster af bogstaver i navne") #Sætter titel på grafen
plt.show()

Word_count_list = [int(len(element)) for element in Navne_sorteret] #Laver en list med længden af hvert element

Word_Count_mean = float(np.mean(Word_count_list)) #udregn gennemsnittet
Word_count_median = float(np.median(Word_count_list)) #udregn medianen

#Dette var en tidligere implementation for det ovenstående
Navnelængde_tæller = {}
for navn in Navne_sorteret: #Laver den samme metode med med ord lngde istedet for bogstaver
    if len(navn) in Navnelængde_tæller:
        Navnelængde_tæller[len(navn)] += 1
    else:
        Navnelængde_tæller[len(navn)] = 1

#Sortering af keys
NLT_keys = list(Navnelængde_tæller.keys())
NLT_keys.sort()
NLT_sorted = {i: Navnelængde_tæller[i] for i in NLT_keys}
NLT_sorted

#Plot
plt.bar(NLT_sorted.keys(), NLT_sorted.values(), width = 1, edgecolor="white", linewidth=0.7)
plt.plot(NLT_sorted.keys(), NLT_sorted.values(), linewidth = 2)
plt.xlim(1,11)
plt.xticks(np.arange(1,11))
plt.grid()
plt.show()



## Der er ikke nogle duplikater så venter lige med det