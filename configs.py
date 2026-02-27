# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "33164428"))
    API_HASH = getenv("API_HASH", "4676ee8c4390d66a46daded67fba8429")
    BOT_TOKEN = getenv("BOT_TOKEN", "8317794667:AAELWrhAjdiA8-HL3c-0KUS1o6N1TEFns_I")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "1002234198300")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6797167274").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://shanu2001:<db_password>@cluster0.uibf8on.mongodb.net/?appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
