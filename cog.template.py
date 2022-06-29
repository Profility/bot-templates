from discord.ext import commands

class cogname(commands.Cog):
    def __init__(self, client):
       self.client = client 
    
    # Cog command
    @commands.command()
    async def command_example(self):
        """
        Template for commands in a cog
        """

    # Cog listener
    @commands.Cog.listener()
    async def listener_example(self):
        """
        Template for listeners in a cog
        """

# Cog setup
def setup(client):
    client.add_cog(cogname(client))