import os
import telegram.ext as tg
from pyrogram import Client
import logging  
from telegram.ext import Application

from motor.motor_asyncio import AsyncIOMotorClient
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

### ❖ ➥
OWNER_ID = os.getenv("OWNER_ID", "8364692780")

### ❖ ➥
SUDO_USERS = os.getenv("SUDO_USERS", "8558024747").split()

### ❖ ➥
LOGGER_ID = os.getenv("LOGGER_ID", "-1003882647583")

### ❖ ➥
BOT_USERNAME = os.getenv("BOT_USERNAME", "nykaa_waifubot")

### ❖ ➥
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

### ❖ ➥
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

### ❖ ➥
IMG_URL = os.getenv("IMG_URL", "https://files.catbox.moe/376q7n.jpg").split()

### ❖ ➥
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/theinfinity_support")

### ❖ ➥
CHANNEL_ID = os.getenv("CHANNEL_ID", "-1003729074782")

### ❖ ➥
API_HASH = os.getenv("API_HASH", "aed61e5ff8c711895f8b0c99e51c16cc")

### ❖ ➥
API_ID = os.getenv("API_ID", "39679517")

### ❖ ➥
UPDATE_CHAT = os.getenv("UPDATE_CHAT", "")

application = Application.builder().token(BOT_TOKEN).build()
ROY = Client(
    "lmao",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    
    
)
client = AsyncIOMotorClient(MONGO_URL)
db = client['Character_catcher']
collection = db['anime_characters_lol']
user_totals_collection = db['user_totals_lmaoooo']
user_collection = db["user_collection_lmaoooo"]
group_user_totals_collection = db['group_user_totalsssssss']
top_global_groups_collection = db['top_global_groups']
pm_users = db['total_pm_users']


