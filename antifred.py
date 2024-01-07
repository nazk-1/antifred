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

    channel = bot.get_channel(ctx.channel_id)
    messages = await channel.history(limit=100).flatten()
    user_ids = (945683386100514827, 184405311681986560)
    fredboat_messages = [msg for msg in messages if msg.author.id in user_ids]

    for msg in fredboat_messages:
        await msg.delete()

    await ctx.send(f"Deleted {len(fredboat_messages)} message(s) from FredBoat.", ephemeral=True)

userids = (945683386100514827, 184405311681986560)
@bot.event
async def on_message_create(message):
    if message.author.id in userids:
        await asyncio.sleep(10)
        try:
            await message.delete()
        except Exception as e:
            print(f"Error in deleting message: {e}")

bot.start()
