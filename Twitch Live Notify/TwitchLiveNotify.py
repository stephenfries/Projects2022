 ######## Created By: Stephen Fries, 2/6/22 ########
######### TWITCH LIVE NOTIFY + DISCORD BOT #########


import os, requests, time                                                                   #               IMPORTS TO ALLOW FOR DISCORD/TWITCH API                     #
from dotenv import load_dotenv                                                              #           dotenv allows loading hidden files for secrets                  #
from discord.ext import commands                                                            # pip install discord.py | pip install python-dotenv | pip install requests #

load_dotenv('clientID.env')
id = os.getenv('client_id')
load_dotenv('clientSecret.env')                                                             # Loads Client ID, Client Secret and Streamer's Name
secret = os.getenv('client_secret')
load_dotenv('streamName.env')
name = os.getenv('stream_name')
load_dotenv('channelID.env')
channelid = os.getenv('channel_id')

client_id =  id                                                                             # Info From https://dev.twitch.tv/console/apps
client_secret = secret                                                                      # Click manage app - ID and Secret are inside there
streamer_name = name                                                                        

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}

######### Returns OAuth token #########
r = requests.post('https://id.twitch.tv/oauth2/token', body)                               
keys = r.json()

######### Returns Client/Authorization Information #########
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']                                       
}                                                                                           
##### DETERMINES IF USER IS ONLINE BY CHECKING IF DATA IS RETURNED #####
stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
stream_data = stream.json()

def checkOnline(stream_data):
        stream_data = stream.json()
        return stream_data
                                                                                      
########### DISCORD BOT SETUP ############                                                  # https://betterprogramming.pub/coding-a-discord-bot-with-python-64da9d6cade7
load_dotenv('token.env')                                                                    # https://discordpy.readthedocs.io/en/latest/api.html#message   DISCORD API
token = os.getenv('DISCORD_TOKEN')                                                          # https://discord.com/developers/applications DISCORD APP TOKEN
bot = commands.Bot(command_prefix='!')                                                      #     ^     Go to Bot (Left Hand Side) to edit      ^

########## ON BOT START UP DISPLAY HOW MANY SERVERS ITS IN ########## 
##### DETERMINE IF TWITCH USER IS ONLINE AND ONLY POST IF THEY ARE ######
                    # CHECKS EVERY 60 SECONDS #
@bot.event
async def on_ready():
    serverCount = 0
    for server in bot.guilds:
        print(f'- {server.id} (name: {server.name})')
        serverCount += 1
        print('Twitch Live Notify is in ' + str(serverCount) + ' Servers.')

##### X DETERMINES IF USER IS ONLINE AND STOPS LOOP FROM SPAMMING #####
    x = 0                                                                               
    while True: 
        checkOnline(stream_data)                                                        
        
        channel = bot.get_channel(id=channelid)                                         # YOU CAN GET CHANNEL ID INSIDE DISCORD BY TYPING: \#channel
                                                                                        #                                             (ex. \#general)
        if stream_data['data'] == []:
            print('user is offline')
            x = 0
            time.sleep(60)
            continue
        elif stream_data['data'] != [] and x == 0:          #DISPLAYS TWITCH LINK, GAME & TITLE
            await channel.send('https://www.twitch.tv/' + streamer_name + '\nWent *LIVE*  on Twitch (**' \
            + str(stream_data['data'][0]['game_name']) + '**)\n' + '`'+str(stream_data['data'][0]['title']) + '`' )
            x = 1
            time.sleep(60)


bot.run(token)