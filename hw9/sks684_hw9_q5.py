'''
Simran Soin
CS-UY 1134
HW9 Q5
'''
from UnsortedArrayMap import UnsortedArrayMap

class InvertedFile:
    def __init__(self, file_name):
        self.all_words = UnsortedArrayMap()
        f = open(file_name, "r")
        count = 0
        for line in f:
            line = line.strip()
            line = line.split(" ")
            if len(line)<2:
                continue
            else:
                for word in line:
                    word = word.lower()
                    word = word.strip(",")
                    if len(word)<1:
                        continue
                    else:
                        try:
                            self.all_words[word]
                            self.all_words[word].append(count)

                        except KeyError:
                            self.all_words[word] = [count]
                        count += 1
    def indices(self,word):
        try:
            return self.all_words[word]
        except KeyError:
            return list()
