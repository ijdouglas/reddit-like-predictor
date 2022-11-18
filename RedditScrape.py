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
                                 filter=['author', 'selftext', 'created_utc', 'subreddit', 'body',
                                         'id','parent_id', 'score', 'author_flair_css_class',
                                         'author_flair_text', 'metadata'],
                                 after = self.start_epoch, 
                                 before = self.end_epoch)
    self.comments = [x for x in result] # extract into list, save as attribute
    
  def as_data_frame(self, attribute_name):
    """
    After comments or posts have been scraped using scrape_comments or scrape_posts,
    they can be returned as a data frame
    """
    #import pandas as pd # already done in __init__
    return(pd.DataFrame(getattr(self, attribute_name)))
  
  # A method to save the desired data (comments, or later, posts)
  def save(self, attribute_name, filename):
    """
    :type attribute_name: str
    :type filename: str
    """
    x = getattr(self, attribute_name)
    pd.DataFrame(x).to_csv(repr(filename), # basically r'filename'
                           encoding='utf-8-sig', index = False)
