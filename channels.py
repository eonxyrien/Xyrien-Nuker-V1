import asyncio
import random

async def delchanny(guild):
    channels = guild.channels
    return await asyncio.gather(*(channel.delete() for channel in channels))

name = [
"xyrienontop",
"nanoangstrom",
"nukedbyxyrien",
"xyriraiders",
"foreverxyri",
"he-awaits"
]

async def crechanny(guild, name=name):
    return await asyncio.gather(
        *(guild.create_text_channel(f"#{random.choice(name)}") for _ in range(60))
    )
