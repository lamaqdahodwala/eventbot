import discord
import discord.ext.commands as commands
from bs4 import BeautifulSoup
import aiohttp
class Teachers(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.session = aiohttp.ClientSession

    @commands.command()
    async def search(self, ctx, teacher):
        embed = discord.Embed(title='Results')
        async with self.session() as session:
            resp = await session.get(f'https://thrillshare-cmsv2.services.thrillshare.com/api/v4/o/5080/cms/directories?locale=en&search={teacher}&filter_ids=')           
            json = await resp.json()
            dirs = json['directories']
            for i in dirs:
                s = BeautifulSoup(i['link'], features='html5lib')
                
                embed.add_field(name=i['full_name'], value=f"""
Title: {i['title']}
Email: {i['email']}
Site: {s.a['href'] if s.a['href'] else 'None'}
                """, inline=False)
            
            await ctx.send(embed=embed)
