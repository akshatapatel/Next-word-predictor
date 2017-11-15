# NEXT WORD SUGGESTION
implementation of text classification using bigrams and then using them predicting the next word of a sentence. We have used a yelp dataset which consists of reviews and its
sentiment for multiple restaurant. We have employed Naive Bayes approach for this project. The outcome of the project is that when the user inputs a word, it will predict the next word and will continue until the user wants to stop. 

# FUNCTIONS:
The various libraries used are:
●	Pandas: Used to read the csv file.
●	Nltk (Natural Language tool kit) : to remove unimportant/unnecessary words from the dataset.
The various functions of python employed are:
●	Reviews are extracted from the HTML or XML files using the BeautifulSoup library.
example = BeautifulSoup(Text,"lxml")
Text=example.get_text();
●	Punctuations are removed from the reviews using the string substitution operation.
Text= re.sub("[^a-zA-Z]"," ",Text);
●	The entire review is split into an array consisting of its words as individual elements.
lower_case = Text.lower()
tempwords = lower_case.split()

●	To split the text into pairs of words(bigrams)
 warr.append(Text)
bigrams = [b for l in warr for b in zip(l.split(' ')[:-1], l.split(' ')[1:])]

