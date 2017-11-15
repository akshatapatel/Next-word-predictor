
from bs4 import BeautifulSoup

import re
 
def freqDpos(Text):

   
                                            
    example = BeautifulSoup(Text,"lxml")
    Text=example.get_text();    
                                                 #removing punctuation
    Text= re.sub("[^a-zA-Z]"," ",Text);     
    warr=[]
    Text=Text.lstrip();
    warr.append(Text);
    #print(warr);
    bigrams = [b for l in warr for b in zip(l.split(' ')[:-1], l.split(' ')[1:])]
    
    i=0;
    return bigrams;
    
    
