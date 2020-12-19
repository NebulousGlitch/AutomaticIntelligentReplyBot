from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import Train

def update_database():
    f = open('read_data.txt','r')
    custom = f.read()
    f.close()
    return custom  
        
def chat_and_get_response(self, text_input):
    chatbot = ChatBot('Ron Obvious')

        # Create a new trainer for the chatbot
    #trainer = ChatterBotCorpusTrainer(chatbot)
    trainer = ListTrainer(chatbot)
        # Train the chatbot based on the english corpus
##    trainer.train(
##        update_database()
##        )

        # Get a response to an input statement

    while True:
        speak = text_input
        x = chatbot.get_response(speak)
        print(x)
        return x

    Train.train_database()

