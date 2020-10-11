# Octocat Drawer - KnightHacks2020

Twitter bot at https://twitter.com/CRMARKH2020 that posts edits of OctoCat drawn by ML to win the 
Octocat drawing contest by GithubEducation. 

## Tools

-Python 3.8
-Twitter Developer Account
-Tweepy
-pix2pix

## ML

Pix2pix model that trains on drawings and edits of octocat to create its own drawings of GitHub's 
mascot. The model is hosted on Google Cloud. 

## Bot

The bot is a Google Cloud Function that is scheduled to run every 10 minutes using a scheduler. This 
makes it so that the Cloud resources are only used during function calls. The code uses Python and 
the Python package, tweepy, to connect to the bot account and post the picture by linking to an 
image file hosted on GitHub. The image is selected based on the number of statuses posted to ensure 
the message changes each time more often than would be random. 
