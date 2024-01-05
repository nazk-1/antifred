import os
import discord
from discord.ext import commands
import asyncio
from interactions import Client  # Updated import statement

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
slash = Client(token=os.getenv('DISCORD_BOT_TOKEN'))  # Updated Client import

@bot.event
async def on_message(message):
    if message.author.id == 184405311681986560:  # FredBoat's User ID
        await asyncio.sleep(30)  # Wait for 30 seconds before deleting the message
        try:
            await message.delete()
        except discord.errors.Forbidden:
            print("I don't have permission to delete this message.")
        except discord.errors.NotFound:
            print("Message was not found (maybe it was already deleted).")

@slash.command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel"
)
async def clearfred(ctx, limit: int = 100):  # Removed interactions.CommandContext
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You don't have the required permissions to execute this command.", ephemeral=True)
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560

    deleted = await ctx.channel.purge(limit=limit, check=is_fredboat, bulk=True)
    await ctx.send(f"Deleted {len(deleted)} message(s) from FredBoat.", ephemeral=True)

slash.start()
