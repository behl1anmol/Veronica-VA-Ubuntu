# from chatterbot import ChatBot 
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from settings import veronica_notify
# from AudioIO import speak

# bot=ChatBot(
#     "Veronica",
# )

# bot.read_only=True
# bot.set_trainer(ChatterBotCorpusTrainer)


# def train_veronica():
# 	speak('reintializing training database')
# 	veronica_notify("Reintializing training database")
# 	bot.train(
# 	     "chatterbot.corpus.english"
# 	)

# train_veronica()

# while True:
# 	try:
# 		usr_input=input()
# 		#print("inside chatbot")		
# 		resp=bot.get_response(usr_input)
# 		veronica_notify(resp)
# 		print(resp)
# 		speak(resp)
# 	except(KeyboardInterrput,EOFError,SystemExit):
# 		break

from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

bot=ChatBot(
    "Veronica",
)

bot.read_only=True
bot.set_trainer(ChatterBotCorpusTrainer)


bot.train(
    "chatterbot.corpus.english"
)

while True:
	try:
		usr_input=input()
		resp=bot.get_response(usr_input)
		print(resp)
	except(KeyboardInterrput,EOFError,SystemExit):
		break	

