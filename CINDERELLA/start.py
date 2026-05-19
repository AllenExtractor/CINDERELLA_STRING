from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://graph.org/file/3f0529e0a232d7a076a60-998260a13c34d2b7ea.jpg",
        caption=f"""✦ » ʜᴇʏ🫣  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᴠͥɪͣᴘͫ𝗖𝘂𝗧𝗲♡𝗡𝗮𝘄𝗮𝗮𝗯𝗭𝗮𝗱𝗮𓆩♛𓆪](https://t.me/SmartBoy_ApnaMS) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔸 sᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/Cinderella_Support"),
                    InlineKeyboardButton("▫️ ᴜᴘᴅᴀᴛᴇs▫️", url="https://t.me/teamcinderella")
                ],
                [
                    InlineKeyboardButton("🔸 𝑪𝒐𝒏𝒕𝒂𝒄𝒕 🔸", url="https://t.me/CinderellaContactBot"),
                    InlineKeyboardButton("▫️𝐏𝐃𝐅 𝐫𝐞𝐧𝐚𝐦𝐞▫️", url="https://t.me/Cinderella_renameBot")
                ]                
            ]
        )
    )
