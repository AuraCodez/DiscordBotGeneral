import sqlite3
import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=",",intents=intents)

yourServerIdGoesHere = 0 #Setup Your server ID here 
yourChannelIdGoesHere = 0 #0 Set up your channel ID to greet the user here.

#@bot.event #Creating the new Database needed
#async def on_ready():
   # db = sqlite3.connect('main')
   # cursor = db.cursor()
   # cursor.execute('''
   # CREATE TABLE IF NOT EXISTS main(
      #  guild_id TEXT,
      #  msgTEXT,
      #  channel_id TEXT )
  # ''' )

@bot.command()
async def commands(ctx):
    await ctx.reply("The commands that are available are multiply, add, divide, subtract, pi, divide, guessTheNumber, convertMetersToKilometers, quote. All of these are used with the prefix of a comma. for example ,add 5 1")

@bot.command()
async def hello(ctx,name):
    await ctx.reply(f"Hello welcome to the server {name}.")

@bot.command()
async def multiply(ctx,a:int,b:int):
    await ctx.reply(f"{a} multiplied by {b} equals to {(a * b)}")

@bot.command()
async def add(ctx,a:int,b:int):
    await ctx.reply(f"{a} added by {b} equals to {(a+b)}")

@bot.command()
async def pi(ctx):
    await ctx.reply(f"The digits 100 of pi are 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 ")

@bot.command()
async def subtract(ctx,a:int,b:int):
    await ctx.reply(f"{a} subtracted by {b} equals to {(a-b)}")

@bot.command()
async def divide(ctx,a:float,b:float):
    await ctx.reply(f"{a} divided by {b} equals to {(a/b):.2f}")

@bot.command()
async def convertMetersToKilometers(ctx,a:int):
    await ctx.reply(f"{a} meters is {(a/1000)} kilometers")

@bot.command()
async def convertGramsToKilograms(ctx,a:int):
    await ctx.reply(f"{a} grams is {(a/1000)} kilograms")

@bot.command() #Can Implement an API for this?
async def quote(ctx):
    quoteList = ["Quote 1", "Quote 2", "Quote 3", "Quote 4"] #These will generate random quotes on what you put in the list, you can read it as a file.
    await ctx.send(str(random.choice(quoteList)))

@bot.command() #Can implement an API for this?
async def randomFact(ctx):
    randomFactList = ["Fact 1", "Fact 2"] #These will generate random facts on what you put in the list, you can read it as a file.
    await ctx.send(str(random.choice(randomFactList)))

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(yourServerIdGoesHere) #Your server ID goes here
    channel = guild.get_channel(yourChannelIdGoesHere) #Your Channel ID goes here
    await channel.send(f"Welcome to the server. {member.mention}")
    await member.send(f"Welcome to the {guild.name} server, I am a discord bot feel free to add me to your server. New updates being added daily!")

userSwears = 0
 
@bot.event
async def on_message(message):
    badword_list = ["stupid","dumb","test"] #Either store it as a list or read in a notepad file with a lot of swear words.
    for i in range (len(badword_list)):
        if badword_list[i] in message.content.lower():
            global userSwears #Setting to global variable
            swearJar +=1
            await message.channel.purge(limit=1)
            await message.author.send(f"Watch it. You currently have {swearJar} swears in total. Reaching 20 would result in an automatic ban.")
    await bot.process_commands(message) #You're trying to run the commands and a on_message at the same time, which causes the commands not to work. So you need to add this process_commands


with open('asdfID.txt') as f: #This is where the bt goes.
    TOKEN = f.readline()

bot.run(TOKEN)

