from initializations import * 

@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")
    if message.author == bot.user:  #���ѹݺ� ����
        return
    
    if message.content.startswith("����"):
        if message.author == message.guild.owner:
            await message.channel.send(f"�� ���")
        else:
            await message.channel.send(f"�� ��ɾ�� ���� ���θ� ����� �� �־��.")

    await bot.process_commands(message) #�� ������ ������ prefix ��ɾ ���� ���� �ʾ���