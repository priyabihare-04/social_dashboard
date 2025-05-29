import requests
from decouple import config
from requests_oauthlib import OAuth1


BEARER_TOKEN = config('TWITTER_BEARER')

def get_user_tweets():
    username = "BiharePriy19663"  

    url = f"https://api.twitter.com/2/users/by/username/{username}"

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
    }

    user_resp = requests.get(url, headers=headers)

    if user_resp.status_code != 200:
        print("User fetch error:", user_resp.text)
        return []

    user_id = user_resp.json()['data']['id']

    tweet_url = f"https://api.twitter.com/2/users/{user_id}/tweets?max_results=5&tweet.fields=created_at"

    tweet_resp = requests.get(tweet_url, headers=headers)

    if tweet_resp.status_code != 200:
        print("Tweet fetch error:", tweet_resp.text)
        return []

    return tweet_resp.json().get('data', [])



def post_tweet(status_text):
    url = "https://api.twitter.com/2/tweets"

    auth = OAuth1(
        config("TWITTER_KEY"),
        config("TWITTER_SECRET"),
        config("TWITTER_ACCESS_TOKEN"),
        config("TWITTER_ACCESS_SECRET")
    )

    payload = {
        "text": status_text
    }

    response = requests.post(url, auth=auth, json=payload)
    print("Tweet Post Response:", response.json())  # For debugging

    return response.status_code == 201

