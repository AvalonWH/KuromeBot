import discord
from discord.ext import commands

class Join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='join')
    async def join(self, ctx):
        
        if ctx.author.voice is None:
            await ctx.send("**⚠️ No estás en un canal de voz!**")
            return
        
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()

        else:
            await ctx.voice_client.move_to(voice_channel)
            
        try:
            # Quitar linea connect
            await ctx.send(f"**Me uní al canal de voz:  `{voice_channel}` ✨**")

        except Exception as e:
            print(e)
            await ctx.send("**Error al unirme al canal de voz 💩**")

async def setup(bot):
  await bot.add_cog(Join(bot))