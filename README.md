Stock Price and News Fetcher
This Python script retrieves the latest stock price changes for a specified company (Tesla) and fetches related news articles when significant price movements occur. It utilizes the News API and Alpha Vantage API to gather data and presents the results in a formatted manner.

Features
Stock Price Retrieval: Fetches daily stock prices for Tesla using the Alpha Vantage API.
News Article Fetching: Gathers the latest news headlines related to Tesla when there’s a significant price change (greater than 1%).
Formatted Output: Displays the news articles with a summary that includes the price change direction and percentage.
Requirements
Python 3.x
requests library (install via pip install requests)
API keys for News API and Alpha Vantage (replace the placeholders with your actual keys)
