import pandas as pd
import re
data=pd.read_csv("word_prob_arr.csv")
str1="Love love loved the atmosphere! Every corner of the coffee shop had its own style, and there were swings!!! I ordered the matcha latte, and it was muy fantastico! Ordering and getting my drink were pretty streamlined. I ordered on an iPad, which included all beverage selections that ranged from coffee to wine, desired level of sweetness, and a checkout system. I got my latte within minutes!  I was hoping for a typical heart or feather on my latte, but found myself listing out all the possibilities of what the art may be. Any ideas?"
Text=str1
words=[]
lower_case=[]
Text= re.sub("[^a-zA-Z]"," ",Text);
lower_case = Text.lower()
tempwords = lower_case.split()
words.append(tempwords)
i=1


c='yes'
word=input("Enter word :")
while c=='yes':
    print ("Start word :",word)
    j=1
    max_prob=0.0000000000000
    k=0
    while j<len(data):
        #print (data['word'][j])
        tr1=[]
        tr3=[]
        fl=0
        
        flag=0
    
        for m in (data['word'][j]):
            
            if m=="(" :
                continue;
            if m=="'":
                fl=fl+1
                if flag==0:
                    flag=1;
                    continue;
                    
                if flag==1 and fl<=3:
                    continue;
                    if fl==4:
                        break;
            if m==")":
                break;
                                        
            if m==",":
                continue;
            else:
            
                if fl>=3:
                    tr3.append(m);
                else:              
                    tr1.append(m);
                                        
                                        
            
        tr2="";
        tr2="".join(tr1)
        tr2=str.lower(tr2)
        #print "tr2 :",tr2
        tr4=""
        tr4="".join(tr3)
        tr4=str.lower(tr4)
        #print "tr4 :",tr4
        #t1=str.lower(str(R[0]))
        #t2=str.lower(str(R[1]))
        #print ("tr1 :",tr1)
        #print ("tr2 :",tr2)
        #print ("tr3 :",tr3)
        #print ("tr4 :",tr4)
        
        if word==tr2.strip():#if words[0][i]==tr2.strip():
            #print (data['word'][j])
            #print (data['prob'][j])
            if data['prob'][j]>=max_prob:
                max_prob=data['prob'][j]
                #print ("max : ",max_prob)
                k=j 
                next_word=tr4.strip('\'')
        j=j+1
        
    print (data['word'][k])
    c=input('Want more?')
    print ("tr4 :",next_word)
    word=next_word 
    print ("next word :",word)