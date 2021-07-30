"""
Innexia Music, Telegram Voice Chat Bot
Copyright (C) 2021  Mr Sammy
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
from config import Config
from pyrogram import Client
from config import Config
REPLY_MESSAGE=Config.REPLY_MESSAGE
if REPLY_MESSAGE is not None:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH,
        plugins=dict(root="innexia")
        )
else:
    USER = Client(
        Config.SESSION,
        Config.API_ID,
        Config.API_HASH
        )
USER.start()
