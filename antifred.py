import os
import discord
from discord import Intents
from discord.ext import commands

intents = Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.id == 184405311681986560:  # FredBoat's User ID
        await discord.utils.sleep_until(10)  # Adjust time as needed
        try:
            await message.delete()
        except discord.Forbidden:
            print("I don't have permission to delete this message.")
        except discord.NotFound:
            print("Message was not found (maybe it was already deleted).")

    await bot.process_commands(message)  # Important for commands to work alongside on_message

@bot.slash_command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel"
)
async def clearfred(ctx: discord.ApplicationContext, limit: int = 100):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.respond("You don't have the required permissions to execute this command.", ephemeral=True)
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560

    deleted = await ctx.channel.purge(limit=limit, check=is_fredboat, bulk=True)
    await ctx.respond(f"Deleted {len(deleted)} message(s) from FredBoat.", ephemeral=True)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
