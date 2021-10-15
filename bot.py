import discord.ext.commands as commands
import os


bot = commands.Bot(command_prefix='*')

bot.run(os.environ['TOKEN'])