from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt=f"Hello {msg.from_user.mention} I am simple rename bot this bot is made by Prime Hritu\n\n✓ Send Me `/rename [filename.extension]` With Reply To A File. [ Replace [filename.extension] with The New Filename and its .extension (.jpg , .png , .jpeg , .mp3 , .mp4 , etc....)]"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("Developer 🇮🇳", url="https://t.me/Prime_Hritu")
        ],[
        InlineKeyboardButton("Updates Channel 🇮🇳", url="https://t.me/Private_Bots")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Hello {msg.from_user.mention} I am simple rename bot
this bot is made by Prime Hritu

✓ Send Me `/rename [filename.extension]` With Reply To A File. [ Replace [filename.extension] with The New Filename and its .extension (.jpg , .png , .jpeg , .mp3 , .mp4 , etc....)]"                                     
    button= [[
        InlineKeyboardButton("Updates Channel 🇮🇳", url="https://t.me/Private_Bots")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ],
        InlineKeyboardButton("⭐ Rate", callback_data="rate")]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Prime_Hritu>𝙃𝙧𝙞𝙩𝙪</a> & <a href=https://t.me/Prime_venom>𝙑𝙚𝙣𝙤𝙢</a>"  
    Manager="<a href=https://t.me/Prime_Hritu>𝙃𝙧𝙞𝙩𝙪</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://t.me/Prime_Hritu>𝙃𝙧𝙞𝙩𝙪</a>\nBot Updates: <a href=https://t.me/Private_Bots>𝙋𝙍𝙄𝙑𝘼𝙏𝙀 𝘽𝙊𝙏𝙎</a>\nMy Master's: {Master}\nManger: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex("rate"))
async def rate(bot, msg):
    txt = "**Click On Rate Here And Rate Me And My Works 👍**"
    button= [[        
        InlineKeyboardButton("Rate Me ⭐", url="https://t.me/Rate_Here/10"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)

@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


