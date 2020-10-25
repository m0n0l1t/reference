import discord
from config import logger, token, bots, owner
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command("help")


@logger.catch
def main():
    @client.command()
    @commands.is_owner()
    async def load(ctx, extension):
        if ctx.author.id in owner:
            client.load_extension(f"Bots.{extension}")
            await ctx.send(f"{extension} is loaded..")

    @client.command()
    @commands.is_owner()
    async def unload(ctx, extension):
        if ctx.author.id in owner:
            client.unload_extension(f"Bots.{extension}")
            await ctx.send(f"{extension} is unloaded..")

    @client.command()
    @commands.is_owner()
    async def reload(ctx, extension):
        if ctx.author.id in owner:
            client.unload_extension(f"Bots.{extension}")
            client.load_extension(f"Bots.{extension}")
            await ctx.send(f"{extension} is reloaded..")

    for filename in bots:
        client.load_extension(filename)

    client.run(token)


main()
