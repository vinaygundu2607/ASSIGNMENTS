import spacy

def pos_tagging(text):
    """
    Perform part-of-speech tagging on the given text using SpaCy.
    :param text: Input text as a string.
    :return: List of tuples containing words and their POS tags.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

if __name__ == "__main__":
    # Perform POS tagging on a sample sentence
    pos_text = 'NLP is amazing and fun to learn.'
    pos_tags = pos_tagging(pos_text)
    print("Part-of-Speech Tags:", pos_tags)
