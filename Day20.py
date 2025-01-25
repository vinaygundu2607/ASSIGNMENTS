import re
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def clean_text(text):
    """
    Clean the input text by converting it to lowercase and removing special characters.
    :param text: Input text as a string.
    :return: Cleaned text as a string.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def extract_emails(text):
    """
    Extract all email addresses from the given text using regular expressions.
    :param text: Input text as a string.
    :return: List of email addresses.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def fetch_webpage_title(url):
    """
    Fetch and return the title of a webpage using requests and BeautifulSoup.
    :param url: URL of the webpage as a string.
    :return: Title of the webpage as a string.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "No title found"
    else:
        return f"Failed to fetch webpage, status code: {response.status_code}"

def generate_wordcloud(text, output_filename):
    """
    Generate a WordCloud from the given text and save it as an image.
    :param text: Input text as a string.
    :param output_filename: Output filename for the WordCloud image.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    wordcloud.to_file(output_filename)
    print(f"WordCloud saved as {output_filename}")

if __name__ == "__main__":
    # Clean a sample input
    sample_input = 'Hello, World! Welcome to NLP 101.'
    cleaned_text = clean_text(sample_input)
    print("Cleaned Text:", cleaned_text)

    # Extract emails from a sample input
    email_input = 'Contact us at support@example.com and sales@example.org.'
    emails = extract_emails(email_input)
    print("Extracted Emails:", emails)

    # Fetch and print the title of a webpage
    test_url = 'https://example.com'
    title = fetch_webpage_title(test_url)
    print("Webpage Title:", title)

    # Generate a WordCloud from sample text
    wordcloud_text = 'data science machine learning artificial intelligence'
    generate_wordcloud(wordcloud_text, 'wordcloud.png')
