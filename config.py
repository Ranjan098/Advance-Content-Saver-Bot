from os import environ 

class Config:
    API_ID = environ.get("API_ID", "12606917")
    API_HASH = environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6553567194:AAHFoJ7y9fT-z12_-S_6HVDz9Bqz5vdIta8") 
    BOT_SESSION = environ.get("BOT_SESSION", "AQDAXcUAMQ_OTXH9wWjOrGR8KTNb0G8q95M5_DWvAuKFh8GFlHBpDlQZkN7OlG5RZ7NRN171f0WNB5TCXJ3aO5jMWdUBLsDrt3gcZ8hjCvR1IUUF_GXFShdVwUdDeqe0ZzQSqzzNwrdGTN16gcV5x5pnRDMM94x-ziJ8UN-Gf8knOTHXMSB-kbKbGp890fiV31A_s8iBR3_e_OeUxDLvxc4Rz6DvukeTwch3VQnc6dnVqze8jj_5K8ydRyb1ccoDWiSIY5sqkdmS_msTkyjnBULDfvEG97NREdGvLtEyspLync4fIVSRc5_YZ4iTDl-0x7GYCRjDCxjI0UKnWLdsZWosK5jPbwAAAAE8_fPSAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5318243282').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
