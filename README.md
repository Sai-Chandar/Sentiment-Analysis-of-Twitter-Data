# Sentiment-Analysis-of-Twitter-Data
Sentiment Analysis of Twitter Data is a script that returns a sentiment value, from -1 to +1, for tweets from a hashtag or comments to a tweet.

## Libraries

You'll need python 3 with pip installed.

`pip install nltk`

`pip install tweepy`

`pip install pandas`

You'll need to download vader lexicon. To do that, open python console and

`import nltk`

`nltk.download('vader_lexicon')`

---
## Usage

To analyze a hashtag use -ht and mention number of tweets by -n.

`python main.py -ht <hashtag> -n <number of tweets>`

To analyze comments to a recent tweet from your business

`python main.py -u <twitter user name> -n <number of tweets>`

---
## Sentiment Range

Positive Sentiment: score >= 0.05

Neutral Sentiment: -0.05 < score < 0.05

Negative Sentiment: score <= -0.05

For more information refer [vader_lexicon](https://github.com/cjhutto/vaderSentiment).

---
## Contributors

- Saichandar Reddy Naini <n.saichander@gmail.com>

---

## License and copyright

 © Saichandar Reddy Naini

 Licensed under [MIT License](LICENSE).
