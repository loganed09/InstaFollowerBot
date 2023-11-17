import os
from instafollower import InstaFollower


SEARCH_ACCOUNT = 'marvel'
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


bot = InstaFollower()

bot.add_followers(USERNAME, PASSWORD)