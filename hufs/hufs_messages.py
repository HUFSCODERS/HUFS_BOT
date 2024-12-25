from discord.ext import commands 

class HufsMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.monitor_message = """ 
# Monitoring.. 👀

한국외대 -공지(웹사이트)- 연결 상태: {}
한국외대 -학사(웹사이트)- 연결 상태: {}
한국외대 -장학(웹사이트)- 연결 상태: {}

디스코드 -공지(채널)- 연결 상태: {}
디스코드 -학사(채널)- 연결 상태: {}
디스코드 -장학(채널)- 연결 상태: {}

디스코드 -공지(역할)- 연결 상태: {}
디스코드 -학사(역할)- 연결 상태: {}
디스코드 -장학(역할)- 연결 상태: {}

마지막으로 업데이트한 시간: {}
monitor 주기: {}초
"""
        self.channel_message = """
ㅤㅤㅤㅤㅤㅤㅤ
ㅤㅤㅤㅤㅤㅤㅤ 
## {}
-# NO: {} 
작성자: **{}**
작성일: **{}**
바로가기 링크-> {}
맨션: {}
"""

async def setup(bot):
    await bot.add_cog(HufsMessages(bot))