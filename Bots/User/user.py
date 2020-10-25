from .models import Users, user_table, engine
from config import logger
import discord
from discord.ext import commands


class User(commands.Cog):

    def __init__(self, client):
        self.client = client
        user_table.metadata.create_all(engine)

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("User is ready")

    @commands.command()
    async def info(self, ctx):
        await ctx.send("Help, wolrd!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        user = Users(message.author.id)
        if message.content.lower().startswith('помидор'):
            await message.channel.send("огурец")


def setup(client):
    client.add_cog(User(client))

