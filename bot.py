import discord
import cogs
from templatebot import Bot
from discord import AllowedMentions, Activity, Game
from os import environ as env
from dotenv import load_dotenv


bot = Bot(
    name="Paint",
    command_prefix="p!",
    allowed_mentions=AllowedMentions(
     everyone=False, roles=False, users=True),
    activity=Game("with colors!"),
)
bot.VERSION = "1.0.0"

for i in cogs.default:
  bot.load_extension(f"cogs.{i}")

bot.run(env.get("TOKEN", None))