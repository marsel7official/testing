from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo_handler(client, message):
    buttons = [[
        InlineKeyboardButton(text="Bright", callback_data="bright"),
        InlineKeyboardButton(text="Mix", callback_data="mix"),
        InlineKeyboardButton(text="B & W", callback_data="b|w"),
        ],[
        InlineKeyboardButton(text="Circle", callback_data="circle"),
        InlineKeyboardButton(text="Blur", callback_data="blur"),
        InlineKeyboardButton(text="Border", callback_data="border"),
        ],[
        InlineKeyboardButton(text="🍡Stick", callback_data="stick"),
        InlineKeyboardButton(text="Rotate", callback_data="rotate"),
        InlineKeyboardButton(text="Contrast", callback_data="contrast"),
        ],[
        InlineKeyboardButton(text="Sepia", callback_data="sepia"),
        InlineKeyboardButton(text="Pencil", callback_data="pencil"),
        InlineKeyboardButton(text="Cartoon", callback_data="cartoon"),
        ],[
        InlineKeyboardButton(text="Inverted", callback_data="inverted"),
        InlineKeyboardButton(text="Glitch", callback_data="glitch"),
        InlineKeyboardButton(text="Remove BG", callback_data="removebg"),
        ],[
        InlineKeyboardButton(text="Close",( callback_data="close_data"),
    ]]
    try:
        await message.reply(text="Select Your Required Mode From Below", quote=True, reply_markup=InlineKeyboardMarkup(buttons))            
    except Exception as e:
        print(e)
        if "USER_IS_BLOCKED" in str(e): return           
        try: await message.reply_text(f"{e} \nSomething Went Wrong!", quote=True)
        except Exception: return
