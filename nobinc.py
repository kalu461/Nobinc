#!/usr/bin/env python3
"""
🔓 DECRYPTED BY AMAN DADDY 👑
Original RC4 encrypted payload from pratham_1764519748999.py
Decrypted and open-sourced for educational purposes
⚡ Made by AMAN DADDY
"""

import asyncio, json, os, random, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# ---------------------------
# CONFIGURATION - EDIT HERE
# ---------------------------
OWNER_ID = 5915051224  # YOUR TELEGRAM ID
TOKENS = [
    "8366785937:AAGIiR80rjzuSkB7OtNc4ztNsHPg2EPBuaM",
    "8556107583:AAEeLtccZXOVl08vETDj4BLT71nnRGoLGL4",
    "8423318697:AAGxg1WdnOMk9MzZHhJPmwVXq5gXPrZkgRM",
    "8545027440:AAGTOQ3HvLepTsDTTvvl_9N5KtYwS0jwzwM",
    "8135497087:AAFm6hpcDMiYn-Zm-8GFq2rQLSA2X4EOgS8",
    "8460058132:AAGF62ahgM07bib5Kc-pZCOQxkkiRME0EQo",
    "8384337128:AAF20lPFWcTTKtvjV56OMT-8YDigelTEJxE",
    "8372572857:AAFi3gCPNIwJ4iD6QJsnNiJ22AhBg40Q_pQ",
    "8580311855:AAEuC-IGIuD-6UK8OpB7H8ePZ5h1TZVEqTc",
    "8519232314:AAEV4BQ5L2FZRsAaGIZtIW8k75xMygs_5OE",
    "8438070958:AAH9kAHj3kdNRifTLZsCpIClKqAdU2vl-x8",
    "8503929519:AAF_x1rFQZ9MMxYK2Y76dodNBIRDLC2iWf0",
    "8568976147:AAErWHmmRCWZzWJTZ0Ruv1Nw3CKrVT4sacQ",
    "8286703321:AAFDTA2iyHctSsHeSVafypsGywKwjI7x0nU",
]

NCEMO_EMOJIS = ["🔥","⚡","💥","💀","🕊","💫","🌪","🐉","👑","🌟","💎","🎭","🚀","✨","🔮",
 "🎯","🌀","🐺","🦅","🐍","🎇","🎆","💠","💣","🧨","🎉","🎊","🌈","🌊","🌙",
 "⭐","🌞","🌝","🌛","🌚","☄️","🌋","🏆","🥇","🎖️","🏅","🎗️","🏵️","🌺","🌸",
 "🌼","🌻","🌹","⚓","🛡️","⚔️","🪄","🧿","🪶","🕹️","🎮","🎲","🧩","🎵","🎶",
 "🎼","🎧","🎤","🎷","🎸","🎺","🥁","📯","📀","📣","📯","🛸","🛰️","🏹","🗡️",
 "🛡️","🩸","⚗️","🔭","🔬","💉","🧪","📚","📖","📝","✒️","🖋️","🖊️","✏️","📐",
 "📏","🧭","🔧","⚙️","🔩","🧱","🏗️","🏛️","🧭","🗺️","🧭","🔔","🔕","💡","🔦"]

SUDO_FILE = "sudo.json"

# ---------------------------
# RAID TEXTS
# ---------------------------
RAID_TEXTS = [
    "",
    "Cʜᴜᴅ Tʀʏ Mᴀᴀ Kᴀ  भोसड़ा⚡",
    "Cʜᴀʟ 2 Kᴏᴅɪ Kᴇ Pɪʟʟᴇ ⚡",
    "चूद Gʏᴀ -!⚡",
    "Tʀʏ मां रंडल⚡",
    "Kᴜᴛɪʏᴀ Kᴇ Lᴀᴅᴋᴇ⚡",
    "Cʜᴏᴛɪ Jᴀᴀᴛ Kᴇ पिल्ले⚡",
    "Jᴇʙ Kᴀᴛʀᴇ Kᴇ ʟᴀᴅᴋᴇ⚡",
    "Kᴜᴛᴛɪ Mᴀᴀ Kᴇ Bᴇᴛᴇ⚡",
    "Cʜᴜᴅ Kᴀʀ गायब Hᴏᴊᴀ ⚡",
    "Cʜᴜᴘ रंडीके Nᴇᴡ Gᴇɴ⚡",
    "Sᴏʀʀʏ Bᴏʟᴅᴇ माफ करदूंगा!⚡",
    "Cʜᴀʟ Aʙʜ Mᴀᴀ Cʜᴜᴅᴀ⚡",
    "Tᴇʀɪ Dᴀᴅɪ Mᴇʀɪ Fᴀɴ⚡",
    "Tʀᴀ Bᴀᴀᴘ Bʜɪᴋᴍᴀɴɢᴀ⚡",
]


