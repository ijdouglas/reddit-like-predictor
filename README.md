# Leverage computer vision to understand likeability in posts
Scrape reddit posts or comments, analyze images posted. Build a model and predict the number of likes for a new image posted to the subreddit.

```
Note: due to how the PushShiftApi works to scrape data, the apparent scores of posts can 
change as posts are continually voted on. So to train the model in a reproducible way, 
scraping the data into the dataset should occur at the same time as preprocessing and 
training, as the model will be slightly different every time the data is scraped.
```

Reddit is a unique platform in that users *belong* to subreddits, and may be recognized by other users who frequent those subreddits. To that extent, likes are not likely to be based solely on likeability of images or text posted, but also aspects of the ooster, including but not limited to their post history, their reputation in the subreddit, even their username.

For this reason, and others explained below, I test r/cat and r/dog because these pictures are posted for similar reasons across users and with very limited narrative context: the pictures are posted because they are pleasing to look at (so, mainly for aesthetic reasons).

As a result, two questions arise:

1. Considering that aesthetics are contained in the picture's **visual properties**, can we use computer vision to predict a behavioral outcome related to those visual properties, namely other user's upvoting behavior in response to the image, theoretically mediated by the visual pleasurability contained in the image's aesthetics.

2. Since r/cat and r/dog have similar purpose (to provide pleasing pictures of either animal), can a general model predict upvotes for both (trained on both or trained on one and tested on the other)?
    - Such a model *may* imply that general aesthetic principles within the domain of say, domesticated mammals governs perception of visual stimuli (i.e., images of cats or dogs)

