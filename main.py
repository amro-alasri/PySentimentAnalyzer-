import argparse
from newspaper import Article
from textblob import TextBlob

def extract_information_and_sentiment(url):
    # Create an Article object and download the article
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Extract information from the article
    text = article.summary
    print("\nArticle Text:\n", text)

    analyze_sentiment(text)

def analyze_sentiment(text):
    # Analyze sentiment using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print("Sentiment:", sentiment)

def read_text_from_file(file_path):
    # Read text from a file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Extract information and sentiment analysis from a news article.")
    parser.add_argument("--url", help="URL of the news article")
    parser.add_argument("--file", help="Path to a text file containing the article content")
    args = parser.parse_args()

    if args.url:
        extract_information_and_sentiment(args.url)
    elif args.file:
        text = read_text_from_file(args.file)
        if text:
            analyze_sentiment(text)
    else:
        print("Error: Either --url or --file must be provided.")
        parser.print_help()

if __name__ == "__main__":
    main()
