from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 6934572688
bot_user = "Nike_subot"
api_id = 27866094
api_hash = "b7a7ebdb70d10917a028b033c999e77d"
session = "1BJWap1sBu3jNo1iqLssDFjt3tYMQ-xvtrzlLzmIZZYQDTFlg9KJoRjtEWF0fQs0BX-sd_8K0zE-UjsmiWM4XnAzDDTQi2Yx4C1TzvRKVkacaLHrQdgahnYWVmJpPX34cWNg3de-ecH_Q5gLmdVSpx4DmGiR9ogpIS8OSx9NK_U94w_eqaDTwyKPDY3NzepT7LXHr15zjBd4otEHKyGuRUg-LALfme3cGK3oyv4Kwks3rZkkFuLVuZEXTp5vvlYCVzZ_RWrVaXht6wow8cSKHiCh8SRcwvHgNTXXeJRIv92LGlnp5ROmmlEgaUd-ifyGsLixBJ2kaKWFzOkdLa1f4YRwSTft44sU="
token = "6909609612:AAEhyk_eRE-DdKOt8dLtsTYu8TbUhXiKlwg"
sudo_command = [6934572688, 6934572688]
pm = "6934572688"
mention = "6934572688"
plugins = dict(root="plugins")
app = Client("user:Nike_subot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Nike_subot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
