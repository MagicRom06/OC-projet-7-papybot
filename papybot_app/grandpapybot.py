import json
import os

import googlemaps
import wikipedia


class GrandPapyBot:
    """
    Class used to manage interactions with papy.
    """
    @staticmethod
    def findAnswer(question):
        """
        method used for parsing question and returning answer
        """
        if question:
            user_message = GrandPapyBot.filter(question)
            if not user_message:
                return GrandPapyBot.notUnderstand()
            else:
                if "adresse" in user_message:
                    place = GrandPapyBot.extract(user_message, "adresse")
                    return GrandPapyBot.findAdress(place)
                elif "film" in user_message:
                    movie = GrandPapyBot.extract(user_message, "film")
                    return GrandPapyBot.findMovie(movie)
                elif "livre" in user_message:
                    book = GrandPapyBot.extract(user_message, "livre")
                    return GrandPapyBot.findBook(book)
                elif "merci" in user_message:
                    return GrandPapyBot.sayThanks()
                elif "salut" in user_message:
                    return GrandPapyBot.sayHello()
                else:
                    return GrandPapyBot.notUnderstand()

    @staticmethod
    def extract(question, subject):
        """
        method used to extract key-words from question
        """
        return ' '.join(question[(question.index(subject)) + 1:len(question)])

    @staticmethod
    def findAdress(place):
        """
        answer for adress request
        """
        gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])
        geocode_result = gmaps.geocode(place)
        print(geocode_result)
        adress = geocode_result[0]['formatted_address']
        location = geocode_result[0]['geometry']['location']
        wiki = GrandPapyBot.getWiki(place)
        return {"papy": "Bien sûr mon poussin ! La voici: {}."
                .format(adress), "location": location, "wiki": wiki}

    @staticmethod
    def findMovie(movie):
        """
        answer for movie request
        """
        wiki = GrandPapyBot.getWiki("film " + movie)
        if wiki == "Désolé je ne connais pas":
            return {"papy": wiki}
        else:
            return {"papy": "oui j'adore ce film !", "movie": wiki}

    @staticmethod
    def findBook(book):
        """
        answer for book request
        """
        wiki = GrandPapyBot.getWiki("livre " + book)
        if wiki == "Désolé je ne connais pas":
            return {"papy": wiki}
        else:
            return {"papy": "oui j'adore ce livre !", "book": wiki}

    @staticmethod
    def notUnderstand():
        """
        answer when papy doesn't understand
        """
        return {"papy": "désolé je n'ai pas compris"}

    @staticmethod
    def sayHello():
        """
        papy says hello !
        """
        return {"papy": "Bonjour mon enfant"}

    @staticmethod
    def sayThanks():
        """
        papy says thanks
        """
        return {"papy": "De rien jeune padawan"}

    @staticmethod
    def getResponse(question):
        """
        method used in index view to forward the question to papy
        in order to get an answer
        """
        return GrandPapyBot.findAnswer(question)

    @staticmethod
    def getWords():
        """
        used to get all useless words in json format
        """
        words = list()
        with open(
            os.path.realpath(
                os.path.dirname(__file__)) +
                '/words_list.json') as f:
            words = json.load(f)
        return words

    @staticmethod
    def filter(question):
        """
        used for parsing the question
        """
        words_to_be_deleted = list()
        question = question.replace("'", " ").split(' ')
        for word in question:
            if word in GrandPapyBot.getWords()['stopwords']:
                words_to_be_deleted.append(word)
        filtered_list = [elt for elt in question if
                         elt not in words_to_be_deleted]
        return filtered_list

    @staticmethod
    def getWiki(subject):
        """
        used for wikipedia research
        """
        wikipedia.set_lang("fr")
        try:
            return wikipedia.summary(subject, sentences=2)
        except wikipedia.exceptions.PageError:
            return "Désolé je ne connais pas"
