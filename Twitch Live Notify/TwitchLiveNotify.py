######## Created By: Stephen Fries, 2/6/22 ########
########## TWITCH CHECK IF USER IS ONLINE ##########
import requests

client_id = 'ClientIdGoesHereYouCanFindAtTwitch'                                                # Info From https://dev.twitch.tv/console/apps
client_secret = 'ClientSecretGoesHereYouCanFindAtTwitch'                                        # Click manage app - ID and Secret are inside there
streamer_name = 'UsernameOfUserToCheckOnline'                                                   # user you want to check if online (ex. 'shroud')

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}

######### Returns OAuth token #########
r = requests.post('https://id.twitch.tv/oauth2/token', body)                                    # Returns a generated Access Token for Twitch                               
keys = r.json()
print(keys)                                                                                     # Prints out data for debugging purposes to see if it succeeded

######### Returns Client/Authorization Information #########
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']                                           # Adds Client-ID and Authorization Key to headers                                       
}                                                                                           
print(headers)                                                                                  # Prints out headers for debugging purposes to see if it succeeded

stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers) #Pulls data from Helix (Twitch API)

##### DETERMINES IF USER IS ONLINE BY CHECKING IF DATA IS RETURNED #####
stream_data = stream.json()

print(stream_data)                                                                              # Prints out data pulled stream and formats as json
                                                                                                # If user is offline 'data' field will be empty list.
if stream_data['data'] != []:
    print('user is online')
elif stream_data['data'] == []:
    print('user is offline')
