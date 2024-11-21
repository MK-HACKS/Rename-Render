# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21426131")

API_HASH = os.environ.get("API_HASH", "4cf9334de5ee97801a8d1797ab37f770")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7668127487:AAE5PSgl1kKUrsDClNl3rxHSMRRbr8VtCRI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "NewLatestMoviesFiles") 

DB_NAME = os.environ.get("DB_NAME", "MKFileRenamerBot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mp1884199:e7v95NMJ7OaX9FQl@cluster0.35yp4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6923298010').split()]

PORT = os.environ.get("PORT", "8080")
