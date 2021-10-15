import discord.ext.commands as commands
import os
from components.main import Main

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Alive and ready!')


bot.add_cog(Main(bot))


bot.run(os.environ['TOKEN'])
