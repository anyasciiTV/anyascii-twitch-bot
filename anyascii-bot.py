import os 
from twitchio.ext import commands 
from dotenv import load_dotenv  

# Load environment variables

load_dotenv() 

bot = commands.Bot(
    IRC_TOKEN=os.environ['TMI_TOKEN'], # TMI token
    CLIENT_ID=os.environ['CLIENT_ID'], # Client ID 
    BOT_NAME=os.environ['BOT_NAME'], # Include the Twitch bot's name
    PREFIX=os.environ['!'], # Prefix prior to the channel command 
    CHANNEL_NAME=[os.environ['CHANNEL_NAME']] # The channel command 
)

# Decorator registers an event and calls a function  when the bot logs in successfully

@bot.event 
async def event_ready(): 
    print(f'{os.environ["BOT_NAME"]} is online!')
    ws = bot._ws # pylint: disables protected-access 
    await ws.send_privmsg(os.environ["CHANNEL_NAME"],'Hello!') # Function sends a message to the specified channel

# Run the bot 

if __name__ == "__main__":
    bot.run()


# Explanation before continuing : 

# The code above is a simple example of Twitch IRC automated bot written in Python, using the "twitchio"
# library. The 'os' library is used to load environment variables, which are used to configure the bot's
# Twitch token, client ID name and command prefix. The 'dotenv' library is used to load the environemnt
# variables from a .env file. The '@bot.event' decorator is used to register a function that will be 
# called when the bot logs in successfully. In this example, the function sends a "Hello" message
# to the channel specified in the environment variables. The 'if __name__ == "__main__":` block
# at the bottom is used to run the bot. 