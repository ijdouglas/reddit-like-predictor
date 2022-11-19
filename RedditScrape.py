"""
Define the `RedditScrape` class that stores attributes to define a subreddit name and date range.
Included methods use these attributes to scrape either comments or posts in given subreddit within date range.
The result of the above is to return a pandas data frame of results and save to desired location,
using the method as_data_frame(self, 'comments') or as_data_frame(self, 'posts'). Other methods can save
the data frame directly from the scraped results, and of course conduct scraping.

This script does not create any instances, rather just defines the class itself!
"""

# Modules needed to create instances of the class defined in this script:
#import os
#import pandas as pd
#import praw
#from psaw import PushshiftAPI
#import datetime as dt
#from datetime import datetime
#from time import sleep

class RedditScrape:
  def __init__(self, subreddit_name, start_epoch, end_epoch):
    """
    :type subreddit_name: str
    :type start_epoch: datetime
    :type end_epoch: datetime
    """
    import pandas as pd
    from psaw import PushshiftAPI
    # Define attributes (also called instance variables)
    self.api = PushshiftAPI()
    self.subreddit_name = subreddit_name
    self.start_epoch = start_epoch
    self.end_epoch = end_epoch

  
  # Here's the method to scrape comments, specifically using pushshift api
  def scrape_comments(self):
    """
    Scrape comments, create self.comments attribute
    """
    result = self.api.search_comments(subreddit=self.subreddit_name,
                                 filter=['subreddit', 'id', 'full_link', 'score', 
                                         'title', 'is_video', 
                                         'is_self' # if is_self, the post was removed
                                        'media_embed'], # if media_embed is a dict, it's likely a video link to youtube or something],
                                 after = self.start_epoch, 
                                 before = self.end_epoch)
    self.comments = pd.DataFrame([x.d_ for x in result]) 
    
  def scrape_posts(self):
    """
    Scrape submissions, calling them `posts` for short, that are posted to boards directly
    """
    result = self.api.search_submissions(subreddit=self.subreddit_name,
                                 filter=['subreddit', 'id', 'full_link', 'score', 
                                         'title', 'is_video', 
                                         'is_self' # if is_self, the post was removed
                                        'media_embed'],
                                 after = self.start_epoch, 
                                 before = self.end_epoch)
    self.posts = pd.DataFrame([x.d_ for x in result]) # extract into list, save as attribute
  
  # A method to save the desired data (comments, or submissions/posts)
  # The purpose of this method is simply to facilitate saving with the proper encoding
  def save(self, attribute_name, filename):
    """
    :type attribute_name: str
    :type filename: str
    """
    x = getattr(self, attribute_name)
    x.to_csv(filename, encoding='utf-8-sig', index = False)
