import os

#test for environment variables
key = 'DISCORD_BOT_TOKEN'
token = os.getenv(key)
print (token)


