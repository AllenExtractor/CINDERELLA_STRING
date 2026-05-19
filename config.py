from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "33853339"))
API_HASH = getenv("API_HASH", "d44e3a158d9da849df318173268f94c0")

BOT_TOKEN = getenv("BOT_TOKEN", " ")
OWNER_ID = int(getenv("OWNER_ID", "8715662594"))

MONGO_DB_URI = getenv("mongodb+srv://m49606145_db_user:Th15V5nu9utMejwO@cluster0.g11tftt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0.")
MUST_JOIN = getenv("MUST_JOIN", "teamcinderella")
