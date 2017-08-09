*** Settings ***
Documentation  Keywords for Reddit bot automation
Library        libraries.reddit_bot  WITH NAME Bot

*** Variables ***
SUBREDDIT_NAME    "buildapcsales"
QUERY_NUMBER    50
SEARCH_TERM    "GPU"

*** Keywords ***
Test
    Log  "Running the first automation test case"
    Bot.Check Post Titles  ${SUB