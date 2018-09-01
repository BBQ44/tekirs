#Tekir by Haso
import discord
import asyncio
import logging
import random
import time
from discord.ext.commands import Bot
from discord.ext import commands

BOT_PREFIX = "tk!"
TOKEN = "NDIzODIyMjYyNjY4NjIzODcy.DZ--vQ.IKcVC8NiqlZbLVIxOCz7btxaUsg"

client = Bot (command_prefix=BOT_PREFIX)

print (discord.__version__)

@client.command(name='Avatar', pass_context=True)
async def avatar(url, member: discord.Member = None):
    embed = discord.Embed(title="Resim")
    embed.set_image(url=member.avatar_url)
    await client.say(embed=embed)


killResponses = [" Yere Çakılarak Öldü " , " Elektrik Akımından Öldü ", " Silahla Vurularak Öldü " , " Kuduzdan Öldü" , " Kan Kaybından Öldü " , " Yaşlılıktan Öldü " , " Hastalıktan Öldü " , " Soğuk Esprilerden Öldü " , " Donarak Öldü " , " Aşırı Sıcaktan Öldü " , " Balinaların Yanına Atılarak Öldü" , "Death Note'ye Yazılarak Öldü"
]
@client.command(name='kill',
                description="Açıklama",
                pass_context = True)
async def kill(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + "Birini Etiketle")
        return

    if member.id == "423822262668623872":
        await client.say(ctx.message.author.mention + " Beni Mi Öldürüceksin")
    if member.id == "409320814081736707":
        await client.say(ctx.message.author.mention + " Beni Mi Öldürüceksin")
    elif member.id == ctx.message.author:
        await client.say(ctx.message.author.mention + "YAZI2")
    else:
        random.seed(time.time())
        chosenResponse = killResponses[random.randrange(len(killResponses))]
        await client.say("{}".format(member.name) + chosenResponse)

client.run(TOKEN) 
