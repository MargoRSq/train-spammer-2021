import asyncio
import aioschedule as schedule
import requests
import time

from threading import Thread
from io import BytesIO

from vkbottle import PhotoMessageUploader
from vkbottle.bot import Bot

from utils.timetable_utils import get_week_num, get_weekday
from utils.timetable import get_day_timetable
from utils.config import (TOKEN, CAT_TOKEN, CHAT_ID,
                          MONDAY,
                          TUESDAY,
                          WEDNESDAY,
                          THURSDAY,
                          FRIDAY,
                          SATURDAY)

bot = Bot(TOKEN)

pivoday = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]

async def good_night():
    weekday = get_weekday() + 1
    headers = {"x-api-key": CAT_TOKEN}
    cat_image_url = requests.get(url="https://api.thecatapi.com/v1/images/search", headers=headers).json()[0]['url']
    cat_image = requests.get(cat_image_url).content
    img = BytesIO(cat_image)
    photo = await PhotoMessageUploader(bot.api).upload(img)
    if weekday == 6:
        weeknum =  get_week_num() + 1
        timetable = get_day_timetable(0, weeknum)
    else:
        timetable = get_day_timetable(weekday)
    text = f'Спокойной ночи, малыши:3\nРасписание на следующий учебный день:\n{timetable}'
    await bot.api.messages.send(chat_id=CHAT_ID, message=text, random_id=0, attachment=photo)

async def good_morning():
    weekday = get_weekday()
    if weekday != 6:
        timetable = get_day_timetable(weekday)
        await bot.api.messages.send(
            message = f'Доброе утро, пупсики, воть расписание на сегодня :3\n{timetable}',
            attachment=pivoday[weekday],
            chat_id=CHAT_ID,
            random_id=0)

def do_schedule():
    schedule.every().day.at("07:00").do(good_morning)
    schedule.every().day.at("23:30").do(good_night)
    loop = asyncio.new_event_loop()
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)

def time_loop():
    thread = Thread(target=do_schedule)
    thread.start()
