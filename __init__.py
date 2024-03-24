#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "12606917" #config("API_ID", default=None, cast=int)
API_HASH = "f25113b8c17dca6fa7abda53a86bd4f7" #config("API_HASH", default=None)
BOT_TOKEN = "6553567194:AAHFoJ7y9fT-z12_-S_6HVDz9Bqz5vdIta8" #config("BOT_TOKEN", default=None)
SESSION = "AQDAXcUAMQ_OTXH9wWjOrGR8KTNb0G8q95M5_DWvAuKFh8GFlHBpDlQZkN7OlG5RZ7NRN171f0WNB5TCXJ3aO5jMWdUBLsDrt3gcZ8hjCvR1IUUF_GXFShdVwUdDeqe0ZzQSqzzNwrdGTN16gcV5x5pnRDMM94x-ziJ8UN-Gf8knOTHXMSB-kbKbGp890fiV31A_s8iBR3_e_OeUxDLvxc4Rz6DvukeTwch3VQnc6dnVqze8jj_5K8ydRyb1ccoDWiSIY5sqkdmS_msTkyjnBULDfvEG97NREdGvLtEyspLync4fIVSRc5_YZ4iTDl-0x7GYCRjDCxjI0UKnWLdsZWosK5jPbwAAAAE8_fPSAA"  #config("SESSION", default=None)
FORCESUB = "backup98jdj" #config("FORCESUB", default=None)
AUTH = "5318243282" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
