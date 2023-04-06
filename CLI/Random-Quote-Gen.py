import requests
import random

response = requests.get("https://type.fit/api/quotes")

# Parse the JSON response into a list of dictionaries
quotes = response.json()

# Extract the text of each quote into a list
quote_texts = [quote["text"] for quote in quotes]

# Select a random quote
quote = random.choice(quote_texts)

# Print the quote
print(quote)
