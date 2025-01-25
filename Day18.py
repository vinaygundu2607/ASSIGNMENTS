import re
import requests
from bs4 import BeautifulSoup

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
