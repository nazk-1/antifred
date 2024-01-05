import os
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.messages = True  # Make sure this is enabled
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

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

