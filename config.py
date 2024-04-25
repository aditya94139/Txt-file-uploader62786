import os

API_ID = API_ID = 23163380

API_HASH = os.environ.get("API_HASH", "2dca155e786c7db2d295e5b4ab10783b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6682851684:AAF0DKe7uCi8Zs084IsvDtgvvc8l0YmYAII")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5827915041))

LOG = -1001907859284,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5827915041").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


