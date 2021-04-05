import json
import os

import googlemaps
import wikipedia


class GrandPapyBot:

    gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])

    @staticmethod
    def findAnswer(question):
        if question:
            user_message = GrandPapyBot.filter(question)
            print(user_message)
            if not user_message:
                GrandPapyBot.notUnderstand()
            else:
                if "adresse" in user_message:
                    place = ' '.join(user_message[
                        (user_message.index("adresse"))
                        + 1:len(user_message)])
                    geocode_result = GrandPapyBot.gmaps.geocode(place)
                    print(place)
                    adress = geocode_result[0]['formatted_address']
                    location = geocode_result[0]['geometry']['location']
                    wiki = GrandPapyBot.getWiki(place)
                    print(wiki)
                    return GrandPapyBot.sayAdress(adress, location, wiki)
                elif "merci" in user_message:
                    return GrandPapyBot.sayThanks()
                elif "salut" in user_message:
                    return GrandPapyBot.sayHello()
                else:
                    return GrandPapyBot.notUnderstand()

    @staticmethod
    def sayAdress(adress, location, wiki):
        return {"papy": "Bien sûr mon poussin ! La voici: {}."
                .format(adress), "location": location, "wiki": wiki}

    @staticmethod
    def notUnderstand():
        return {"papy": "désolé je n'ai pas compris"}

    @staticmethod
    def sayHello():
        return {"papy": "Bonjour mon enfant"}

    @staticmethod
    def sayThanks():
        return {"papy": "De rien jeune padawan"}

    @staticmethod
    def getResponse(question):
        return GrandPapyBot.findAnswer(question)

    @staticmethod
    def getWords():
        words = list()
        with open(
            os.path.realpath(
                os.path.dirname(__file__)) +
                '/words_list.json') as f:
            words = json.load(f)
        return words

    @staticmethod
    def filter(question):
        words_to_be_deleted = list()
        question = question.replace("'", " ").split(' ')
        for word in question:
            if word in GrandPapyBot.getWords()['stopwords']:
                words_to_be_deleted.append(word)
        filtered_list = [elt for elt in question
                        if elt not in words_to_be_deleted]
        return filtered_list

    @staticmethod
    def getWiki(subject):
        wikipedia.set_lang("fr")
        try:
            return wikipedia.summary(subject, sentences=2)
        except wikipedia.exceptions.PageError:
            return "Je n'ai jamais été à cet endroit..."
