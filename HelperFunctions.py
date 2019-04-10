import nltk
from nltk.corpus import stopwords,wordnet
from nltk.stem import WordNetLemmatizer
from six import string_types
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from appos import appos
import math

lemmatizer = WordNetLemmatizer()
stop_words=set(stopwords.words('english'))
sid = SentimentIntensityAnalyzer()
word_idf={}

def run_sentiment_analysis(text):
    sentiment_tuple=[]
    ss=sid.polarity_scores(text)
    for k in ss:
        sentiment_tuple.append(ss[k])
    return tuple(sentiment_tuple)

def text_expander(word):
    if word in appos.keys():
        return appos[word]
    return word


def sw_and_lemmatize(text):
    lemmatized=[]
    for word in text.split():
        # removing stopwords
        if not word in stop_words:
            # stemming word
            temp=lemmatizer.lemmatize(word)
            lemmatized.append(temp)
    return ' '.join(lemmatized) 


 
def word_tf(word, text):
    if len(' '.join(text))==0:
        return 0.0
    word_count=' '.join(text).count(word)
    return float(word_count) / len(' '.join(text))
 
 
def idf_calculator(text):
    global word_idf
    vocabulary = set()
    for sentence in text:
        for word in sentence.split():
            vocabulary.update(word)
    
    vocabulary = list(vocabulary)    
    DOCUMENTS_COUNT = len(text)
    
    for sentence in text:
        words = set(sentence.split())
        for word in words:
            if word not in word_idf.keys():
                word_idf[word]=0
            word_idf[word] += 1
    
    for word in vocabulary:
        if word in word_idf.keys():
            word_idf[word] = math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
    return vocabulary,word_idf

## ---------- NOT AS ACCURATE ---------------------

# def get_wordnet_pos(word):
#     tag = nltk.pos_tag([word])[0][1][0].upper()
#     tag_dict = {"J": wordnet.ADJ,
#                 "N": wordnet.NOUN,
#                 "V": wordnet.VERB,
#                 "R": wordnet.ADV}

#     return tag_dict.get(tag, wordnet.NOUN)

# def lemmatize_pos(text):
#     lemmatized=[]
#     for word in text.split():
#         # removing stopwords
#         if not word in stop_words:
#             # stemming word
#             temp=lemmatizer.lemmatize(word,get_wordnet_pos(word))
#             lemmatized.append(temp)
#     return ' '.join(lemmatized) 