

from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@UstaD.on(events.NewMessage(pattern="/ping"))
@UstaD2.on(events.NewMessage(pattern="/ping"))
@UstaD3.on(events.NewMessage(pattern="/ping"))
@UstaD4.on(events.NewMessage(pattern="/ping"))
@UstaD5.on(events.NewMessage(pattern="/ping"))
@UstaD6.on(events.NewMessage(pattern="/ping"))
@UstaD7.on(events.NewMessage(pattern="/ping"))
@UstaD8.on(events.NewMessage(pattern="/ping"))
@UstaD9.on(events.NewMessage(pattern="/ping"))
@UstaD10.on(events.NewMessage(pattern="/ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "𝐢𝐒𝐎𝐔𝐋!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤖ɪ𝐄𝐀𝐆𝐋𝐄 !\n`{ms}` 𝗺𝘀")                       
