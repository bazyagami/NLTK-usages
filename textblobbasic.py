text1="today is an excellent day"
text2="today is a horrible day"

from textblob import TextBlob
t=TextBlob(text1)
t1=TextBlob(text2)
print(t.sentiment)
print(t1.sentiment)

text="heaalth is wealtth"
spell=TextBlob(text)
print(spell.correct())