from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "7382535660:AAF1W3s_g1NhQlqr_d4uFrhaByj5Nq7H-Fk"
    SUDOERS = [6996341586]
    NSFW_LOG_CHANNEL = -1002227725928
    SPAM_LOG_CHANNEL = -1002214254535
    ARQ_API_KEY = "EEQDKW-JSNCHU-YOZPVF-KOBPGR-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
