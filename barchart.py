import matplotlib.pyplot as plt
import collections
import numpy as np

path = "text.txt"

with open (path, 'r', encoding = "utf-8") as file:
    string = file.read()
    string_list = string.split()
    string_dict = {}

for word in string_list:
    if word in string_dict:
        string_dict[word] = string_dict[word] + 1
        #increment the count
    else:
        string_dict[word] = 1
        
sortedwords = sorted(string_dict.items(), key=lambda kv: kv[1])
newdict = collections.OrderedDict(sortedwords)

frequency = newdict.values()
words = newdict.keys()
n = np.arange(len(newdict))


bar = plt.bar(n, frequency, facecolor = "yellow", alpha = 0.5)
plt.title("Frequency of words", fontsize = 24)
plt.xticks(n, words, rotation = 90)
plt.xlabel("Frequency", fontisize = 16)
plt.ylabel("Words", fontsize = 16)
plt.show()






