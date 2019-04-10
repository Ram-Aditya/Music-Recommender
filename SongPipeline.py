from HelperFunctions import *

def run_pipeline(filename):
    # read in the form of lyric lists
    with open(filename,"r") as lyricfile:
        lyrics=lyricfile.readlines()

    song_sentiment=[0.0,0.0,0.0,0.0]
    lyrics=list(set(lyrics))
    lyric_sentiments=[]
    lyric_importance=[]
    processed_lyrics=[]
    
    for lyric in lyrics:
        ## PATH 1 - Sentiment analysis
        
        # Run required preprocessing for sentiment analysis
        # Essentially convert to lower case, replace commas, handle expansion of words
        cleaned_lyric="" 
        lyric = lyric.replace(',', '')
        words=lyric.split()
        for word in words:
            cleaned_lyric+=text_expander(word.lower())
            cleaned_lyric+=" "
        
        # Run to get sentiment score tuple - stop words are needed here for context!
        lyric_sentiment=run_sentiment_analysis(cleaned_lyric)
        lyric_sentiments.append(lyric_sentiment)
        
        ## PATH 2 - Determine the Importance of each lyric 
        
        # remove stopwords 
        # lemmatization
        processed_lyric=sw_and_lemmatize(cleaned_lyric)
        processed_lyrics.append(processed_lyric)

    # Running tdf-idf on vocabulary produced after processing all lyrics of the song 
    _,word_idf= idf_calculator(processed_lyrics)
    
    # Calculating average tf-idf value

    for lyric in processed_lyrics:
        lyric_avg=0
        word_count=0
        for word in lyric.split():
            if word in word_idf.keys():
                lyric_avg+=((word_tf(word, processed_lyrics)) * word_idf[word])
                word_count+=1
        if word_count!=0:
            lyric_avg/=word_count
        else:
            lyric_avg=0.0
        # average tf-idf per processed lyric
        lyric_importance.append(lyric_avg)

    # calculating simple average tf-idf for the song score
    for i in range(len(processed_lyrics)):
        for j in range(0,4):
            song_sentiment[j]=lyric_sentiments[i][j]*lyric_importance[i]
    for i in range(4):
        song_sentiment[i]/=len(processed_lyrics)
    
    #print("neg,neu,pos,cpd")
    #print(song_sentiment)
    
    return song_sentiment


if __name__ == "__main__":
    run_pipeline("../song4.txt")