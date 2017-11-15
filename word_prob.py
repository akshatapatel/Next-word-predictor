
import pandas as pd
import csv
print("HI");
data_pos=pd.read_csv("freq_pos.csv");

firstEle_pos=[]
l=0
for l in range(1,len(data_pos),2):
    str1=[];
    
    flag=0;
    for k in data_pos['word'][l]:
        if k=="(":
            continue;
        if k=="'":
            if flag==0:
                flag=1;
                continue;
            
            if flag==1:
                break;
            
        else:
            str1.append(k);
    
    str2="";
    str2="".join(str1)
    str2=str.lower(str2);
    #print(str1);
    firstEle_pos.append(str2);
#firstEle_neg=[k[0] for k in arr1 ]
#print(firstEle_pos);
print("Positive first ele done!");
comb_freq=0;
all_good=[]
all_bad=[]
print(len(data_pos),len(firstEle_pos))
num=range(1,len(data_pos),2);
print(len(num));
i=-1;
for j in range(1,len(data_pos),2):
    if data_pos["freq"][j]!="freq":
        i=i+1
        comb_freq_pos=data_pos["freq"][j]
        print(data_pos["word"][j]);
        print(firstEle_pos[i]);
        #print("aaaaaa");
        ind_first_freq_pos=(firstEle_pos.count(firstEle_pos[i]))
        #print(comb_freq_pos,ind_first_freq_pos);
        prob=(comb_freq_pos)/(ind_first_freq_pos)
        #print(goodness)
        all_good.append((data_pos["word"][j],prob))
i=-1;    

        

word_prob_arr=[]
fieldnames = ['word', 'prob'] 
with open('word_prob_arr.csv', 'a') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for j in range(0,len(all_good)):
            writer.writerow({'word':all_good[j][0], 'prob':all_good[j][1]})
            break; 
                 
    
            

