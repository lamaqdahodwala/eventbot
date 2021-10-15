import asyncio
import discord.ext.commands as commands
import aiohttp


class Main(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.session = aiohttp.ClientSession

    @commands.command(name='events')
    async def show_events(self, ctx, events=5):
        async with self.session() as session:
            resp = await session.get('https://thrillshare-cmsv2.services.thrillshare.com/api/v4/o/5080/cms/events?locale=en')
            json = await resp.json()
            
            for i in range(events):
                async with ctx.typing():
                    event = json[i]
                    await ctx.send(f'{event["title"]} - {event["cms_formatted_date"]}')
                    await asyncio.sleep(1)

            