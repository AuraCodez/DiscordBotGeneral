import discord
from discord.ext import commands
import sqlite3
from json import loads
import random
import requests


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=",", intents=intents)


#Database to store 1) the swear word and 2) the swear count of each user 3) the username
#Make a database named swearDB.db (or any name you perfer) and store it in the root directory of your repo
conn = sqlite3.connect("swearDB.db")
cursor = conn.cursor()



yourServerIdGoesHere = (
    0  # Setup Your server ID here (To introduce the users to your server)
)
yourChannelIdGoesHere = 0  # 0 Set up your channel ID to greet the user here.


@bot.command()
async def commands(ctx):
    await ctx.reply(
        "The commands that are available are multiply, add, divide, subtract, pi, divide, guessTheNumber, convertMetersToKilometers, quote. All of these are used with the prefix of a comma. for example ,add 5 1"
    )


@bot.command()
async def hello(ctx, name):
    await ctx.reply(f"Hello welcome to the server {name}.")


# API quote
@bot.command()
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    data = loads(response.text)
    quote = data[0]["q"] + " -" + data[0]["a"]

    await ctx.reply(quote)


# API fact
@bot.command()
async def fact(ctx):
    with open("apiID.txt") as f:
        api_key = f.read()

    limit = 3
    api_url = "https://api.api-ninjas.com/v1/facts?limit={}".format(limit)
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    factList = loads(response.text)
    factz = []
    for i in range(len(factList)):
        for key in factList[i]:
            factz.append(factList[i][key])

    factzRandom = random.choice(factz)
    await ctx.send(factzRandom)


@bot.event
async def on_member_join(member):
    guild = bot.get_guild(yourServerIdGoesHere)  # Your server ID goes here
    channel = guild.get_channel(yourChannelIdGoesHere)  # Your Channel ID goes here
    await channel.send(f"Welcome to the server. {member.mention}")
    await member.send(
        f"Welcome to the {guild.name} server, I am a discord bot feel free to add me to your server. New updates being added daily!"
    )


swearJar = 0


@bot.event
async def on_message(message):
    badword_list = [
        "test",
        "stuff",
        "lol",
    ]  # Either store it as a list or read in a notepad file with a lot of swear words.
    for i in range(len(badword_list)):
        if badword_list[i] in message.content.lower():
            global swearJar  # Setting to global variable
            swearJar += 1
            await message.channel.purge(limit=1)
            user = str(message.author)
            message_content = message.content
            cursor.execute(
                "INSERT INTO swear(name, word, count) VALUES(?, ?, ?)",
                (user, message_content, swearJar),
            )
            conn.commit()
            conn.close()
            await message.author.send(
                f"Watch it. You currently have {swearJar} swears in total. Reaching 20 would result in an automatic ban."
            )
    await bot.process_commands(
        message
    )  # You're trying to run the commands and a on_message at the same time, which causes the commands not to work. So you need to add this process_commands


with open("asdfID.txt") as f:  # This is where the bt goes. Paste it in here.
    TOKEN = f.readline()


bot.run(TOKEN)
