import discord
import random
import string

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


PASSWORD = "1234"  


logged_users = {}


EMOJIS = ["😀", "😎", "😂", "😍", "🤔", "🥶", "😡", "👻", "🐱", "🐶", "🍕", "⚡", "🔥", "🎉", "🌍"]

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content.startswith('$login'):
        parts = message.content.split()
        if len(parts) == 2 and parts[1] == PASSWORD:
            logged_users[message.author.id] = True
            await message.channel.send(" Login exitoso!")
        else:
            await message.channel.send(" Contraseña incorrecta.")
        return

    if message.author.id not in logged_users:
        await message.channel.send(" Debes hacer login con `$login <contraseña>`")
        return

   
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$genpass'):
        
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        await message.channel.send(f" Tu contraseña generada: `{password}`")
    elif message.content.startswith('$emoji'):
        
        emoji = random.choice(EMOJIS)
        await message.channel.send(emoji)
    else:
        await message.channel.send(message.content)

client.run("MTQxNzY1ODU3NDE5MjExNTg4NA.GYYwB3.mspS3muH1bqvWxlwITmDKA7pWjALOIOWGveQrg")