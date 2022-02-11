# Twitch Live Notify - Discord Bot
* Uses Python 3+ 
    * discord.py 
    * python-dotenv
    * requests
* Twitch API 
* Discord API

## PROGRAM
Checks if a user has started a stream and posts the information to discord <br />
Displays: Stream URL / Game Stream is Playing / Title of the Stream.
![Imgur](i.imgur.com/Hl9nETw.png)

## Dependencies Installation
* Open Command Prompt
* pip install discord.py
* pip install python-dotenv
* pip install requests

## HOW TO USE
### FIRST WE MUST CREATE A DISCORD BOT
* Log into: https://discord.com/developers/applications/
* Click on "New Application" on the top right
* Name your bot - Mine is called "Twitch Live Notify"
* Click Create
* Click "Bot" on the Left-Hand Side Menu
* Click "Add Bot"
* It will ask if you want to tie a bot to your application - click yes
* Click "OAuth2" on the Left-Hand Side Menu
* Click In-app Authorization
* Checkmark "bot"
* At the bottom you should see a URL generate, copy that URL
* Paste that URL into your browser and Select the server you want the bot to join
* Now go back to the discord webpage and click "Bot" on the left-hand side
* Under "USERNAME" you should see "TOKEN" Click on "Click to Reveal Token"
* Copy that string to a text file, we will use it later

## TWITCH DEVELOPER APPLICATION
* Log into: https://dev.twitch.tv/console/apps
* Select "Applications" and then click "Register Your Application"
* Set "Name" of your application to anything you like
* Set OAuth Reirect URLs to "http://localhost" then click "Add"
* Select "Category" of your bot, this does not matter
* Click "Applications" tab, locate your app under "Developer Applications" and click "Manage"
* You Should see "Client ID" and "Client Secret" > "New Secret"
* Click "New Secret" to generate a secret for your application
* copy both the Client ID and Client Secret to the text file you put the discord token in

## GET YOUR CHANNEL ID
* Quickest and Easiest Way is to go to your Discord Server
* type backslash and your discord channel name. (For example: \#general)
* Copy the numbers into the text file with your discord token, twitch client id, and secret

## CHANGING .ENV FILES TO YOUR SETTINGS
* Go inside the "Twitch Live Notify" Folder
* Right-Click token.env and click "edit" or open with notepad
* Replace "TypeDiscordTokenHere" with your discord token you copied in the text file - make sure you don't remove the "DISCORD_TOKEN="
* Save token.env
* Right-Click clientID.env and click "edit" or open with notepad
* Replace "TypeYourClientIDHere" with your Twitch Client ID you copied in the text file - make sure you don't remove the "client_id="
* Save clientID.env
* Right-Click clientSecret.env and click "edit" or open with notepad
* Replace "TypeYourClientSecretHere" with your Twitch Client Secret you copied in the text file - make sure you don't remove the "client_secret="
* Save clientSecret.env
* Right-Click channelID.env and click "edit" or open with notepad
* Replace "TypeDiscordChannelIDHere" with your Discord Channel Numbers you copied in the text file - make sure you don't remove the "channel_id="
* Save channelID.env
* Right-Click streamName.env and click "edit" or open with notepad
* Replace "TypeStreamerNameHere" with a Twitch Streamer Username - make sure you don't remove the "stream_name="
* Save streamName.env


## RUN THE PROGRAM AND ENJOY!


