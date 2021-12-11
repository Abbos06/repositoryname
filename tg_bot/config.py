class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "5018845036:AAEIYk-v62xDDaVNLj-QBdLzRiSLnYUQSNg"
    OWNER_ID = "607453263" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Abbos20182583"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sql://cloudcomputing:litsey316@database-3.cirlskqjtc1k.ap-northeast-2.rds.amazonaws.com:3306/dbname'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
