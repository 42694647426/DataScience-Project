import json
import os
import sys
import math

def Nmaxelements(data, N):
    data = dict(sorted(data.items(), key=lambda item: item[1] , reverse=True))
    data = list(data)[:N]
    return data


def main(wordCount , number):

    wordFreq = {}
    for category in wordCount.keys():
        categoryDic = {}
        for word in wordCount[category].keys():
            totalCategory = 0
            categoryTotal = wordCount[category][word]
            for category2 in wordCount.values():
                if word in category2:
                    totalCategory = totalCategory + 1
            categoryDic[word] = categoryTotal * math.log(5/totalCategory,10)
        wordFreq[category] = Nmaxelements(categoryDic,number)
    return wordFreq

if __name__ == "__main__":

    input_file = sys.argv[2]
    number = int(sys.argv[4])

    f = open(input_file,'r')
    wordCount = json.load(f)
    f.close()

    wordFreq  = main(wordCount , number)
    print(wordFreq)
