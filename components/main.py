import asyncio
import discord.ext.commands as commands
import discord
import aiohttp


class Main(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.session = aiohttp.ClientSession

    @commands.command(name='events')
    async def show_events(self, ctx, events=5):
        # try:
            async with self.session() as session:
                resp = await session.get('https://thrillshare-cmsv2.services.thrillshare.com/api/v4/o/5080/cms/events?locale=en')
                json = await resp.json()
                embed = discord.Embed(title='IMS events')


                for i in range(events):
                    async with ctx.typing():
                                                
                        event = json['events'][i]
                        embed.add_field(name=event['title'], value=event['cms_formatted_date'], inline=False)

                await ctx.send(embed=embed)

        # except Exception as e:
        #     print(e)
        #     await ctx.send('Something went wrong.')