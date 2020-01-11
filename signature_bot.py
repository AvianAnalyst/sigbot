import discord
import json

client = discord.Client()
with open('sigs.json', 'r')as sig_file:
    sigs = json.load(sig_file)
print(sigs)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(f'msg received, author == {message.author}, message.author.id == {message.author.id}')
    print(type(message.author.id))
    if message.content.startswith('!sig'):
        signature = message.content[5:]
        sigs[str(message.author.id)] = signature
        with open('sigs.json', 'w') as sig_file:
            json.dump(sigs, sig_file)

    if str(message.author.id) in sigs.keys():

        await message.channel.send(sigs[str(message.author.id)])
    else:
        print('something went wrong')


client.run('NjY1MzMxNzIwNzM1ODE3NzI4.XhkEmw.6c5gqW2mzAFplN617cn0MwuQTfU')

