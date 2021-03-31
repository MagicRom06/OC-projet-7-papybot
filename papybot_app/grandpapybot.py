import json
import os


class GrandPapyBot:
	
	@staticmethod
	def findAnswer(question):
		if question:
			user_message = GrandPapyBot.filter(question)
			if not user_message:
				GrandPapyBot.notUnderstand()
			else:
				if "adresse" in user_message and "OpenClassrooms" in user_message:
					return GrandPapyBot.sayOcAdress()
				elif "merci" in user_message:
					return GrandPapyBot.sayThanks()
				elif "salut" in user_message:
					return GrandPapyBot.sayHello()
				else:
					return GrandPapyBot.notUnderstand()

	@staticmethod
	def sayOcAdress():
		return "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris."

	@staticmethod
	def notUnderstand():
		return "désolé je n'ai pas compris"

	@staticmethod
	def sayHello():
		return "Bonjour mon enfant"

	@staticmethod
	def sayThanks():
		return "De rien jeune padawan"

	@staticmethod
	def getResponse(question):
		return GrandPapyBot.findAnswer(question)

	@staticmethod
	def getWords():
		words = list()
		with open(os.path.realpath(os.path.dirname(__file__)) + '/words_list.json') as f:
			words = json.load(f)
		return words

	@staticmethod
	def filter(question):
		words_to_be_deleted = list()
		question = question.replace("'", " ").split(' ')
		for word in question:
			if word in GrandPapyBot.getWords()['stopwords']:
				words_to_be_deleted.append(word)
		filtered_list = [elt for elt in question if elt not in words_to_be_deleted]
		return filtered_list
