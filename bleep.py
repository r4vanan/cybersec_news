#!/usr/bin/python
import feedparser
import time

# RSS feed URL
url = 'https://www.bleepingcomputer.com/feed/'

# Get the current time
current_time = time.time()

# Get the start and end times for today
start_of_today = time.mktime(time.localtime(current_time - (24 * 60 * 60)))
end_of_today = time.mktime(time.localtime(current_time))

# Parse the RSS feed
feed = feedparser.parse(url)

# Iterate through each article in the feed
for article in feed.entries:
    # Get the published time of the article
    published_time = time.mktime(article.published_parsed)

    # Check if the article was published today
    if start_of_today <= published_time <= end_of_today:
        print('Title:', article.title)
        print('Link:', article.link)
        print('Description:', article.summary)
        print('Published on:', time.strftime('%Y-%m-%d %H:%M:%S', article.published_parsed))
        print()

