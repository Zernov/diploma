from nltk.stem.snowball import RussianStemmer
from nltk.corpus import stopwords

from keras.preprocessing.text import text_to_word_sequence

from string import punctuation

#import nltk
#nltk.download('stopwords')

stemmer = RussianStemmer()
stemmer.stopwords = stopwords.words('russian')

def stem(news):

    result = []

    for item in news:
        temp = []

        words = text_to_word_sequence(item, filters=''.join(punctuation) + '–—01234567890')

        for word in words:
            if word not in stemmer.stopwords:
                temp.append(stemmer.stem(word))

        result += temp

    return ' '.join(result)