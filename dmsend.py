
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('섹스')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="욕배틀 시작!")
                        embed.add_field(name="욕배틀 시작했습니다 빨리 겨들어오세요", value=msg, inline=True)
                        embed.set_footer(text=f"https://discord.gg/3AgNku")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzQ1MTAwNjMzMDgxNjQzMTMx.Xzs3Cg.FTxb-_aznnmH35Ny66bsQ3h86-8')
