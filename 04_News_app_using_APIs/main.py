import requests 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api = os.getenv("NEWS_API_KEY")

# Check if API key was loaded successfully
if not api:
    print("API key not found. Make sure you have set NEWS_API_KEY in your .env file.")
    exit()

while True:
    # News category options for the user
    options = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

    print("What type of US news are you interested in today?")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    # Take and validate user input for news category
    while True:
        try:
            topic = int(input(f"Choose from (1-{len(options)})\n>>"))

            if 1 <= topic <= len(options):
                query = options[topic - 1]
                break
        except:
            print("Invalid input. Please enter a number.")

    # Build the request URL using the selected category
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={query}&apiKey={api}"

    # Fetch and display news articles
    try:
        r = requests.get(url)
        data = r.json()

        if data.get("status") != "ok":
            print("Error fetching news:")

        elif not data["articles"]:
            print("No articles found for this category. Please try a different one.")

        else:
            for index, article in enumerate(data["articles"]):
                print(f"{index + 1}. {article['title']} (Source: {article['source']['name']})\nFor more details visit:- {article['url']}\n")

    except Exception as e:
        print("An error occurred:", e) 

    # Ask if the user wants to search for another category
    print("Do you want to explore another news. (y/n)")

    while True:
        another_query = input(">>").strip().lower()
        if another_query in ["y", "n"]:
            break
        else:
            print("Please choose from (y/n)")
   
    if (another_query == "n"):
            break
