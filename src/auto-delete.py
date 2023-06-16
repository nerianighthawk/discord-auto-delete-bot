import os
from discord import Intents, Client, Interaction
from discord.abc import GuildChannel
from discord.app_commands import CommandTree
from discord.ext import tasks
from dotenv import load_dotenv

# .env ファイルをロードして環境変数へ反映
load_dotenv()

# 環境変数からトークンを取得
TOKEN = os.getenv('TOKEN')

class AutoDelete(Client):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)
    
    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self):
        print(f"login: {self.user.name} [{self.user.id}]")

    @tasks.loop(seconds=5)
    async def check_messages(self, channel: GuildChannel):
        await channel.send('test')


intents = Intents.all()
intents.typing = False
client = AutoDelete(intents=intents)


@client.tree.command(
    name="read_start",
    description="send test"
)
async def start(interaction: Interaction):
    print('start')
    await interaction.response.send_message("started")
    client.check_messages.start(interaction.channel)


@client.tree.command(
    name="read_end",
    description="end test"
)
async def stop(interaction: Interaction):
    print('end')
    await interaction.response.send_message("stop")
    client.check_messages.start(interaction.channel)


client.run(TOKEN)
