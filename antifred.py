import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.tree.sync()  # Synchronize slash commands

@bot.event
async def on_message(message):
    if message.author.id == 184405311681986560:  # FredBoat's User ID
        await asyncio.sleep(10)  # 10-second delay
        try:
            await message.delete()
        except discord.Forbidden:
            print("I don't have permission to delete this message.")
        except discord.NotFound:
            print("Message was not found (maybe it was already deleted).")

    await bot.process_commands(message)

@bot.tree.command(name="clearfred", description="Clears messages from FredBoat in the current channel")
async def clearfred(interaction: discord.Interaction, limit: int = 100):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("You don't have the required permissions to execute this command.", ephemeral=True)
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560

    deleted = await interaction.channel.purge(limit=limit, check=is_fredboat, bulk=True)
    await interaction.response.send_message(f"Deleted {len(deleted)} message(s) from FredBoat.", ephemeral=True)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
