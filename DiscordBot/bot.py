import discord
import responses

async def send_messages (message, user_message, is_private):
    try:
        response = responses.handleresponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA5NTg4MTI1Njc2NTQ5NzQ2NA.GGn2dd.c8EcCuoot5HFr9jMuDosEuaE655chYEHvSFN9g'
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)