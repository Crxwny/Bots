import discord
from discord import Intents
from discord.ext import commands
import os
import random

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = Intents.default()
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()  # Slash Commands synchronisieren
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Fehler beim Synchronisieren: {e}")

    print(f"🤖 {bot.user} ist online!")


@bot.tree.command(name="hello", description="Sagt Hallo!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hey!")


@bot.tree.command(name="roll", description="Würfelt eine Zahl zwischen 1 und 6")
async def roll(interaction: discord.Interaction):
    number = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 Du hast eine **{number}** gewürfelt!")


@bot.tree.command(name="help", description="Zeigt die Hilfe an")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "ℹ️ **Hilfe:**\n`/hello` – Sagt Hallo\n`/roll` – Würfelt eine Zahl\n`/help` – Zeigt diese Hilfe an")


def run_discord_bot():
    bot.run(TOKEN)
