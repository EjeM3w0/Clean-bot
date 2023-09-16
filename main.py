import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')

@bot.command("info")
async def info (ctx):
    info = ("https://translated.turbopages.org/proxy_u/en-ru.ru.830574b3-6505969e-0551ac5d-74722d776562/https/en.wikipedia.org/wiki/Pollution ,  https://studfile.net/preview/1636331/ ,  https://natworld.info/nauki-o-prirode/vidy-istochniki-i-prichiny-zagrjaznenija-okruzhajushhej-prirodnoj-sredy ,  https://rusarctica.ru/blog/khoroshee-delo/kak-spasti-prirodu-8-shagov-kotorye-mozhet-sdelat-kazhdyy/   --   это сайты, которые помогут вам разобраться в проблеме загрезнения")
    await ctx.send(info)

bot.run("")
