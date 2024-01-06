import asyncio
import os
import interactions

bot = interactions.Client(token=os.getenv('DISCORD_BOT_TOKEN'))

@interactions.slash_command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel"
)
async def clearfred(ctx: interactions.SlashContext):
    await ctx.defer(ephemeral=True)

    # Checking permissions using try-except block
    try:
        if not ctx.author.permissions & interactions.Permissions.MANAGE_MESSAGES:
            await ctx.send("You don't have the required permissions to execute this command.", ephemeral=True)
            return
    except AttributeError:
        await ctx.send("Cannot verify permissions.", ephemeral=True)
        return

    channel = bot.get_channel(ctx.channel_id)
    messages = await channel.history(limit=100).flatten()
    fredboat_messages = [msg for msg in messages if msg.author.id == 184405311681986560]

    for msg in fredboat_messages:
        await msg.delete()

    await ctx.send(f"Deleted {len(fredboat_messages)} message(s) from FredBoat.", ephemeral=True)

@bot.event
async def on_message_create(message):
    if message.author.id == 184405311681986560:
        await asyncio.sleep(5)
        try:
            await message.delete()
        except Exception as e:
            print(f"Error in deleting message: {e}")

bot.start()
