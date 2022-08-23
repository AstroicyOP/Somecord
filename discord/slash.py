import datetime

import discord

bot = discord.Bot(debug_guilds=[...])

@bot.slash_command()
@option(name="channel1", choices=["Channel1", "Channel2"])
async def choice_test(ctx, channel1):
    channel = bot.get_channel(939551193145950258)
    Channel1: channel
    await Channel1.send()



@bot.slash_command()
async def timeout(ctx: discord.ApplicationContext, member: discord.Member, minutes: int):
    """Apply a timeout to a member."""

    duration = datetime.timedelta(minutes=minutes)
    await member.timeout_for(duration)
    await ctx.respond(f"Member timed out for {minutes} minutes.")

    """
    The method used above is a shortcut for:
    until = discord.utils.utcnow() + datetime.timedelta(minutes=minutes)
    await member.timeout(until)
    """


bot.run("TOKEN")
