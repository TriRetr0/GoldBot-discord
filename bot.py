import discord
import random
import typing
from discord.utils import get
from discord.ext import commands

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '\\')
@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="\h"))
	print("Ready")

@client.command()
async def ping(ctx):
	embedVar = discord.Embed(title="PONG!", description=f"{round (client.latency * 1000)}ms")
	await ctx.send(embed=embedVar)
	print(f'Pong! {round (client.latency * 1000)}ms ')

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	embedVar = discord.Embed(title="BANNED:", description=f"User {member.mention} has been kicked")
	embedVar.set_image(url="https://media.tenor.com/images/20f4d7719a71e29fb905eb49006b91ff/tenor.gif")
	await ctx.send(embed=embedVar)
	print(f'User {member} has been kicked')

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embedVar = discord.Embed(title="UNBANNED:", description=f"User {member.mention} has been unbanned")
            await ctx.send(embed=embedVar)
            print(f'Unbanned {user}')
            return

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.User, *, reason=None):
	await member.ban(reason=reason)
	embedVar = discord.Embed(title="BANNED:", description=f"User {member.mention} has been banned")
	embedVar.set_image(url="https://media1.tenor.com/images/4f70c8f25f6836936afc348c1f982373/tenor.gif")
	userAvatarUrl = member.avatar_url
	embedVar.set_thumbnail(url=userAvatarUrl)
	await ctx.send(embed=embedVar)
	print(f'User {member} has been banned')

@client.command()
async def ip(ctx):
	emb = discord.Embed(title="Le serveur n'est pas encore ouvert", color=0xfcca03)
	await ctx.send(embed=emb)
	print("Le serveur n'est pas encore ouvert")

@client.command()
async def banlist(ctx):
	number=0
	embedVar = discord.Embed(title="BANLIST:", description="**DEV BY TriRetr0**", color=0xFF0000)
	banned_users = await ctx.guild.bans()
	for i in banned_users:
		number = number+1
		f = open("ban.txt","a")
		f.write(f"{i}\n")
		embedVar.add_field(name=f"User {number}:", value=f"{i}", inline=False)
		print(number)
	BAN_LIST = open("ban.txt","r").read()
	await ctx.send(embed=embedVar)
	print(BAN_LIST)
	open("ban.txt","w").write("")

@client.command()
async def invite(ctx):
	embedVar = discord.Embed(title="INVITE MY BOT", description="[**DEV BY TriRetr0**](https://discord.com/oauth2/authorize?client_id=751510591977291786&scope=bot&permissions=8)", color=0xfcca03)
#	embedVar.set_image(url="https://cdn.discordapp.com/avatars/751510591977291786/c49a678f9485184e1a86ef449456b350.webp?size=64")
	await ctx.send(embed=embedVar)
	print("INVITE")

@client.command()
async def vote(ctx):
	embedVar = discord.Embed(title="VOTE:", description="[**DEV BY TriRetr0**](https://serveur-minecraft.com/1872)", color=0xfcca03)
#	embedVar.set_image(url="https://cdn.discordapp.com/avatars/751510591977291786/c49a678f9485184e1a86ef449456b350.webp?size=64")
	await ctx.send(embed=embedVar)
	print("INVITE")

@client.command()
async def guilds(ctx):
	GUILDS = client.guilds
	for i in GUILDS:
		print(i)
		f = open("guilds.txt","a")
		f.write(f"{i}\n")
	GUILDS_LIST = open("guilds.txt","r").read()
	embedVar = discord.Embed(title="GUILDS :", description=f"{GUILDS_LIST}", color=0xfcca03)
	await ctx.send(embed = embedVar)
	erase = open("guilds.txt","w")
	erase.write("")

@client.command()
async def dm(ctx, user: discord.User):
	invitelink = await ctx.channel.create_invite(maw_uses=1,unique=True)
	await user.send(invitelink)
	print(user)

@client.command()
async def cat(ctx):
	embedVar = discord.Embed(title="CAT:")
	embedVar.set_image(url="https://images.theconversation.com/files/350865/original/file-20200803-24-50u91u.jpg")
	await ctx.send(embed=embedVar)

@client.command()
async def dog(ctx):
	embedVar = discord.Embed(title="DOG:")
	embedVar.set_image(url="https://images.theconversation.com/files/319375/original/file-20200309-118956-1cqvm6j.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=900.0&fit=crop")
	await ctx.send(embed=embedVar)

