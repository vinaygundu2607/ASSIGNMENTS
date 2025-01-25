import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string, stem_text
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stopwords, stemming, and lemmatizing.
    """
    # Convert text to lowercase and tokenize
    tokens = simple_preprocess(text)
    
    # Remove stopwords
    tokens_no_stopwords = [remove_stopwords(word) for word in tokens]
    
    # Apply stemming
    stemmed_tokens = [stemmer.stem(word) for word in tokens_no_stopwords]
    
    # Apply lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
    
    return lemmatized_tokens

# Read the sample text file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    return processed_text

# Example usage
if __name__ == "__main__":
    # Replace with your file path
    file_path = "c:\\Users\\vinay\\Downloads\\sample.txt"
    
    try:
        processed_text = process_file(file_path)
        print("Processed Text:")
        print(processed_text)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please make sure the file exists.")
