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

def get_songs(user_id, token):
    return call_api("audio.get", ("oid", user_id), token)

def save_music(songList, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    for song in enumerate(songList[1::]):
        file = (song[1])["artist"]+" - " + (song[1])["title"];
        file = file.replace("/", "")
        filename = os.path.join(directory, ( file+ ".mp3"))
        if not os.path.exists(filename):
            print "Downloading %s" % filename
            open(filename, "w").write(urllib2.urlopen((song[1])["url"]).read())
        else:
           print "Exist %s" % filename

directory = raw_input("File Directory: ")
# email = raw_input("Email: ")
# password = getpass.getpass()
email = "o.v.kovrizhin@gmail.com"
password = "kovrizhka11"
token, user_id = vk_auth.auth(email, password, "3714507", "audio")
oid = raw_input("Please enter userId or grope Id, feel free if you want download music from your profile:\n")
if oid == "":
    oid = user_id
songsList = get_songs(oid, token)
save_music(songsList, directory)