# ---------------------------
# GLOBAL STATE
# ---------------------------
if os.path.exists(SUDO_FILE):
    try:
        with open(SUDO_FILE, "r") as f:
            _loaded = json.load(f)
            SUDO_USERS = set(int(x) for x in _loaded)
    except Exception:
        SUDO_USERS = {OWNER_ID}
else:
    SUDO_USERS = {OWNER_ID}
with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)

def save_sudo():
    with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)

group_tasks = {}         
slide_targets = set()    
slidespam_targets = set()
swipe_mode = {}
apps, bots = [], []
delay = 1

logging.basicConfig(level=logging.INFO)

# ---------------------------
# DECORATORS
# ---------------------------
def only_sudo(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id
        if uid not in SUDO_USERS:
            return await update.message.reply_text("⛔ You are not Owner.")
        return await func(update, context)
    return wrapper

def only_owner(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id
        if uid != OWNER_ID:
            return await update.message.reply_text("⛔ Only Owner can do this.")
        return await func(update, context)
    return wrapper

# ---------------------------
# LOOP FUNCTION
# ---------------------------
async def bot_loop(bot, chat_id, base, mode):
    i = 0
    while True:
        try:
            if mode == "raid":
                text = f"{base} {RAID_TEXTS[i % len(RAID_TEXTS)]}"
            else:
                text = f"{base} {NCEMO_EMOJIS[i % len(NCEMO_EMOJIS)]}"
            await bot.set_chat_title(chat_id, text)
            i += 1
            await asyncio.sleep(delay)
        except Exception as e:
            print(f"[WARN] Bot error in chat {chat_id}: {e}")
            await asyncio.sleep(2)

# ---------------------------
# COMMANDS
# ---------------------------
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "𓆩𓆩⃟⚡𝐍𝐎𝐁𝐈𝐗 ~ भगवान हूँ - 🔱 ⃟𓆪𓆪\n"
        "Use /help to see all commands."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "𓆩𓆩⃟⚡ NOBI TG FIGHT SCRIPT — HELP MENU ⚡⃟𓆪𓆪\n"
        "───────────────────────────────\n\n"

        "💨 𝐆𝐂 𝐋𝐎𝐎𝐏𝐒\n"
        "⚡ /gcnc <text>\n"
        "⚡ /stopgcnc\n"
        "⚡ /stopall\n"
        "⚡ /delay <sec>\n"
        "⚡ /status\n\n"

        "💨 𝐒𝐔𝐃𝐎 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓\n"
        "⚡ /addsudo (reply)\n"
        "⚡ /delsudo (reply)\n"
        "⚡ /listsudo\n\n"

        "💨 𝐀𝐁𝐎𝐔𝐓\n"
        "⚡ /myid\n"
        "⚡ /ping\n\n"

        "💨 𝐎𝐖𝐍𝐄𝐑\n"
        "━━━━━━━━━━━━━━━\n"
        "@scary_godz\n"
        "━━━━━━━━━━━━━━━"
    )

async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_time = time.time()
    msg = await update.message.reply_text("☄️ Pinging...")
    end_time = time.time()
    latency = int((end_time - start_time) * 1000)
    await msg.edit_text(f" here 🍁 {latency} ms")

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🧸 ID: {update.effective_user.id}")

# --- GC Loops ---
@only_sudo
async def gcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: return await update.message.reply_text("Usage: /gcnc <text>")
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    group_tasks.setdefault(chat_id, {})
    for bot in bots:
        if bot.id not in group_tasks[chat_id]:
            task = asyncio.create_task(bot_loop(bot, chat_id, base, "raid"))
            group_tasks[chat_id][bot.id] = task
    await update.message.reply_text(" 🌀 GC name loop started with raid texts.")

@only_sudo
async def ncemo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: return await update.message.reply_text(" Usage: /ncemo <text>")
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    group_tasks.setdefault(chat_id, {})
    for bot in bots:
        if bot.id not in group_tasks[chat_id]:
            task = asyncio.create_task(bot_loop(bot, chat_id, base, "emoji"))
            group_tasks[chat_id][bot.id] = task
    await update.message.reply_text(" Emoji loop started with all bots.")

@only_sudo
async def stopgcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in group_tasks:
        for task in group_tasks[chat_id].values():
            task.cancel()
        group_tasks[chat_id] = {}
        await update.message.reply_text(" Loop stopped in this GC.")

@only_sudo
async def stopall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for chat_id in list(group_tasks.keys()):
        for task in group_tasks[chat_id].values():
            task.cancel()
        group_tasks[chat_id] = {}
    await update.message.reply_text(" All loops stopped.")

@only_sudo
async def delay_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global delay
    if not context.args: return await update.message.reply_text(f"⏱ Current delay: {delay}s")
    try:
        delay = max(0.5, float(context.args[0]))
        await update.message.reply_text(f" Delay set to {delay}s")
    except: await update.message.reply_text(" Invalid number.")

@only_sudo
async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Active Loops:\n"
    for chat_id, tasks in group_tasks.items():
        msg += f"Chat {chat_id}: {len(tasks)} bots running\n"
    await update.message.reply_text(msg)

# --- SUDO ---
@only_owner
async def addsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        SUDO_USERS.add(uid); save_sudo()
        await update.message.reply_text(f" {uid} added as sudo.")

@only_owner
async def delsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        if uid in SUDO_USERS:
            SUDO_USERS.remove(uid); save_sudo()
            await update.message.reply_text(f"{uid} removed from sudo.")

@only_sudo
async def listsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" SUDO USERS:\n" + "\n".join(map(str, SUDO_USERS)))

