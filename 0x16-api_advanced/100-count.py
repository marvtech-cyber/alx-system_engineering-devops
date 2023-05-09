s module defines the number_of_subscribers function.
"""

import praw

def count_words(subreddit, word_list, hot_list=None, count_dict=None):
    # Create PRAW instance
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    # Create hot_list and count_dict if not provided
    if hot_list is None:
        hot_list = []
    if count_dict is None:
        count_dict = {}

    # Get hot articles from subreddit
    subreddit_obj = reddit.subreddit(subreddit)
    hot_articles = subreddit_obj.hot(limit=100)

    # Iterate through hot articles and add titles to hot_list
    for article in hot_articles:
        hot_list.append(article.title)

    # Count occurrences of each word in hot_list
    for word in word_list:
        count = sum(1 for title in hot_list if word.lower() in title.lower().split())
        if count > 0:
            # Add word to count_dict
            if word.lower() not in count_dict:
                count_dict[word.lower()] = count
            else:
                count_dict[word.lower()] += count

    # If there are more hot articles, recursively call function with updated hot_list and count_dict
    if subreddit_obj._path.endswith('/hot'):
        next_subreddit = subreddit_obj._path[:-4]
    else:
        next_subreddit = subreddit_obj._path + '/hot'
    try:
        return count_words(next_subreddit, word_list, hot_list=hot_list, count_dict=count_dict)
    except:
        pass

    # Sort count_dict by count and then alphabetically
    sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_count:
        print(word + ':', count)
