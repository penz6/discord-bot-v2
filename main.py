import discord
import random
import token.py
bot = commands.Bot(command_prefix='>', intents=intents)
#you have to define bot for some stupid reason so here it is

#login message
@client.event
async def on_ready():
    print("We have logged in boys.")
#select mission
missionlist = ["Crystalline Caverns","Magma Core","Glacial Strata","Salt Pits","Azure Weald","Sandblasted Corridors","Dense Biozone","Hollow Bough","Fungus Bogs","Chernobyl"]
randommission = random.choice(missionlist)
#send the actual mission
@bot.hybrid_group(fallback="get")
async def mission(ctx):
    await ctx.send(randommission)
#run bot
token.run(botoken)







