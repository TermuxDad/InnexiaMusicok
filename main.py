"""
Innexia Music, Telegram Voice Chat Bot
Copyright (C) 2021  Mr Sammy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

from pyrogram import Client, idle
import os
from config import Config
from utils import mp
from pyrogram.raw import functions, types

CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="innexiaMusic")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()

bot.run(main())
bot.start()
bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Check if bot alive"
            ),
            types.BotCommand(
                command="help",
                description="Shows help message"
            ),
            types.BotCommand(
                command="play",
                description="Play song from youtube/audiofile"
            ),
            types.BotCommand(
                command="deezer",
                description="Play song from Deezer"
            ),
            types.BotCommand(
                command="player",
                description="Shows current playing song with controls"
            ),
            types.BotCommand(
                command="playlist",
                description="Shows the playlist"
            ),
            types.BotCommand(
                command="skip",
                description="Skip the current song"
            ),
            types.BotCommand(
                command="joinvc",
                description="Join VC"
            ),
            types.BotCommand(
                command="leave",
                description="Leave from VC"
            ),
            types.BotCommand(
                command="vc",
                description="Ckeck if VC is joined"
            ),
            types.BotCommand(
                command="stop",
                description="Stops Playing"
            ),
            types.BotCommand(
                command="radio",
                description="Start radio / Live stream"
            ),
            types.BotCommand(
                command="stopradio",
                description="Stops radio/Livestream"
            ),
            types.BotCommand(
                command="replay",
                description="Replay from beggining"
            ),
            types.BotCommand(
                command="clean",
                description="Cleans RAW files"
            ),
            types.BotCommand(
                command="pause",
                description="Pause the song"
            ),
            types.BotCommand(
                command="resume",
                description="Resume the paused song"
            ),
            types.BotCommand(
                command="mute",
                description="Mute in VC"
            ),
            types.BotCommand(
                command="volume",
                description="Set volume between 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="Unmute in VC"
            ),
            types.BotCommand(
                command="restart",
                description="Restart the bot"
            )
        ]
    )
)

idle()
bot.stop()
