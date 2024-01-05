import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.slash_command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel"
)
async def clearfred(ctx: commands.SlashContext, limit: int = 100):
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You don't have the required permissions to execute this command.", ephemeral=True)
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560

    deleted = await ctx.channel.purge(limit=limit, check=is_fredboat, bulk=True)
    await ctx.send(f"Deleted {len(deleted)} message(s) from FredBoat.", ephemeral=True)

# Use the environment variable to get the bot token
bot_token = os.environ.get("DISCORD_BOT_TOKEN")

# Make sure the bot token is not None
if bot_token is not None:
    # Start the bot with the token
    bot.run(bot_token)
else:
    print("Bot token not found in environment variables.")
