# Import packages
import pandas as pd
import json

def load_tweets(file_path):
    tweets_data = []
    try:
        print(f"Opening file: {file_path}")
        with open(file_path, "r") as tweets_file:
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
        print("Please ensure the file exists in the current directory.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        exit()
    return tweets_data

def create_dataframe(tweets_data):
    try:
        df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
        print("DataFrame created successfully.")
        print(df.head())
        return df
    except KeyError as e:
        print(f"Key error: {e} - Ensure the tweets contain 'text' and 'lang' fields.")
    except Exception as e:
        print(f"An unexpected error occurred while creating the DataFrame: {e}")
        return None

# Main script
tweets_data = load_tweets('tweets.txt')
df = create_dataframe(tweets_data)
