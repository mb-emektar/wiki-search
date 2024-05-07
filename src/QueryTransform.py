import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class QueryTransform:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, text):
        tokens = word_tokenize(text)
        return tokens

    def remove_stopwords(self, tokens):
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
        return filtered_tokens

    def apply_stemming(self, tokens):
        stemmed_tokens = [self.stemmer.stem(word) for word in tokens]
        return stemmed_tokens
    
    def remove_punctuation(self, text):
        no_punctuation_text = "".join([char for char in text if char not in string.punctuation])
        return no_punctuation_text



    def process_text(self, text):
        text = self.remove_punctuation(text)
        print(text)
        print("--------------")
        tokens = self.tokenize(text)
        print(tokens)
        print("--------------")
        tokens = self.remove_stopwords(tokens)
        print(tokens)
        print("--------------")
        tokens = self.apply_stemming(tokens)
        print(tokens)
        print("--------------")
        processed_text = " ".join(tokens)
        print(processed_text)
        print("--------------")
        print("--------------")
        print("--------------")

        return processed_text
