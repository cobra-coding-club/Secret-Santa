from interactions import listen, Client, Intents

GUILD_ID = 'Id du serveur de test'
TOKEN = 'Token du bot'
BOT = Client(intents=Intents.DEFAULT, debug_scope=GUILD_ID)


@listen()
async def on_ready():
    print("Le bot est prêt !")


BOT.start(TOKEN)
