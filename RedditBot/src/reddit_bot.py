import praw
import config
from sys import argv


class RedditBot():

    def __init__(self):
        self.reddit = self.bot_login()

    def bot_login(self):
        r = praw.Reddit(username = config.username, password = config.password, client_id = config.client_id,
                        client_secret = config.client_secret,
                        user_agent = '{}\'s test post search v0.1.'.format(config.username))
        return r

    def check_post_titles(self, subreddit_name, number_of_posts, search_query):
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=number_of_posts):
            if search_query in submission.title:
                print submission.title


def main(args):
    r = RedditBot()
    r.check_post_titles('buildapcsales', 1000, 'PSU')

main(argv)

