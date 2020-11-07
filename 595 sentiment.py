
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob

def Sentiment_anlysis(sentence):
    blob = TextBlob(sentence)
    score=np.array([])
    for sentence in blob.sentences:
        score=np.append(score,sentence.sentiment.polarity)

    return score



def main():
    text = '''
    The titular threat of The Blob has always struck me as the ultimate movie
    monster: an insatiably hungry, amoeba-like mass able to penetrate
    virtually any safeguard, capable of--as a doomed doctor chillingly
    describes it--"assimilating flesh on contact.
    Snide comparisons to gelatin be damned, it's a concept with the most
    devastating of potential consequences, not unlike the grey goo scenario
    proposed by technological theorists fearful of
    artificial intelligence run rampant.
    '''
    score=Sentiment_anlysis(text)
    print(score)
    plt.hist(score)
    plt.show()


if __name__ == '__main__':
    main()