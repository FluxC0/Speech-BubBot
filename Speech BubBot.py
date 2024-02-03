import discord 
import random
from discord.ext import commands

TARGETID = input("what userID should i reply to with speech bubbles?")
token = input("what is the token of the bot?")

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author.id == int(TARGETID):
      # Add responses in here. make sure you make the gif links strings and add commas to the end to define it as a list.
      responses = ['https://tenor.com/view/purble-place-purble-purple-speech-bubble-chungus-gif-26240224',
      'https://tenor.com/view/spongefly-speech-bubble-gif-26113306',
      'https://tenor.com/view/lego-island-brickster-discord-speech-bubble-gif-25986049',
      "https://tenor.com/view/boy-kisser-boykisser-boy-kisser-type-type-typing-gif-4348094406361571449",
      'https://tenor.com/view/speech-bubble-png-speech-bubble-gif-26086226',
      'https://tenor.com/view/among-us-sus-discord-speech-bubble-among-us-discord-speech-bubble-ok-man-gif-7378430653913901797',
      'https://tenor.com/view/mod-discord-mod-nerd-glasses-speech-bubble-gif-27462011',
      'https://tenor.com/view/chicken-spitting-bars-gif-14236938144080559653',
      'https://tenor.com/view/young-sheldon-speech-bubble-discord-sheldon-cooper-sheldon-gif-5616514344261205807',
      'https://tenor.com/view/speechbubble-speech-bubble-please-meme-gif-25693113',
      'https://tenor.com/view/speech-bubble-discord-who-cares-handsome-squidward-squidward-gif-25418980',
      'https://tenor.com/view/quirky-speech-bubble-gif-738969972579857891',
      'https://tenor.com/view/garfield-speech-bubble-garfield-wide-wide-garfield-garfwide-explaining-garfield-gif-17863144809496135774',
      'https://tenor.com/view/nerd-nerd-emoji-meme-speech-bubble-bubble-gif-25115885',
      'https://tenor.com/view/goobysart-speech-bubble-boykisser-mauzymice-anti-furry-gif-6769248524556738224',
      "https://tenor.com/view/mauzymice-cat-gif-27575020",
      'https://tenor.com/view/speechbubble-discord-i-am-inside-your-gif-25941808'
      
      
      
                  
                  
                  
                  
        
                  
                  
                  
                  
                  
                  
        ]
      response = random.choice(responses)
      await message.channel.send(response)
# ADD TOKEN HERE! BOT WILL NOT FUNCTION WITHOUT A BOT TOKEN!!!!  
client.run(token)
