import json
import os

import googlemaps
import wikipedia


class GrandPapyBot:
    """
    Class used to manage interactions with papy.
    """

    # load google map client
    gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])

    @staticmethod
    def findAnswer(question):
        """
        method used for parsing question and returning answer
        """
        if question:
            # deleting useless words that are in words_list.json
            user_message = GrandPapyBot.filter(question)
            if not user_message:
                GrandPapyBot.notUnderstand()
            else:
                # if the question concerns an adress:
                # - display adresse
                # - google map location
                # - wiki information for the research
                if "adresse" in user_message:
                    place = ' '.join(user_message[
                        (user_message.index("adresse"))
                        + 1:len(user_message)])
                    geocode_result = GrandPapyBot.gmaps.geocode(place)
                    adress = geocode_result[0]['formatted_address']
                    location = geocode_result[0]['geometry']['location']
                    wiki = GrandPapyBot.getWiki(place)
                    return GrandPapyBot.sayAdress(adress, location, wiki)
                # if the question concerns a movie:
                # - display wiki information regarding the movie
                elif "film" in user_message:
                    movie = ' '.join(
                        user_message[(
                            user_message.index("film")):len(user_message)])
                    wiki = GrandPapyBot.getWiki(movie)
                    return GrandPapyBot.findMovie(wiki)
                # if the question concerns a book:
                # - display wiki information regarding the book
                elif "livre" in user_message:
                    book = ' '.join(
                        user_message[(
                            user_message.index("livre")):len(user_message)])
                    wiki = GrandPapyBot.getWiki(book)
                    return GrandPapyBot.findBook(wiki)
                elif "merci" in user_message:
                    return GrandPapyBot.sayThanks()
                elif "salut" in user_message:
                    return GrandPapyBot.sayHello()
                else:
                    return GrandPapyBot.notUnderstand()

    @staticmethod
    def sayAdress(adress, location, wiki):
        """
        answer for adress request
        """
        return {"papy": "Bien sûr mon poussin ! La voici: {}."
                .format(adress), "location": location, "wiki": wiki}

    @staticmethod
    def findMovie(wiki):
        """
        answer for movie request
        """
        if wiki == "Désolé je ne connais pas":
            return {"papy": wiki}
        else:
            return {"papy": "oui j'adore ce film !", "movie": wiki}

    @staticmethod
    def findBook(wiki):
        """
        answer for book request
        """
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