# --- Slide / Spam / Swipe ---
@only_sudo
async def targetslide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slide_targets.add(update.message.reply_to_message.from_user.id)
        await update.message.reply_text(" Target slide added.")

@only_sudo
async def stopslide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        slide_targets.discard(uid)
        await update.message.reply_text("Target slide stopped.")

@only_sudo
async def slidespam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slidespam_targets.add(update.message.reply_to_message.from_user.id)
        await update.message.reply_text(" Slide spam started.")

@only_sudo
async def stopslidespam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slidespam_targets.discard(update.message.reply_to_message.from_user.id)
        await update.message.reply_text("🐠Slide spam stopped.")

@only_sudo
async def swipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: return await update.message.reply_text("Usage: /swipe <name>")
    swipe_mode[update.message.chat_id] = " ".join(context.args)
    await update.message.reply_text(f" Swipe mode ON with name: {swipe_mode[update.message.chat_id]}")

@only_sudo
async def stopswipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    swipe_mode.pop(update.message.chat_id, None)
    await update.message.reply_text(" Swipe mode stopped.")

# --- Auto Replies ---
async def auto_replies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid, chat_id = update.message.from_user.id, update.message.chat_id
    if uid in slide_targets:
        for text in RAID_TEXTS: await update.message.reply_text(text)
    if uid in slidespam_targets:
        for text in RAID_TEXTS: await update.message.reply_text(text)
    if chat_id in swipe_mode:
        for text in RAID_TEXTS: await update.message.reply_text(f"{swipe_mode[chat_id]} {text}")

# ---------------------------
# BUILD APP & RUN
# ---------------------------
def build_app(token):
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(CommandHandler("gcnc", gcnc))
    app.add_handler(CommandHandler("ncemo", ncemo))
    app.add_handler(CommandHandler("stopgcnc", stopgcnc))
    app.add_handler(CommandHandler("stopall", stopall))
    app.add_handler(CommandHandler("delay", delay_cmd))
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(CommandHandler("addsudo", addsudo))
    app.add_handler(CommandHandler("delsudo", delsudo))
    app.add_handler(CommandHandler("listsudo", listsudo))
    app.add_handler(CommandHandler("targetslide", targetslide))
    app.add_handler(CommandHandler("stopslide", stopslide))
    app.add_handler(CommandHandler("slidespam", slidespam))
    app.add_handler(CommandHandler("stopslidespam", stopslidespam))
    app.add_handler(CommandHandler("swipe", swipe))
    app.add_handler(CommandHandler("stopswipe", stopswipe))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_replies))
    return app

async def run_all_bots():
    global apps, bots
    for token in TOKENS:
        if token.strip():
            try:
                app = build_app(token)
                apps.append(app); bots.append(app.bot)
            except Exception as e:
                print("Failed building app:", e)

    for app in apps:
        try:
            await app.initialize(); await app.start(); await app.updater.start_polling()
        except Exception as e:
            print("Failed starting app:", e)

    print(" TOOL HAS BEEN STARTED BY PRATHAM (all bots started).")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_all_bots())
