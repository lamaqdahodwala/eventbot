import discord
import discord.ext.commands as commands
import aiohttp
class Teachers(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.session = aiohttp.ClientSession

    @commands.command()
    async def search(self, ctx, teacher):

        async with self.session() as session:
            session.get(f'https://thrillshare-cmsv2.services.thrillshare.com/api/v4/o/5080/cms/directories?locale=en&search={teacher}&filter_ids=')           
             
