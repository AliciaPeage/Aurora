import discord

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')


async def vjoin(client, message, args):

    channel = discord.utils.get(message.server.channels, name=args[0], type=discord.ChannelType.voice)

    try:
        await client.join_voice_channel(channel)
    except discord.ClientException:
        print('Already in a voice channel...')
    except discord.InvalidArgument:
        print('This is not a voice channel...')
    else:
        print('Ready to play audio in ')

async def vleave(client, message, args):
    print('bob')