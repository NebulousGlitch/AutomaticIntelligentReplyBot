from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import tweepy
import time

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

Query = ['league of legends', 'lol', 'ahri', 'lol champion']

def find_twitter_conversation():
    for eachQuery in Query:
        thread_links = api.search(q=eachQuery,result_type='recent',count=10)
        for eachLink in thread_links:
            try:
                print(thread_links[0].quoted_status.text)
            except:
                print("no quote")
                
##def write_to_database():
##    f = open('read_data.txt', 'a+')

def update_database():
    f = open('read_data.txt','r')
    custom = f.read()
    f.close()
    return custom

def train_database():
    chatbot = ChatBot('Ron Obvious')

    trainer = ListTrainer(chatbot)

    trainer.train(
        update_database()
        )

find_twitter_conversation()


