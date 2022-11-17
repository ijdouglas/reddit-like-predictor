"""
Define the class `RedditScrape` class that stores attributes to define a subreddit name and date range.
Included methods will use these attributes to scrape either comments or posts in said sub for dates.
Return pandas data frame of results and save to desired location.

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
  # To define another method (as in the __init__ method as well), the first
  # argument is self so that within the method the attributes of the instance
  # are accessible to the method
  
  # Here's the method to scrape comments, specifically suing pushshift api
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

  # A method to save the desired data (comments, or later, posts)
  def save(self, attribute_name, filename):
    """
    :type attribute_name: str
    :type filename: str
    """
    x = getattr(self, attribute_name)
    pd.DataFrame(x).to_csv(repr(filename), # basically r'attribute_name'
                           encoding='utf-8-sig', index = False)
# note that attributes can be edited AFTER inititialization directly
# instance = RedditScrape('cat', dt.datetime(1111, 11, 11), dt.datetime(1112, 11, 11))
# instance.subreddit_name = 'dog' # change subreddit name to dog
# And this will not impact anything until scrape_comments() is run, after which point changes
# to the subreddit_name attribute will mismatch comments attribute until scrape_comments is run again
