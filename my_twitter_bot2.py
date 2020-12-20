import tweepy
import time
import wget
import urllib
import bs4 as bs
import TwitterChatBot
import Train

print('This is a twitter bot! KEK \n', flush=True)

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id



def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'a')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def read_image_id():
    f = open(file_title, 'r')
    data = f.read()
    f.close()
    return data
def store_image_id():
    f = open(file_title, 'a')
    for eachString in search_twitter_and_recieve_urls():
        f.write(eachString)
    f.close()   

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

search_words = ['ahri', 'ahri league', 'ahri hentai', 'ahri lol',
                'ahri champion league', '#ahri', '#ahrilol']
date_since = "2020-12-16"

def search_twitter_and_recieve_urls():
#    tweets = tweepy.Cursor(api.search,
 #             q=search_words,
  #            lang="en",
   #           since=date_since).items(15)
    #length = len(tweets)
    # Iterate and print tweets

    log = []
    for eachQuery in search_words:
        print(
            '''
            --------------------
          SEARCHING FOR IMAGES IN {}
            --------------------
            '''.format(eachQuery.upper()))
        media_files = []
        ahri_images = api.search(q=eachQuery,result_type='mixed',count=30)
        x = len(ahri_images)
        i = 0
        check_images = 0
        for tweet in range(0, x-1):
            tweets_image = ahri_images[i].entities.get('media', [])

            if (len(tweets_image) > 0):
                if tweets_image[0]['media_url'] in log:
                    #print("duplicant")
                    break
                elif tweets_image[0]['media_url'] in read_image_id():
                    #print("duplicant")
                    break
                else:
                    media_files.append(tweets_image[0]['media_url'])
                    log.append(tweets_image[0]['media_url'])
                    check_images += 1

            i += 1
        if check_images == 0:
                print('No images were found PepeHands')            
        print('URLs:\n' + str(media_files) +'\n')
        
        for media_file in media_files:
            print("Downloading file...")
            wget.download(media_file)
            print("Download file successfully! widepeepoHappy\n")        

    return log

file_title = 'imagelog.txt'


#def download_images():
#    media_files = search_twitter_and_recieve_urls()
 #   for media_file in media_files:
  #      print("Downloading file...")
   #     wget.download(media_file)
    #    print("Download file successfully! widepeepoHappy\n")

def reply_to_mentions():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        try:
            print(str(mention.id) + '-' + mention.full_text)
            store_last_seen_id(last_seen_id, FILE_NAME)
            if '#pepega' in mention.full_text.lower():
                print('found #pepega!', flush=True)
                print('responding back...\n', flush=True)
                api.update_status('@' + mention.user.screen_name +
                                  " You're a pepega!", mention.id)
            else:
                break
                
        except tweepy.TweepError as error:
            if error.api_code == 187:
                # Do something special
                print('[FAILED]Duplicate message\n')
            else:
                raise error   

def reply_to_tweets():

    replyQuery = ['league of legends']
    tweet_search = api.search(q=replyQuery,lang='en',result_type='recent',count=20)
    content = TwitterChatBot.chat_and_get_response(self=0, text_input=tweet_search[0].text)
    if "RT" in tweet_search[0].text:
        print("Didn't reply...")
    else:
        api.update_status('@' + tweet_search[0].user.screen_name + ' ' + str(content), tweet_search[0].id)
    f = open('read_data.txt', 'w', encoding='utf-8')
    f.write(str(tweet_search[0].text) + '\n')
    f.write(str(content))
    f.close()
        
while True:
    #reply_to_mentions()
    read_image_id()
    #search_twitter_and_recieve_urls()
    store_image_id()
    #reply_to_tweets()
    #download_images()   
    time.sleep(15)


