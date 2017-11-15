from subprocess import check_output
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import nltk
import csv
import extract_bigrams
from nltk.corpus import stopwords            # Import the stop word list

mean_words_pos0=[]

data=pd.read_csv("Book1_pos.csv")

mean_words_pos=[]
n=0;

mean_words_pos0.append(extract_bigrams.freqDpos(data['Text'][i]))


def get_words_in_rev(rev):
        all_words=[]
        for(words) in rev:
            all_words.extend(words)
        #print(all_words);
        return all_words
        
def get_word_features(wordlist):
    #print(wordlist);
        #wordlist=nltk.FreqDist(wordlist)
    '''    
    print("\nFREQ DISTR :");
    wordfreq=[]
    #print(wordlist[8]);
    n=0

    
    for i in wordlist:
        n=n+1
        wordfreq.append(wordlist.count(i))
        print(wordfreq[0]);
        if n==100000:
            break;
    
    fieldnames = ['word', 'freq']
    #print("\naaaaaaa");
    #print(wordfreq[10]);
        #print("ffffffffffff");
        #print(wordlist);
    with open('freq_pos.csv', 'a') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
            #for i in range(0,6500):
    
        i=0;
        print("Before for:::");
    #for i in range(0,len(wordlist)):
        for i in range(0,100000):
            print(wordlist[i], wordfreq[i]);
            writer.writerow({'word':wordlist[i], 'freq':wordfreq[i]})
    '''
    firstEle_pos=[]
    firstEle_pos=[k[0] for k in wordlist ]
    print(firstEle_pos);
    

   
get_word_features(get_words_in_rev(mean_words_pos0))