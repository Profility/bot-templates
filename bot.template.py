import os
import discord
import logging
from ruamel.yaml import YAML
from discord.ext import commands

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

# Load configuration file
cogs = []
with open('config.yml', 'r') as conf:
    config = YAML().load(conf)

bot = commands.Bot(
    command_prefix=config['bot']['prefix'],
    help_command=None
)

# When bot is ready
@bot.event
async def on_ready():
    log.info(f'{bot.user} ({bot.user.id}) is online!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(config['bot']['status'].format(prefix = config['bot']['prefix'])))

# Load cogs
for f in os.listdir('./path/subpath'): # change to folder path
    if f.endswith('.py'):
        cogs.append(f'{f[:-3]}')
        bot.load_extension(f'path.subpath.{f[:-3]}') # change to folder path, replace / with .
        log.info(f'Loaded {f[:-3]}')

bot.run(config['bot']['token'])