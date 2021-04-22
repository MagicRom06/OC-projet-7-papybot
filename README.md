# OC-p7-Créez GrandPy Bot, le papy-robot

## Contexte
Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

## Cahier des charges
### Fonctionnalités
Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
Vous utiliserez l'API de Google Maps et celle de Media Wiki.
Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !

### Parcours utilisateur
L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :

header : logo et phrase d'accroche
zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.
footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez
L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"

## Prérequis
Le programme utilise python3 et le framework Flask.

## Lancement du programme
git clone https://github.com/MagicRom06/OC-projet-7-papybot.git<br>
Pour activer l'environnement virtuel une fois dans le repertoire, executer la commande pipenv shell<br>
exécuter la commande "pipenv install -r requirements.txt"<br>
Une fois dans le répertoire principal, exécuter python run.py

## Exemples
Voici quelques exemples de question à poser à PapyBot:
- "Est-ce que tu connais l'adresse d'Openclassrooms ?"
- "Est-ce que tu connais le film la ligne rouge ? "
- "Est-ce que tu connais le livre germinal ?"<br>

ATTENTION: Pour que papybot comprenne la question, il faut s'assurer que les mots "adresse", "film" ou "livre" (selon la recherche) soientt devant le sujet recherché.