@client.command()
async def bird(ctx):
	embedVar = discord.Embed(title="BIRD:")
	embedVar.set_image(url="https://upload.wikimedia.org/wikipedia/commons/4/45/Eopsaltria_australis_-_Mogo_Campground.jpg")
	await ctx.send(embed=embedVar)

@client.command()
async def meme(ctx, image_url, title):
	await ctx.message.delete()
	username = ctx.message.author.name
	avatar = ctx.message.author.avatar_url
	embedVar = discord.Embed(title=f"{title}", description=f"{username}'s meme")
	embedVar.set_thumbnail(url=avatar)
	embedVar.set_image(url=f"{image_url}")
	await ctx.send(embed=embedVar)
	print(avatar)

@client.command()
@commands.has_permissions(administrator=True)
async def react(ctx, title):
	await ctx.message.delete()
	username = ctx.message.author.name
	avatar = ctx.message.author.avatar_url
	embedVar = discord.Embed(title=f"{title}", description=f"Author: {username}")
	embedVar.set_thumbnail(url=avatar)
	message = await ctx.send(embed=embedVar)
	await message.add_reaction("✔")
	await message.add_reaction("❌")
	print(avatar)

@client.command()
async def c(ctx, calcul):
	userAvatarUrl = ctx.message.author.avatar_url
	username = ctx.message.author.name
	result = eval(calcul)
	print(eval(calcul))
	embedVar = discord.Embed(title=f"{result}", description=f"{username}")
	await ctx.send(embed=embedVar)

@client.command()
async def ann(ctx, title, description, mention):
	userAvatarUrl = ctx.message.author.avatar_url
	username = ctx.message.author.id
	embedVar = discord.Embed(title=f"{title}", description=f"<@{mention}> {description}")
	embedVar.set_thumbnail(url=f"{userAvatarUrl}")
	embedVar.add_field(name=f"Author :", value=f"<@{username}>", inline=True)
	await ctx.send(embed=embedVar)

@client.command()
async def avatar(ctx, *, member : discord.User):
	userAvatarUrl = avamember.avatar_url
	username = ctx.message.author.name
	embedVar = discord.Embed(title=f"{username}")
	embedVar.set_image(url=f"{userAvatarUrl}")
	await ctx.send(embed=embedVar)

@client.command()
async def x(ctx):
	message = ctx.message
	await message.add_reaction('<:gold:750244705878540340>')

@client.command()
async def h(ctx):
	embedVar = discord.Embed(title="HELP - RealGoldBot", description="RealGoldBot dev by TriRetr0", color=0xfcca03)
	embedVar.set_thumbnail(url="https://img.icons8.com/bubbles/2x/help.png")
	embedVar.add_field(name="\\h", value="Display this message", inline=True)
	embedVar.add_field(name="\\ping", value="Latency test", inline=True)
	embedVar.add_field(name="\\ban", value="*[Admin only]*: usage: \\ban [@user]", inline=True)
	embedVar.add_field(name="\\unban", value="*[Admin only]*: usage: \\unban [user#tag]", inline=True)
	embedVar.add_field(name="\\kick", value="*[Admin only]*: usage: \\kick [@user]", inline=True)
	embedVar.add_field(name="\\react", value="*[Admin only]*: usage: \\react [Title]", inline=True)
	embedVar.add_field(name="\\dm", value="Send a DM with an invite of the server. usage: \\dm [username#tag]", inline=True)
	embedVar.add_field(name="\\guilds", value="Display all the servers with RealGoldBot inside", inline=True)
	embedVar.add_field(name="\\invite", value="Send a link to invite this bot in your server", inline=True)
	embedVar.add_field(name="\\vote", value="Send a link to vote our server", inline=True)
	embedVar.add_field(name="\\ip", value="Display the ip of our minecraft server", inline=True)
	embedVar.add_field(name="\\banlist", value="Display all bans", inline=True)
	embedVar.add_field(name="\\bird", value="It's a bird", inline=True)
	embedVar.add_field(name="\\dog", value="It's a coroned dog", inline=True)
	embedVar.add_field(name="\\cat", value="It's a coroned cat", inline=True)
	embedVar.add_field(name="\\c", value='Calcul. Usage: \\c [ex: 1+1 (+,-,/,*)]', inline=True)
	embedVar.add_field(name="\\meme", value='Post your meme. Usage: \\meme [image URL] "[Your title]" ', inline=True)
	await ctx.send(embed=embedVar)

@client.event
async def on_command_error(ctx, error):
	embedVar = discord.Embed(title="ERROR:", description=f'```{error}```')
	await ctx.send(embed=embedVar)
	print(error)

client.run(TOKEN)
