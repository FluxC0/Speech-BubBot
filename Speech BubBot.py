import discord
import random
from discord.ext import commands
import tkinter as tk

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

def start_bot():
    target_id = TARGETIDtxt.get()
    bot_token = tokentxt.get()

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author.id == int(target_id):
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
                # Add more responses here
            ]
        response = random.choice(responses)
        await message.channel.send(response)

    client.run(bot_token)

root = tk.Tk()

TARGETIDtxt = tk.Entry(root, bg="#353839",fg="#5865F2")
tokentxt = tk.Entry(root, bg="#353839",fg="#5865F2")
labela = tk.Label(root, text="What is the ID you intend to Target?",bg="#0e1111",fg="#5865F2")
labelb = tk.Label(root, text="What is the Bot Token Used?",bg="#0e1111",fg="#5865F2")
buttona = tk.Button(root, text="Start Bot", command=start_bot,)
buttona.config(background="#353839",foreground="#5865F2")
root.config(background="#0e1111")
root.title("Speech BubBot")
root.geometry("200x100")
labela.pack()
TARGETIDtxt.pack()
labelb.pack()
tokentxt.pack()
buttona.pack()
root.mainloop()
#test for changes to pre