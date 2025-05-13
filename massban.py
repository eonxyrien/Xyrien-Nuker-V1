import asyncio

async def massban(guild, reason="FUCKED BY ASTRAL"):
    tasks = []
    for member in guild.members:
        tasks.append(guild.ban(member, reason=reason))
        await asyncio.gather(*tasks)
