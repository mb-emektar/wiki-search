import nltk
import re
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

    def split_query(self, query):
        # Regex pattern to match quoted text
        quoted_pattern = r'\".*?\"'

        # Find all quoted text in the query
        quoted_texts = re.findall(quoted_pattern, query)

        # Remove quoted text from the query
        query_no_quoted = re.sub(quoted_pattern, '', query)

        # Remove extra spaces
        query_no_quoted = ' '.join(query_no_quoted.split())

        return query_no_quoted, quoted_texts

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
        # Regex to find text within quotes
        quoted_texts = re.findall(r'\".*?\"', text)
        
        # Remove punctuation from non-quoted text
        def remove_punct(match):
            part = match.group(0)
            if part in quoted_texts:
                return part  # Keep quoted text as is
            else:
                return "".join([char for char in part if char not in string.punctuation])

        # Apply the remove_punct function to each part of the text
        no_punctuation_text = re.sub(r'[^\" ]+', remove_punct, text)
        return no_punctuation_text



    def process_text(self, text):
        no_quoted_text, quoted_texts = self.split_query(text)
        no_quoted_text = self.remove_punctuation(no_quoted_text)
        print(no_quoted_text)
        print("--------------")
        tokens = self.tokenize(no_quoted_text)
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

        # Combine processed_text and quoted_texts
        merged_text = processed_text + " " + " ".join(quoted_texts)
        print(merged_text)
        
        return merged_text
