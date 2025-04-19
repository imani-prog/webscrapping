import tweepy
import json

# Replace with your actual bearer token
bearer_token = "YOUR_BEARER_TOKEN"

# Define a listener class to handle incoming tweets
class MyStreamListener(tweepy.StreamingClient):
    def __init__(self, bearer_token, file_path):
        super().__init__(bearer_token)
        self.file_path = file_path
        self.file = open(file_path, "a", encoding="utf-8")  # Open file in append mode

    def on_tweet(self, tweet):
        try:
            # Write tweet data to file as JSON
            self.file.write(json.dumps({"text": tweet.text, "lang": tweet.lang}) + "\n")
            print(f"Tweet saved: {tweet.text}")
        except Exception as e:
            print(f"Error writing tweet to file: {e}")

    def on_exception(self, exception):
        print(f"Exception occurred: {exception}")
        self.file.close()  # Ensure the file is closed on exception
        return super().on_exception(exception)

    def disconnect(self):
        self.file.close()  # Close the file when disconnecting
        super().disconnect()

# Main script
try:
    print("Setting up Twitter API authentication...")
    stream = MyStreamListener(bearer_token=bearer_token, file_path="tweets.txt")
    print("Authentication successful.")

    print("Starting Twitter Stream with filters...")
    stream.add_rules(tweepy.StreamRule("clinton OR trump OR sanders OR cruz"))  # Add filter rules
    stream.filter()  # Start streaming
except tweepy.TweepyException as e:
    print(f"Tweepy error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
