import spacy
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')


nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):

    text_lower = text.lower()


    stop_words = set(stopwords.words('english'))
    tokens = text_lower.split() 
    
    
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return filtered_tokens


if __name__ == "__main__":
    text = input("Enter the text: ")
    processed_text = preprocess_text(text)
    
    print("\nProcessed Text (Lowercased and without stopwords):")
    print(" ".join(processed_text))

