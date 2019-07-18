'''
Parsing through the submission and comment tree; rough work for identifying 
Redditor and Submission object attributes.
'''

# Imports
import praw
from praw.models import MoreComments
import requests
import requests.auth
from config import client_id, client_secret, user_agent
from config import reddit_un, reddit_pw

import pandas as pd
import numpy as np
import nltk

# Instantiate
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent,
                     username = reddit_un,
                     password = reddit_pw)

# Read only flag
# dir(object_name) to get attributes of an object (if praw documentation poor)
reddit.read_only = False
# print("Read only flag: ", reddit.read_only)
subreddit = reddit.subreddit('watchexchange')

# Instantiate empty dataframe
colnames = ['Title', 'Submission Score', 'Submission ID', 'Submission URL', 'Prices', 'Seller']
df = pd.DataFrame(columns = colnames)

# Iterating through comments
for submission in subreddit.new(limit = 5):
    submission.comments.replace_more(limit = None)
    print("* "*50)
    print(submission.selftext) # submission text
    print("AUTHOR NAME: ", submission.author.name) # submission author
    print("AUTHOR CKARMA: ", submission.author.comment_karma) # author comment karma count
    print("AUTHOR LKARMA: ", submission.author.link_karma) # author link karma count
    print("SUBMISSION ID: ", submission.id) # submission id
    print("SUBMISSION PERMALINK: ", submission.permalink) # submission url
    print("* "*50)
    for comment in submission.comments.list():
        # if comment.author is None: 
        #     continue
        if not comment.author:
            continue
        if str(comment.author.name) != "AutoModerator":
            print("isAutomod flag: ", str(comment.author.name) != "AutoModerator")
            print(type(comment.author))
            # print(comment.author.name)
            print(comment.body) # body
        else:
            continue

df.head()


'''
WIP
def parse_comments(top_comment):
    # print(top_comment.id)
    # print(top_comment.body)
    for comment in top_comment.replies:
        sparse_comments(comment)

for submission in subreddit.new(limit = 1):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments:
        print(comment.author)
        # comment.author returns a ``Redditor`` object; comment.author.name returns the username
        if comment.author.name is not "AutoModerator": 
            print("parsed")
            parse_comments(comment)
        else:
            pass
'''