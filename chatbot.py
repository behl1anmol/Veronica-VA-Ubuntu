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
