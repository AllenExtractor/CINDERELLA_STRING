import os
import threading
import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen
from flask import Flask
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

# Initialize start time
StartTime = time.time()

# Initialize the Client
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="CINDERELLA"),
)

# ─── Flask keep-alive server for Render ───────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Bot is running.!'

def run_flask():
    port = int(os.environ.get("PORT", 8000))
    flask_app.run(host="0.0.0.0", port=port)

# Start Flask in background thread so Render detects open port
threading.Thread(target=run_flask, daemon=True).start()
# ─────────────────────────────────────────

if __name__ == "__main__":
    print("𝐂𝐢𝐧𝐝𝐞𝐫𝐞𝐥𝐥𝐚 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠....")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(f"@{uname} NOW CINDERELLA SESSION GEN IS READY TO GEN SESSION")
    
    idle()
    app.stop()
    print("𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐒𝐭𝐨𝐩𝐩...")
