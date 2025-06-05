import discord
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Platform regex to embeddable links
PLATFORMS = {
    r"(https?://(?:www\.)?instagram\.com/p/\S+)": "https://kkinstagram.com/p/",
    r"(https?://(?:www\.)?instagram\.com/reel/\S+)": "https://kkinstagram.com/reel/",
    r"(https?://(?:www\.)?instagram\.com/tv/\S+)": "https://kkinstagram.com/tv/",
    r"(https?://(?:www\.)?instagram\.com/stories/\S+)": "https://kkinstagram.com/stories/",
    r"(https?://(?:www\.)?twitter\.com/\S+)": "https://vxtwitter.com/",
    r"(https?://(?:www\.)?tiktok\.com/\S+)": "https://vxtiktok.com/",
    r"(https?://(?:www\.)?reddit\.com/\S+)": "https://vxreddit.com/",
}

# Convert original URL to embeddable one
def transform_link(url):
    for pattern, new_base in PLATFORMS.items():
        match = re.match(pattern, url)
        if match:
            path = url.split(".com/")[1]
            return new_base + path
    return None

@client.event
async def on_ready():
    print(f'🤖 Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    modified_links = []

    for word in message.content.split():
        new_link = transform_link(word)
        if new_link and new_link != word:
            modified_links.append(new_link)

    if modified_links:
        try:
            await message.delete()
        except discord.Forbidden:
            print("⚠️ Missing permission to delete messages.")
        except discord.HTTPException as e:
            print(f"⚠️ Failed to delete message: {e}")

        user_mention = message.author.mention
        await message.channel.send(
            f"🔗 Embeddable Links (requested by {user_mention}):\n" +
            "\n".join(modified_links)
        )

print("🔑 Loaded token:", TOKEN)
client.run(TOKEN)
