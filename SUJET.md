# SECRET SANTA

## Les outils

Pour ce projet, nous aurons besoin de quelques outils:

- Visual Studio Code (ou un autre éditeur de texte): Pour écrire notre incroyable code
- Python 3: Pour lancer et faire tourner le bot
- La librairie discord-py-interactions: La documentation nous sera utile pour trouver comment implémenter les
  fonctionalités dont nous avons besoin. [Documentation](https://interactions-py.github.io/interactions.py/)

Tout est déjà installé alors pas de soucis à se faire !

## Prise en main

L'entrée principale de notre programme est le fichier `main.py`. C'est ici que nous allons écrire notre code.
Tu devrais y trouver plusieurs lignes intéressantes.
Tout d'abord des lignes à remplir

```python
GUILD_ID = 'Id du serveur de test'
TOKEN = 'Token du bot'
```

Tu trouveras l'id de ton serveur en activant les options développeurs dans les paramètres de Discord.
Pour le token, il faut aller dans l'onglet "Bot" de ton application sur le site des développeurs Discord, comme expliqué
dans la page précédente.

Ensuite, tu trouveras une ligne qui ressemble à ça:

```python
BOT = Client(intents=Intents.DEFAULT, debug_scope=GUILD_ID)
```

Ici on crée notre bot en lui donnant le nom `BOT`. On lui donne aussi des paramètres, comme les intents et le scope de
débug. Ces paramètres nous permettent de définir ce que le bot peut faire et ou il peut le faire.

La dernière ligne, nous permet de lancer le bot, il est impératif de la laisser à la fin du fichier. Sinon notre bot se
lancera sans les informations nécessaires.

```python
BOT.start(TOKEN)
```

Enfin un Elfe Sénior t'as laissé un petit exemple de code pour t'aider à démarrer.

```python
@listen
async def on_ready():
    print("Le bot est prêt !")
```

Cette fonction est appelée quand le bot est prêt à être utilisé. Tu peux y mettre tout ce que tu veux, comme par exemple
un message pour dire que le bot est prêt.

## Ta première commande

Pour créer une commande, il faut utiliser le décorateur `@slash_command()` au dessus d'une fonction. Cette fonction sera
appelée quand la commande sera utilisée. Le décorateur prend quelques paramètres pour définir la commande, tu peux
retrouver toutes les informations à ce sujet sur [la page de
la documentation](https://interactions-py.github.io/interactions.py/Guides/03%20Creating%20Commands/).

Commence par créer une commnande appelée `noyeux_joel` qui envoie un message de joyeux noël en mentionnant l'utilisateur
qui l'a appelé. Libre à toi de lui donner une description pour que les amis de Xavier comprennent ce qu'elle fait.
Cette commande doit aussi afficher un message dans le terminal de Xavier pour lui dire que la commande a été appelée, à
toi de voir ce que tu veux passer comme message à notre Xavier national.

## Passons aux choses sérieuses

Finis de jouer, Xavier a besoin de son bot au plus tôt pour pouvoir organiser son Secret Santa. Commence par créer une
commande `ajouter_participant` qui prend en paramètre le nom d'un participant. Cette commande doit
renvoyer un message en disant que le participant a bien été ajouté. Le bot doit aussi sauvegarder les noms de tous les
participants dans une liste pour pouvoir les utiliser plus tard.

## Le budget, c'est important

Maintenant que nous avons nos participants, il faut leur donner un budget. Crée une commande `definir_budget` qui prend
en paramètre un nombre. Ce nombre sera le budget de chaque participant. Cette commande doit renvoyer un message en
disant que le budget a bien été défini. Le bot doit aussi sauvegarder le budget dans une variable pour pouvoir
l'utiliser plus tard.

## C'est parti !

Maintenant que nous avons nos participants et notre budget, il faut lancer le Secret Santa. Crée une
commande `lancer_secret_santa` qui ne prend pas de paramètre. Cette commande doit renvoyer un message en disant que le
Secret Santa a bien été lancé. Le bot doit envoyer un message en associant chaque participant à un autre participant.
Pour ne pas spoiler tout le monde de qui est son père noël, le message doit mettre chaque nom de père noël en spoiler.

```
- Le père noël de Xavier est : ||Père Noël||.
```

Xavier ne peut pas demander à ses amis de le rejoindre sur son serveur de test pour ne pas gâcher la surprise, mais si
tu veux tu peux aussi remplacer les noms par des vrais utilisateurs de ton serveur de test et leur envoyer un message
avec le nom de la personne à qui ils doivent offrir un cadeau.

## Des super cadeaux

Quand un participant à récupéré le cadeau qu'il doit offrir, il faut qu'il puisse le dire au bot pour qu'on sache quand
chaque membre a récupéré son cadeau. Crée une commande `cadeau_recupere` qui prend en paramètre le nom du participant
qui a récupéré son cadeau, le nom de son cadeau, le prix du cadeau et un message pour le destinataire du cadeau. Il faut
enregistrer ces informations pour pouvoir les utiliser plus tard. Si le prix du cadeau est trop éloigné du budget, le
bot doit renvoyer un message en disant que le cadeau n'est pas dans le budget global et ne doit pas accepté le cadeau.

## Le grand jour

Une fois que le dernier participant a récupéré son cadeau avec la commande, il faut les distribuer ! Crée une
commande `distribuer_cadeaux` qui ne prend pas de paramètre. Cette commande doit renvoyer un message en disant que les
cadeaux ont bien été distribués. Le bot doit envoyer un message en public et/ou en privé à chaque participant en lui
révélant qui est son père noël et en lui donnant le cadeau ainsi que le message associé.

## Les stats c'est cool

Xavier est un grand féru de statistiques, il aimerait bien avoir des statistiques sur son Secret Santa. Crée une
commande `statistiques` qui ne prend pas de paramètre. Cette commande doit renvoyer un message avec les statistiques de
l'événement, qui a été le dernier à récupérer son cadeau, qui a été le premier, qui a eu le cadeau le plus cher, la
moyenne des prix et d'autres trucs du genre. Libre à toi de choisir les statistiques que tu veux afficher.