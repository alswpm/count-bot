import discord
from discord.ext import commands
from discord.ui import View, Button

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

players = {
    "민제": 0,
    "범수": 0,
    "상민": 0,
    "기준": 0
}

class CounterView(View):
    def __init__(self):
        super().__init__(timeout=None)
        for name in players.keys():
            self.add_item(PlayerButton(name))

class PlayerButton(Button):
    def __init__(self, name):
        super().__init__(label=f"{name} +1", style=discord.ButtonStyle.primary)
        self.name = name

    async def callback(self, interaction: discord.Interaction):
        # 카운트 증가
        players[self.name] += 1

        # 새 View를 다시 생성 (버튼 동작 유지용)
        view = CounterView()

        # 새 메시지 내용 만들기
        msg = "\n".join([f"**{n}**: {c}" for n, c in players.items()])

        # interaction 응답 (edit_message 대신 response.edit_message 사용)
        await interaction.response.edit_message(content=msg, view=view)

@bot.command()
async def start(ctx):
    """카운트 시작"""
    msg = "\n".join([f"**{n}**: {c}" for n, c in players.items()])
    view = CounterView()
    await ctx.send(msg, view=view)

@bot.event
async def on_ready():
    print(f"✅ 로그인 완료: {bot.user}")

bot.run("MTQzMTk0ODEzODI2ODA3MDAyMw.GWQva7.tPPLUc0YgiIhhdG0k4SUQ91C5N2la4iTTCz7wQ")
