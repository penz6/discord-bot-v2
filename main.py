import discord
from discord.ext import commands
from bottoken import bottoken
from profanity_check import predict, predict_prob
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#you have to define client for some reason

#login message
@client.event
async def on_ready():
    print("Logged into Discord")
#filter
@client.event
async def on_message(message):
        if predict_prob([message.content]) > .90:
            modchannel = client.get_channel(731715895612670043) ##add channel id here
            ##channel definition
            await message.author.add_roles(message.guild.get_role(1042529545204539414))## specify role id here
            await message.delete()
            ##deletes message
            logembed = discord.Embed(title="Someone has said something that is in your block list, they have been flagged with the flagged role. They have limited access to the server until you remove it.", color=0x845883)
            logembed.add_field(name="User?", value=message.author, inline=False)
            logembed.add_field(name="Certainty? (in decimal form)", value=predict_prob([message.content]), inline=False)
            logembed.add_field(name="Content?", value=message.content, inline=False)
            ##embed
            await modchannel.send(embed=logembed)
            await message.channel.send("Your message has been deleted due to offensive content, the appropriate people have been contacted.")
            ##sends stuff
            




#run bot
client.run(bottoken)







