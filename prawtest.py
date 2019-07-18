# Imports
import praw
import requests
import requests.auth
from config import client_id, client_secret, user_agent
from config import reddit_un, reddit_pw

import pandas as pd
import numpy as np

# Instantiate
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent,
                     username = reddit_un,
                     password = reddit_pw)

# Read only flag
reddit.read_only = False
print("Read only flag: ", reddit.read_only)


subreddit = reddit.subreddit('watchexchange')

print("Subreddit name: ", subreddit.display_name)   # Output: redditdev
print("Subreddit title: ", subreddit.title)         # Output: reddit Development

limit_no = 5
colnames = ['Title', 'Submission Score', 'Submission ID', 'Submission URL', 'Prices', 'Seller']
df = pd.DataFrame(columns = colnames)

for submission in subreddit.new(limit = limit_no):
    entry = [submission.title, submission.score, submission.id, submission.url, 0, submission.author]
    df2 = pd.DataFrame([entry], columns = colnames)
    df = pd.concat([df2, df])

    submission_comments = submission.comments.list()
    print(submission_comments)