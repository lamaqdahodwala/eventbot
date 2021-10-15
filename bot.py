import discord.ext.commands as commands
import os
from server.server import main
import threading
from components.main import Main

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Alive and ready!')


bot.add_cog(Main(bot))

t = threading.Thread(target=main)

t.start()

bot.run(os.environ['TOKEN'])
