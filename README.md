# UltroidAddons
Plugins repository for [@TheUltroid](https://github.com/TeamUltroid/Ultroid).

# Contributing
If you want to contribute to this repository (adding your plugins/porting from other bots), use the below format and create a pull request.   
⚠️ First check whether the stuff you push works. Also, if the pull request doesn't follow the below format, it will be closed without notice.

```
# Credits @username (creator of plugin and who ported)   
   
# Ported from (if ported else skip)   
   
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >   
```
   
Kindly do not steal others works without credits.<br>

# Example Plugin
   Required Import are Automatically Done.
   
```python3
@ultroid_cmd(pattern="hi")
   async def hello_world(event):
       await event.reply("Hello World")
```

<br>

> Made with 💕 by [@TeamUltroid](https://t.me/TeamUltroid).
