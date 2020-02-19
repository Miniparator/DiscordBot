import discord

class MyBot(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Eingeloggt")
        
    #Wenn Nachricht empfangen wird
    async def on_message(self, message):
        if message.author == bot.user:
            return
        
        if str(message.channel) == "bottest1":
            await message.channel.send("Auch hi")
    
file = open("key.txt")
file_content = file.read()
file.close()

key = file_content.rstrip()

print(key)
    
bot = MyBot()
bot.run(key)
