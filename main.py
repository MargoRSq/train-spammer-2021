from typing import Tuple
from vkbottle.bot import Bot, rules, Message

from utils.config import TOKEN, GROUP_ID
from commands import bps

bot = Bot(TOKEN)

for bp in bps:
    bp.load(bot)

print("Here we go!")
bot.run_forever()