import asyncio
import os
import interactions

bot = interactions.Client(token=os.getenv('DISCORD_BOT_TOKEN'))

# Slash Command to clear messages from FredBoat
@bot.command(
    name="clearfred",
    description="Clears messages from FredBoat in the current channel",
    scope=1234567890  # replace with your guild ID
)
async def clearfred(ctx: interactions.CommandContext):
    await ctx.defer(ephemeral=True)  # Defer the response

    if not ctx.author.permissions & interactions.Permissions.MANAGE_MESSAGES:
        await ctx.send("You don't have the required permissions to execute this command.")
        return

    def is_fredboat(msg):
        return msg.author.id == 184405311681986560  # FredBoat's User ID

    channel = await bot.get_channel(ctx.channel_id)
    messages = await channel.get_messages(limit=100)
    fredboat_messages = [msg for msg in messages if is_fredboat(msg)]

    for msg in fredboat_messages:
        await msg.delete()

    await ctx.send(f"Deleted {len(fredboat_messages)} message(s) from FredBoat.")

# Event listener to automatically delete FredBoat's messages after 5 seconds
@bot.event
async def on_message_create(ctx):
    if ctx.author.id == 184405311681986560:  # FredBoat's User ID
        await asyncio.sleep(5)  # Change delay to 5 seconds
        try:
            await ctx.delete()
        except Exception as e:
            print(f"Error in deleting message: {e}")

bot.start()
