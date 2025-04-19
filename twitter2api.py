# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

try:
    print(f"Opening file: {tweets_data_path}")
    with open(tweets_data_path, "r") as tweets_file:
        print("Reading tweets from file...")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e} - Skipping line.")
    print("File reading completed.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
    print("Please ensure the file 'tweets.txt' exists in the current directory.")
    print("If you don't have the file, create it and add JSON-formatted tweet data.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# Ensure there is at least one tweet before accessing keys
if tweets_data:
    print("Printing keys of the first tweet:")
    print(tweets_data[0].keys())
else:
    print("No tweets found in the file.")
