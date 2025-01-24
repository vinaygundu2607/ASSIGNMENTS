from collections import Counter

def calculate_word_frequency(text):
   
    words = text.lower().split()
   
    word_counts = Counter(words)
    return word_counts


if __name__ == "__main__":
    text = input("Enter the text: ")
    word_counts = calculate_word_frequency(text)
    
    print("\nWord Frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
