import requests

# Define the company to track
COMPANY = "Tesla"

# List to hold formatted news articles
formatted_news = []

def get_news(company, up_down, percentage):
    """Fetches the latest news articles related to the specified company."""
    # Set up parameters for the News API request
    parameters = {
        "apiKey": "abcdef",  # Replace with your actual News API key
        "q": company,        # Query for the specified company
        "language": "en",    # Language of the news articles
        "pageSize": 3        # Limit to 3 articles
    }
    # Make the API request
    response1 = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response1.raise_for_status()  # Raise an error for bad responses
    data1 = response1.json()["articles"]  # Extract articles from the response
    three_articles = data1[:3]  # Get the top 3 articles
    # Format the articles for output
    formatted_article = [
        f"{company} {up_down}{percentage} Headline: {article['title']} \n Brief: {article['description']}"
        for article in three_articles
    ]
    return formatted_article

# Parameters for fetching stock data
parameters_stock = {
    "function": "TIME_SERIES_DAILY",  # Specify the API function
    "symbol": "TSLA",                  # Stock symbol for Tesla
    "apikey": "6Q8TGJL77RKIJ0PE"       # Replace with your actual Alpha Vantage API key
}

# Make the API request for stock data
response = requests.get(url="https://www.alphavantage.co/query", params=parameters_stock)
response.raise_for_status()  # Raise an erro
