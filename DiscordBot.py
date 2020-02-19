import discord

class MyBot(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Eingeloggt")
        
    #Wenn Nachricht empfangen wird
    async def on_message(self, message):
        message_content = message.content

        #Wenn die Nachricht vom Bot selber ist
        if message.author == bot.user:
            return
        
        if str(message.channel) == "bottest1":
            if message_content[0] == "/":
                command = message_content.split("/")[1].split(" ")
                answer = ""
                if command[0] == "solve":
                    answer = eval(command[1]) 
                
                await message.channel.send(answer)

   
#Token aud Datei auslesen die Nicht auf Github hochgeladen wird 
file = open("key.txt")
file_content = file.read()
file.close()

#Das \n entfernen
key = file_content.rstrip()

#Bot starten
bot = MyBot()
bot.run(key)
