from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import sys
import tweepy
import time
import re

## CHAMPION TRAIN
## FOR TRAINING CONVOS RELATED TO SPECIFIC CHAMPIONS

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

search_words = "Aatrox,Ahri,Akali,Alistar,Amumu,Anivia,Annie,Aphelios,Ashe,Aurelion Sol,Azir,Bard,Blitzcrank,Brand,Braum,Caitlyn,Camille,Cassiopeia,Cho'Gath,Corki,Darius,Diana,Dr. Mundo,Draven,Ekko,Elise,Evelynn,Ezreal,Fiddlesticks,Fiora,Fizz,Galio,Gangplank,Garen,Gnar,Gragas,Graves,Hecarim,Heimerdinger,Illaoi,Irelia,Ivern,Janna,Jarvan IV,Jax,Jayce,Jhin,Jinx,Kai'Sa,Kalista,Karma,Karthus,Kassadin,Katarina,Kayle,Kayn,Kennen,Kha'Zix,Kindred,Kled,Kog'Maw,LeBlanc,Lee Sin,Leona,Lillia,Lissandra,Lucian,Lulu,Lux,Malphite,Malzahar,Maokai,Master Yi,Miss Fortune,Mordekaiser,Morgana,Nami,Nasus,Nautilus,Neeko,Nidalee,Nocturne,Nunu and Willump,Olaf,Orianna,Ornn,Pantheon,Poppy,Pyke,Qiyana,Quinn,Rakan,Rammus,Rek'Sai,Rell,Renekton,Rengar,Riven,Rumble,Ryze,Samira,Sejuani,Senna,Seraphine,Sett,Shaco,Shen,Shyvana,Singed,Sion,Sivir,Skarner,Sona,Soraka,Swain,Sylas,Syndra,Tahm Kench,Taliyah,Talon,Taric,Teemo,Thresh,Tristana,Trundle,Tryndamere,Twisted Fate,Twitch,Udyr,Urgot,Varus,Vayne,Veigar,Vel'Koz,Vi,Viktor,Vladimir,Volibear,Warwick,Wukong,Xayah,Xerath,Xin Zhao,Yasuo,Yone,Yorick,Yuumi,Zac,Zed,Ziggs,Zilean,Zoe,Zyra"

Query = search_words.split(",")

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def find_twitter_conversation():
    list_of_conversations = []
    f = open('stored_tweets.txt','r',encoding='utf-8')
    stored_tweets = f.read()
    for eachQuery in Query:
        thread_links = api.search(q=eachQuery+' League of Legends',lang='en',
                                  result_type='recent',count=50,
                                  tweet_mode='extended')
        for eachLink in thread_links:
            try:
                x = eachLink.retweeted_status
            except:
                if eachLink.full_text in list_of_conversations:
                    break
                else:
                    text = eachLink.full_text
                    result = re.sub(r"http\S+", "", text) #taken from stackexchange
                    even_cleaner = " ".join(filter(
                        lambda x:x[0]!='@', result.split())) #taken from stackexchange
                    if even_cleaner in stored_tweets:
                        break
                    else:
                        list_of_conversations.append(even_cleaner)
        print('Found tweets for ' + eachQuery)
        time.sleep(5)
    f.close()
    f = open('stored_tweets.txt','a',encoding='utf-8')
    for eachString in list_of_conversations:
        f.write(eachString + ' ')         
    return list_of_conversations

def train_database():
    chatbot = ChatBot('Ron Obvious')

    trainer = ListTrainer(chatbot)

    trainer.train(
        find_twitter_conversation()
        )
    print('\nsuccessfully trained!\n')

while True:
    train_database()
    time.sleep(1800)
