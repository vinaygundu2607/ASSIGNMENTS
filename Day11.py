import os
import gensim
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.utils import simple_preprocess
from gensim.parsing.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

# Download necessary NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def preprocess_text(text):
    """
    Preprocess the input text: tokenization, removing stop words, stemming, and lemmatization.
    :param text: Input text as a string.
    :return: Preprocessed tokens as a list.
    """
    # Tokenization and removing stop words
    text = remove_stopwords(text)
    tokens = simple_preprocess(text)

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in stemmed_tokens]

    return lemmatized_tokens

def get_wordnet_pos(word):
    """
    Map POS tag to the first character accepted by WordNetLemmatizer.
    :param word: A word as a string.
    :return: POS tag compatible with WordNetLemmatizer.
    """
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        'J': wordnet.ADJ,
        'N': wordnet.NOUN,
        'V': wordnet.VERB,
        'R': wordnet.ADV
    }
    return tag_dict.get(tag, wordnet.NOUN)

def process_file(file_path):
    """
    Read and preprocess text from a file.
    :param file_path: Path to the input text file.
    :return: List of preprocessed tokens.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return preprocess_text(text)

def tokenize_text(text):
    """
    Tokenize a paragraph into sentences and words.
    :param text: Input text as a string.
    :return: Tuple of list of sentences and list of word tokens.
    """
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    return sentences, words

if __name__ == "__main__":
    # Path to your sample text file
    sample_file = "sample_text.txt"

    try:
        # Process the file
        tokens = process_file(sample_file)
        print("Preprocessed Tokens:", tokens)

        # Tokenize text into sentences and words
        with open(sample_file, 'r', encoding='utf-8') as file:
            text = file.read()
        sentences, words = tokenize_text(text)
        print("Sentences:", sentences)
        print("Words:", words)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
