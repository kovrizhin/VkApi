from os import wait
from time import sleep
import vk_auth
import json
import urllib2
from urllib import urlencode
import json
import os
import os.path
import getpass
import sys

def call_api(method, params, token):
    if isinstance(params, list):
        params_list = [kv for kv in params]
    elif isinstance(params, dict):
        params_list = params.items()
    else:
        params_list = [params]
    params_list.append(("access_token", token))
    url = "https://api.vk.com/method/%s?%s" % (method, urlencode(params_list))
    return json.loads(urllib2.urlopen(url).read())["response"]

def get_chathistory(user_id, token, startId, len):
    return call_api("messages.getHistory", [("uid", "163769"), ("offset", startId), ("count", len)], token)

email = ""
password = ""
token, user_id = vk_auth.auth(email, password, "3714507", "messages")

loop = True
i = 0;
result = []
while loop:
    chathistory = get_chathistory(user_id, token, i, 200)
    i +=200
    if((len(chathistory) == 1) & (chathistory[0] == 13041)):
        loop = False
    else:
        result += chathistory[1::]
        sleep(0.3)
        print "\n len " + str(len(chathistory))
        print "\ncount: " + str(i)


parseHistory = list((str((history[1])["from_id"]), (history[1])["body"]) for history in enumerate(result))
print len(result)






