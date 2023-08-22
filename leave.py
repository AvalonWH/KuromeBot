import discord
from discord.ext import commands

class Leave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leave")
    async def leave(self, ctx):
    
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
            await ctx.send("**🌘 Me he desconectado del canal de voz 💤**")
        else:
            await ctx.send("**No estoy conectada a un canal de voz 🌻 **")
            
async def setup(bot):
  await bot.add_cog(Leave(bot))