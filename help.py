import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        
        embed = discord.Embed(color=0x123456)

        embed.title = "⭐️ Comandos de ayuda💫" 
        embed.description = "🌟 Lista de comandos disponibles 🪐"
        
        embed.add_field(name="", value=f"`-join: `᲼᲼᲼᲼᲼Llamas a Kurome a unirse a tu chat de voz", inline=False)
        embed.add_field(name="", value=f"`-leave: `᲼᲼᲼᲼Kurome Sale de tu chat de voz", inline=False)
        embed.add_field(name="", value=f"`-play: `᲼᲼᲼᲼᲼Kurome Reproduce tus canciones favoritas", inline=False)
        embed.add_field(name="", value=f"`-skip: `᲼᲼᲼᲼᲼Kurome Salta la canción actual", inline=False)
        embed.add_field(name="", value=f"`-pause: `᲼᲼᲼᲼Kurome Pausa la música", inline=False)
        embed.add_field(name="", value=f"`-resume: `᲼᲼᲼Kurome Reanuda la música", inline=False)
        embed.add_field(name="", value=f"`-shuffle: `᲼᲼Kurome la cola cambia a modo aleatorio", inline=False)
        embed.add_field(name="", value=f"`-clear: `᲼᲼᲼᲼Kurome Borra la cola de música del servidor", inline=False)
        embed.add_field(name="", value=f"`-ping: `᲼᲼᲼᲼᲼Muestra el ping del bot y sus estadísticas", inline=False)
        
        embed.set_footer(text=f"🌑 Kurome v{discord.__version__}")
        embed.add_field(name=" ", value="**✨GitHub:** [AvalonWH](https://github.com/AvalonWH) | (`Futuro sitio web del bot xdxd`)")
        

async def setup(bot):
  await bot.add_cog(Help(bot))