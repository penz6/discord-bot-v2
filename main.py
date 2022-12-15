import discord
from discord.ext import commands
from bottoken import bottoken
from better_profanity import profanity
from roleid import roleid
from channelid import channelid
from discord import app_commands
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
#you have to define client for some reason


#login message
@client.event
async def on_ready():
    await tree.sync()
    print("Logged into Discord")



#filter
@client.event
async def on_message(message):
        profanity.load_censor_words()
        if profanity.contains_profanity(message.content):
            modchannel = client.get_channel(channelid)
            ##channel definition (hardcoded)
            await message.author.add_roles(message.guild.get_role(roleid))
            await message.delete()
            ##deletes message (hardcoded) right click on the role you want and choose get id 
            logembed = discord.Embed(title="Someone has said something that is in your block list, they have been flagged with the flagged role. They have limited access to the server until you remove it.", color=0x845883)
            logembed.add_field(name="User?", value=message.author, inline=False)
            logembed.add_field(name="Content?", value=message.content, inline=False)
            ##embed
            await modchannel.send(embed=logembed)
            await message.channel.send("Your message has been deleted due to offensive content, the appropriate people have been contacted.")
            ##sends stuff

# defines role id
@tree.command(name="roleid", description="set the role id")
@app_commands.default_permissions()
async def roleidcommand(interaction, roleid1 : str): 
    f = open( 'roleid.py', 'w' )
    f.write("roleid = " + roleid1)
    f.close()
    await interaction.response.send_message("Done")

#defines channel id
@tree.command(name="channelid", description="set the channel id")
@app_commands.default_permissions()
async def roleidcommand(interaction, channelid1 : str): 
    f = open( 'channelid.py', 'w' )
    f.write("channelid = " + channelid1)
    f.close()
    await interaction.response.send_message("Done")

#run bot
client.run(bottoken)





