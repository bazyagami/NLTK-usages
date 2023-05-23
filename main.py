
# cleaning the text :
# making sure everything is in lower case
# remove all the punctuations
#make trans - make transformations 3 arg - 'char to replace' 'char to replace w' 'char to delete'


import string
from collections import Counter
import matplotlib.pyplot as plt

#cleaning the words

text = open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
print(lower_case)
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)

# tokenization breaks the string into small chunks called tokens that helps understanding the context
#stop words are words that basically don't add any meaning to the sentence
#NLTK has ready-made stop words

tokenized_words=cleaned_text.split()
print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

print(final_words)

#NLP algo
#check if the final word is present in the emo text file
#if present add emo to emotion_list
#count each emotion in the emotion_list

emotion_list=[]

with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()    #too automatically format the x-axis to acc all the emotions
plt.savefig('graph.png')
plt.show()

#use zuck, steve job's speeches to class
