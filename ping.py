import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name='ping')
    async def ping(self, ctx):
        
        embed = discord.Embed(color=0x123456)

        embed.set_author(name=f"¡Pong! 🏓", icon_url=self.bot.user.avatar.url)
        embed.title = "**✨ Estadísticas de Kurome 🍡✨**"
        embed.add_field(name="", value=f"**🌐 Ping API: {round(self.bot.latency * 1000)}ms**", inline=False)
        embed.add_field(name="", value=f"**🌎 Estoy en: {len(self.bot.guilds)} Servidores  🗿**", inline=False)
        
        embed.set_footer(text=f"🌑 Kurome v{discord.__version__}")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))