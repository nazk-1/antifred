import os
import discord
from discord.ext import commands
import asyncio
import interactions  # Make sure this is installed with pip install discord-py-interactions

intents = discord.Intents.default()
intents.messages = True  # Make sure this is enabled
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
slash = interactions.Client(token=os.getenv('DISCORD_BOT_TOKEN'))

@bot.event
async def on_message(message):
    if message.author.id == 184405311681986560:  # FredBoat's User ID
        await asyncio.sleep(10)  # Adjust time as needed
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("I don't have permission to delete this message.")
        except discord.errors.NotFound:
            print("Message was not found (maybe it was already deleted).")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
@slash.command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel"
)
async def clearfred(ctx: interactions.CommandContext, limit: int = 100):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You don't have the required permissions to execute this command.", ephemeral=True)
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560

    deleted = await ctx.channel.purge(limit=limit, check=is_fredboat, bulk=True)
    await ctx.send(f"Deleted {len(deleted)} message(s) from FredBoat.", ephemeral=True)

slash.start()