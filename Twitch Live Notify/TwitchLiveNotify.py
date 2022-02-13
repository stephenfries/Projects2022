from asyncio import streams
import os, requests, time                                              #                               IMPORTS TO ALLOW FOR DISCORD/TWITCH API                            #
from dotenv import load_dotenv                                         # pip install discord.py | pip install python-dotenv | pip install requests  | pip install asyncio #
from discord.ext import commands                                       

load_dotenv('config.env')
id = os.getenv('client_id')                                                                 # Loads Client ID, Client Secret and Streamer's Name
secret = os.getenv('client_secret')
name = os.getenv('stream_name')
channelID = os.getenv('channel_id')

client_id =  id                                                                             # Info From https://dev.twitch.tv/console/apps
client_secret = secret                                                                      # Click manage app - ID and Secret are inside there
streamer_name = name.split(',')                                                             # separate multiple users with comma (shroud,summit1g,etc)
print(streamer_name)
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

def checkOnline(streamers):
    global headers
    global stream_data
    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + str(streamers), headers=headers)
    stream_data = stream.json()
    return stream_data
                                                                                      
########### DISCORD BOT SETUP ############                                                  
                                                                                            # https://discordpy.readthedocs.io/en/latest/api.html#message   DISCORD API
token = os.getenv('discord_token')                                                          # https://discord.com/developers/applications DISCORD APP TOKEN
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

##### offlineStatus DETERMINES IF USER IS ONLINE AND checkStatus IS FOR SCALABILITY #####
    checkStatus = 0
    offlineStatus = [] 
    for streamers in streamer_name:
            streamStatus = {streamers:'offline'}
            offlineStatus.append(streamStatus)  
    print(offlineStatus)                                                                        # SHOWS WHO IS CURRENTLY ONLINE / OFFLINE                                                
    while True: 
            for streamers in streamer_name:
                checkOnline(streamers)                                                         
                channel = bot.get_channel(id=int(channelID))                                    # YOU CAN GET CHANNEL ID INSIDE DISCORD BY TYPING: \#channel
                if checkStatus <= len(list(streamer_name)):                                     #                                             (ex. \#general)
                    if checkOnline(streamers) == {'data': [], 'pagination': {}}:
                        print(streamers + ' is offline')
                        offlineStatus[checkStatus] = {streamers:'offline'}
                        checkStatus += 1
                        continue                                               # v CHANNEL.SEND DISPLAYS TWITCH LINK, GAME & TITLE v
                    elif checkOnline(streamers) != {'data': [], 'pagination': {}} and offlineStatus[checkStatus] == {streamers:'offline'}:          
                        await channel.send('https://www.twitch.tv/' + streamers + '\nWent *LIVE*  on Twitch (**' \
                        + str(stream_data['data'][0]['game_name']) + '**)\n' + '`'+str(stream_data['data'][0]['title']) + '`')
                        offlineStatus[checkStatus] = {streamers:'online'}
                        print(streamers + ' is online.')
                    checkStatus += 1
            checkStatus = 0
            time.sleep(30)    
bot.run(token)