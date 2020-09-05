# imports iniciales
import random
import asyncio
import discord
import tweepy
from discord.ext import commands
import randomTweetPicker
import local_settings

# declaraciones de cliente
token = local_settings.discord_token
client = discord.Client()
bot = commands.Bot(command_prefix='.')
server_test = bot.get_guild(id='651245325868335125')


# eventos
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="tu perfil de Twitter | .ayuda"))
    server = bot.get_guild(id='521405402559283201')
    server_test = bot.get_guild(id='651245325868335125')
    # return server
    # return server_test
    # return server
    print('Listo para la acción')


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Listo para la acción (.ayuda)')
        break


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def ayuda(ctx):
    await ctx.send('```Comandos:\n\n.ping -> Mide latencia.\n\n.rtp usuario (sin "@") -> Devuelve un tweet aleatorio de los últimos 100 tweets originales de un usuario```')


@bot.command()
async def rtp(ctx, arg):
    usuario = '@'+arg
    mensaje_error = '*El usuario '+usuario + \
        ' no existe o su cuenta es privada/está suspendida.*'
    print(usuario)
    try:
        tweet = randomTweetPicker.get_random_tweet(usuario)
        print(tweet)
        await ctx.send('@' + arg + ' dijo: ' + tweet)
    except tweepy.error.TweepError:
        print(mensaje_error)
        await ctx.send(mensaje_error)

print('comandos cargados')

bot.run(token)
