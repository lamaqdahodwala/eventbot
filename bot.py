import discord.ext.commands as commands
import os
from components.main import Main

bot = commands.Bot(command_prefix='*')


bot.add_cog(Main(bot))


# bot.run(os.environ['TOKEN'])
# bot.run(os.environ['TOKEN'])
bot.run('ODk4Njg5OTE1NjM2ODI2MTkz.YWn4NA._cpZyuJzlCsXeTIhJ6OeEc0nxzg')
