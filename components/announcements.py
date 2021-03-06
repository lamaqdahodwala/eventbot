import asyncio
import discord.ext.commands as commands
import discord
import re
import aiohttp


class Announcements(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.session = aiohttp.ClientSession
    
    @commands.command(name='announcements')
    async def get_announcements(self, ctx):
        async with self.session() as session:
            resp = await session.get('https://thrillshare-cmsv2.services.thrillshare.com/api/v2/s/94968/live_feeds?locale=en')
            json = await resp.json() 

            announcement = json['live_feeds'][0]

            time_ago = announcement['time_ago']
            an = announcement['status']

            a = re.split(r'\*', an)

            embed = discord.Embed(title="IMS Announcements")
            embed.color = discord.Color.green()

            for i in a:
                embed.add_field(name="Announcement", value=i)

            await ctx.send(embed=embed)