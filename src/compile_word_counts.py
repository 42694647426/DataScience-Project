import pandas as pd
import json
import os
import sys
import re


def main(input_file):

    # Get Pony dialogues
    dialogue = pd.read_csv(input_file, sep='\t')
    #dialogue = dialogue.head(100)
    dialogues = {}
    dialogues['Omicron'] =  dialogue[dialogue["Topic"]=='O']['Twitts']
    dialogues['Vaccine'] =  dialogue[dialogue["Topic"]=='V']['Twitts']
    dialogues['News'] =  dialogue[dialogue["Topic"]=='N']['Twitts']
    dialogues['Influences'] =  dialogue[dialogue["Topic"]=='I']['Twitts']
    dialogues['Opinion'] =  dialogue[dialogue["Topic"]=='P']['Twitts']



    # Make everything lower case and take all puntionations
    for category in dialogues.keys():
        dialogues[category] = dialogues[category].replace(r'[()\[\],-.?!:;#&]+', ' ', regex=True)
        dialogues[category] = dialogues[category].str.lower()

    # Delete stopwords from the file   
    dirname = os.path.dirname(__file__)
    stopwordsFile = os.path.join(dirname, '../data/stopwords.txt')
    with open(stopwordsFile) as stopwords:
        for stopwordLine in stopwords:
            stopword = stopwordLine.rstrip()
            for category  in dialogues.keys():
                dialogues[category] = dialogues[category].replace(r'\b%s\b' % re.escape(stopword),' ', regex=True)

    # Delete words with non alphabetic characters Inclusidng @ and #
    for category  in dialogues.keys():
        dialogues[category] = dialogues[category].replace(r'[^\s]*[^a-z\s][^\s]*', ' ', regex=True)

    wordCount = {}
    # Word count
    for category in dialogues.keys():
        categoryDic = {}
        for dialog in dialogues[category]:
            for word in dialog.split():
                if (word not in categoryDic):
                    categoryDic[word]  = int(dialogues[category].str.count(r'\b%s\b' % re.escape(word)).sum())
        wordCount[category] = categoryDic
    
    # Delete words that don't appear more than 5
    wordCountFinal = {}
    for category in wordCount.keys():
        categoryDic = {}
        for word in wordCount[category].keys():
            count = 0
            for category2 in wordCount.values():
                if word in category2: count = count + category2[word]
            if count >= 5: categoryDic[word] = int(wordCount[category][word])
        wordCountFinal[category] = categoryDic

    return wordCountFinal

if __name__ == "__main__":
    input_file = sys.argv[4]
    output_file = sys.argv[2]
    wordCount = main(input_file)
    # Write to outou
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(wordCount , f)

