class script(object):
    START_TXT = """𝖧𝖾𝗅𝗅𝗈 {},
𝖬𝗒 𝖭𝖺𝗆𝖾 𝖨𝗌 <a href='https://t.me/Sakurafilterbot'>𝖲𝖺𝗄𝗎𝗋𝖺</a>,𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 𝖠𝗅𝗌𝗈 , 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗇𝖽 𝖬𝖺𝗄𝖾 𝖬𝖾 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇📍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: 𝚂𝙰𝙺𝚄𝚁𝙰
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href='https://t.me/PaulWalker_TG'>𝙿𝚊𝚞𝚕𝚆𝚊𝚕𝚔𝚎𝚛 🇱🇷</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: <a href='https://MongoDB.com'>𝙼𝙾𝙽𝙶𝙾 𝙳𝙱</a>
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href='https://qovery.com'>𝚀𝙾𝚅𝙴𝚁𝚈</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [BETA]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Sakura is a closed source project.   

<b>DEVS:</b>
- <a href='https://t.me/PaulWalker_TG'>𝙿𝚊𝚞𝚕𝚆𝚊𝚕𝚔𝚎𝚛</a>

CODES:
1. Auto Filter
2. Group Managing  
"""
    BAN_TXT = """<b>Bans:</b>
Some people need to be publicly banned; spammers, annoyances, or just trolls.

<b>Admin commands:</b>
- /ban - Ban a user
- /tban - Temporarily ban a user.
Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
- /unban - Unban a user

<b>Example:</b>
- Ban a user for two hours
-> /tban @username 2h

Made By @SakuraBotUpdates ❤️
"""
    PING_TXT= """<b>Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

- /alive - To check you are alive.
- /help - To get help 
- /ping - To get your ping 

<b>Usage :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features 

Made by @SakuraBotUpdates ❤️
"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json

<b>Features:</b>
Message Editting JSON
Pm Support
Group Support

<b>Note:</b>
Everyone can use this command , if spaming happens bot will automatically ban you from the group

Made By @SakuraBotUpdates ❤️
"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>🎲 NOTHING MUCH JUST SOME FUN THINGS</b>
t𝗋𝗒 𝗍𝗁𝗂𝗌 𝖮𝗎𝗍: 
𝟣. /dice - Roll The Dice 
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat 
3. /Runs - Jokes In Malayalam ( Not Really Jokes, But Feel Free To Use)

Made By @SakuraBotUpdates ❤️
"""
    PURGE_TXT ="""<b>Purge</b>
    
    Delete A Lot Of Messages From Groups! 
    
    <b>ADMIN</b> 
    
    ◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message

Made By @SakuraBotUpdates ❤️
    """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

-  𝙸𝚏 𝚈𝚘𝚞 𝙳𝚘𝚗'𝚝 𝚆𝚊𝚗𝚝 𝚃𝚠𝚘 𝙱𝚘𝚝 𝚄𝚜𝚎 𝙼𝚊𝚗𝚞𝚊𝚕 𝙵𝚒𝚕𝚝𝚎𝚛 𝙵𝚘𝚛 𝙵𝚒𝚕𝚝𝚎𝚛𝚒𝚗𝚐 𝚆𝚎𝚋𝚜𝚎𝚛𝚒𝚎𝚜

<b>NOTE:</b>
1. 𝚂𝚊𝚔𝚞𝚛𝚊 𝚂𝚑𝚘𝚞𝚕𝚍 𝙽𝚎𝚎𝚍 𝙰𝚍𝚖𝚒𝚗 𝙿𝚛𝚒𝚟𝚒𝚕𝚊𝚐𝚎 𝚃𝚘 𝚆𝚘𝚛𝚔 
2. 𝙾𝚗𝚕𝚢 𝙰𝚍𝚖𝚒𝚗𝚜 𝙲𝚊𝚗 𝚄𝚜𝚎 𝙵𝚒𝚕𝚝𝚎𝚛 
3. 𝙰𝚕𝚎𝚛𝚝 𝙱𝚞𝚝𝚝𝚘𝚗𝚜 𝙷𝚊𝚟𝚎 𝙻𝚒𝚖𝚒𝚝𝚜 𝙱𝚞𝚝 𝙳𝚘𝚗'𝚝 𝙲𝚊𝚛𝚎 

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>

Made By @SakuraBotUpdates ❤️
"""
    MUTE_TXT = """<b>𝖬𝗎𝗍𝖾:</b>

𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 Muted; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   

<b>🔞 𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:</b>

- /mute - 𝖬𝗎𝗍𝖾 𝖠 𝖴𝗌𝖾𝗋 
- /tmute - 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unmute - 𝖴𝗇mute 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
 - 𝖬𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tmute @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁

Made By @SakuraBotUpdates ❤️
"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Sakura Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Sakura supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Sakurabotupdates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

Made By @SakuraBotUpdates ❤️
"""
    AUTOFILTER_TXT = """<b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.

Made By @SakuraBotUpdates ❤️
"""
    CONNECTION_TXT = """<b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>

Made By @SakuraBotUpdates ❤️
"""
    FILTER_TXT ="""𝚂𝙴𝙻𝙴𝙲𝚃 𝙰 𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚈𝙿𝙴 𝙱𝙴𝙻𝙾𝚆:"""
    PIN_TXT = """<b> Pin :- </b>

All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!

<b>📚 Commands & Usage:</b>

◉ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

◉ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message

Made By @SakuraBotUpdates ❤️
"""
    TGRAPH_TXT ="""<b>HELP: Telegraph</b>

Do as you wish with telegra.ph module!

<b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

NOTE:
• Sakura should have admin privillage.
• This Command Is Available in goups and pms
• This Command Can be used by everyone

Made By @SakuraBotUpdates ❤️
"""
    IMBD_TXT ="""<b>Search</b>

Search anything without leaving telegram!

USAGE:
➥ /imdb - get the film information from IMDb source
➥ /search - get the film information from various sources

Made By @SakuraBotUpdates ❤️
"""
    INFO_TXT ="""<b>Info</b>

Get information about something!

USAGE:
➥ /id - get the id of a specifed user
➥ /info - get the information about a user

<b>NOTE:</b>
• Sakura should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

Made By @SakuraBotUpdates ❤️
"""
    EXTRAMOD_TXT = """<b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>

Made By @SakuraBotUpdates ❤️
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /index  - <code>to add files from a channel</code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
