# Innexia Music

- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.
- A Telegram Bot to Play Audio in Voice Chats With Youtube and Deezer support.
- Supports Live streaming from YouTube.

---

## Deploy To Railway
[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/MrSammyXD/music&envs=API_ID,API_HASH,BOT_TOKEN,ARQ_API,SESSION_STRING,CHAT,LOG_GROUP,ADMINS,ADMIN_ONLY,MAXIMUM_DURATION,STREAM_URL,REPLY_MESSAGE )

___

## NOTE:

- Make sure you have started a VoiceChat in your Group before deploying.

---


## Variables
<details>
  <summary><b>See Variables</b></summary>
<br/>

### Pre Requisites 
- `API_ID` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UsetTGzKBot](https://telegram.dog/UseTGzKBot)
- `API_HASH` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot)
- `BOT_TOKEN` : Get From [@Botfather](https://telegram.dog/BotFather)
- `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@TcBots/TcPlayerBot#main.py)
- `CHAT` : ID of Channel/Group where the bot plays Music.
- `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
- `ADMINS` : ID of users who can use admin commands.
- `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
- `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command. Some Streaming Links [Click here.](https://t.me/SiderzBot)
- `MAXIMUM_DURATION` : Maximum duration of song to play.(Optional)
- `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 
- `ADMIN_ONLY` : Pass `Y` If you want to make /play and /deezer commands only for admins of `CHAT`. By default `N` /play and /deezer is available for all.

</details>

---

## Deploy Now

<details><summary><b>Deploy to Heroku</b></summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/DarkCyberS/InnexiaMusic">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">

<a href="https://youtu.be/FKaAU4Pr2bw"><img src="https://img.shields.io/badge/How%20to%20Deploy%20on%20Heroku-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/FKaAU4Pr2bw"><img src="https://img.shields.io/youtube/views/FKaAU4Pr2bw?style=social">
</a>
</p>
</details>

<details>
  <summary><b>Deploy on Qovery</b></summary>
<br/>

<p align="left">
<a href="https://console.qovery.com">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20to%20Qovery-blueviolet?style=for-the-badge&logo=qovery">
  </a>
</p>

<a href="https://youtu.be/KC4YdpDGQKg"><img src="https://img.shields.io/badge/How%20to%20Deploy%20on%20Qovery-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/KC4YdpDGQKg"><img src="https://img.shields.io/youtube/views/KC4YdpDGQKg?style=social">
</a>
</p>

</details>

<details>
  <summary><b>Deploy in your VPS</b></summary>
<br/>

```sh
git clone https://github.com/DarkCyberS/InnexiaMusic
cd VCMusicPlayer
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```

</details>

---



#### Support
Join Now Telegram [Innexia Music Live Sets](https://t.me/SiderzBot?voicechat)



## Credits

- [Zaute Km](https://github.com/ZauteKm) 
- [Mr Sammy](https://github.com/MrSammyXD) 
- [SiderZ](https://t.me/BotDevlopers)
