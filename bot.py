print("Starting Muffin...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

Client = discord.Client()
bot_prefix= ["m.", "M."]
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='398867510608265221')
footer_text = "═ ∘Our ♡ Server∘ ═"
error_img = ':warning:'
default_invite = 'https://discord.gg/Er3XwBm'
limit = 10000000000000000
version = '1.0'

mods = ['299761993382887425']
mods_chnl = '528843220315275284'
banned_users = []
banned_servers = []
ignored = []
currency_t = []
responses_t = []
currencies = []

hug_links = []
pat_links = []
kiss_links = []
nom_links = []
throw_links = []
bite_links = []
bloodsuck_links = []
cuddle_links = []
highfive_links = []
poke_links = []
slap_links = []
punch_links = []
stare_links = []
facepalm_links = []
lick_links = []
spank_links = []
cry_links = []
dance_links = []
bow_links = []
dab_links = []

rps_choices = ["rock", "paper", "scissors", "r", "p", "s"]
rps_r = ["rock", "r"]
rps_p = ["paper", "p"]
rps_s = ["scissors", "s"]
rps_tie = {"rock" : "rock",
           "paper" : "paper",
           "scissors" : "scissors",
           "r" : "rock",
           "p" : "paper",
           "s" : "scissors"}

eb = ["Hell no!",
      "No!",
      "Hell yes!",
      "Yes!",
      "Definitely!",
      "Definitely not!",
      "Probably!",
      "Probably not!",
      "Most likely!",
      "Yes! I'm sure of it!",
      "No! I'm sure of it!"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

revivals = []
nhie_msgs = []
wyr_msgs = []
marriages = []
dicks = []
howgays = []
ships = []
rates = []
balances = []

con_messages = []
con_wait = []
slots_wait = []
worked = []
stole = []

responses_msgs = {"good bot" : ["C:", "yey me good botty", "I'm not your dog, human.", "uwu"],
             "bad bot" : [";c", "so sad", "I'm not your fucking dog.", "much cri"],
             "fun" : ["fun?", "fun.", "fun!", "( ͡° ͜ʖ ͡°)"],
             "ayy" : ["lmao", "ayy bro", "aye"],
             "lol" : ["hahaha", "lmao", "xD", "lol"],
             "hi" : ["hello", "haalloo", "hey", "hi, how you doing?"],
             "whalecum" : ["stop saying that shit", "c r i n g e", ">.>", "(╯°□°）╯︵ ┻━┻", "just why", "fucking pervert"],
             "fuck you" : ["well fuck you right back", ":(", "so rude"],
             "fuck" : ["you", "me", "us", "everyone"],
             "heck" : ["no swearing on this christian server", "ban this filth", ">:C"],
             "ok" : ["ok", "yes", "not ok", "k"],
             "cool" : ["cool cool", "cool indeed"],
             "spook" : ["sp00k3d"],
             "yas" : ["fucking hell that was cringy as shit", "...", ">.>", "yass moist fam"],
             "owo" : ["OWO", "OwO", "uwu", "UwU"],
             "bitch" : ["betch", "benches be benching", "*bench*"],
             "nigga" : ["YOU CAN'T SAY THAT, IT'S RACIST", "ni:b::b:a", "gigga nigga"],
             "same" : ["same", "me too"],
             "welcome" : ["welcome", "welcome, have fun", "enjoy your stay", "heyo, welcome to this beautiful server"],
             "bye" : ["no wait ;-; come back", "cyah", "goodnight", "bai"],
             "jk" : ["its joke", "syke its just a prank", "lol", "xd"],
             "no u" : ["yesn't u", "no us", "no no u", "aint you"],
             "rip" : ["gg", "f"]}


banned_users_chnl = '528843505464770580'
banned_servers_chnl = '528843566127251465'
log_chnl = '528843600516087810'
dicks_chnl = '528843692870729738'
balances_chnl = '528843731416252416'
marriages_chnl = '528843768191909889'
gays_chnl = '528843802555842560'
ships_chnl = '528843846369673216'
wyr_chnl = '528843875570286603'
nhie_chnl = '528843921195794470'
revivals_chnl = '528843952703406129'
interactions_chnl = '528843987377848320'
ignored_chnl = '528844025353076736'
currency_t_chnl = '515867314189631507'
responses_t_chnl = '528844116549959691'
rates_chnl = '528844163693805568'

staff_role = '516586573668679680'
splitter = "**~~`====================`~~**"

loading_e = ":arrows_counterclockwise: "
slotsgif1_e = ":gem: "
slotsgif2_e = ":moneybag: "
slotsgif3_e = ":heavy_dollar_sign: "
slotsgif4_e = ":dollar: "
error_e = ":x:"
bug_e = ":bug: "
close_e = ":heavy_multiplication_x: "
log_e = ":newspaper2: "
msg_e = ":bow: "
noperms_e = ":x:"
pingbad_e = ":beginner: "
pinggood_e = ":beginner: "
pingok_e = ":beginner: "
reload_e = ":arrows_counterclockwise:"
servers_e = ":shield: "
support_e = ":shield: "
users_e = ":grinning: "
worked_e = ":black_heart:"
check_e = ":white_check_mark: "
interactions_e = ":tada: "
game_e = ":video_game: "
battle_e = ":crossed_swords: "
messages_e = ":comet: "
bannedservers_e = ":no_entry_sign: "
bannedusers_e = ":no_entry: "
cointoss_e = ":heavy_dollar_sign: "
suicide_e = ":skull: "
roast_e = ":fire: "
calculator_e = ":1234: "
ship_e = ":sparkles: "
kill_e = ":gun: "
rate_e = ":100: "
dicklength_e = ":eggplant: "
howgay_e = ":gay_pride_flag: "
suggestion_e = ":bulb: "
coins_e = ":gem: "
divorce_e = ":broken_heart: "
marriage_e = ":heart: "
convert_e = ":recycle: "
slots_e = ":slot_machine: "
on_e = ":black_square_button: "
off_e = ":black_large_square:  "
ignored_e = ":no_entry_sign: "
work_e = ":dollar: "
generator_e = ":bulb: "
steal_e = ":bust_in_silhouette: "
gift_e = ":gift: "
ban_e = ":wave: "
link_e = ":link: "

started = ["1"]
# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(banned_users_chnl), limit=limit):
        a = i.content.split(' | ')
        banned_users.append(a[0])
    print("[START UP] Loaded banned users.")
    async for i in client.logs_from(client.get_channel(wyr_chnl), limit=limit):
        wyr_msgs.append(i.content)
    print("[START UP] Loaded 'would you rather' messages.")
    async for i in client.logs_from(client.get_channel(nhie_chnl), limit=limit):
        nhie_msgs.append(i.content)
    print("[START UP] Loaded 'never have I ever' messages.")
    async for i in client.logs_from(client.get_channel(revivals_chnl), limit=limit):
        revivals.append(i.content)
    print("[START UP] Loaded chat revivals.")
    async for i in client.logs_from(client.get_channel(marriages_chnl), limit=limit):
        marriages.append(i.content)
    print("[START UP] Loaded marriages.")
    async for i in client.logs_from(client.get_channel(dicks_chnl), limit=limit):
        dicks.append(i.content)
    print("[START UP] Loaded dick lengths.")
    async for i in client.logs_from(client.get_channel(gays_chnl), limit=limit):
        howgays.append(i.content)
    print("[START UP] Loaded how-gays.")
    async for i in client.logs_from(client.get_channel(ships_chnl), limit=limit):
        ships.append(i.content)
    print("[START UP] Loaded ships.")
    async for i in client.logs_from(client.get_channel(rates_chnl), limit=limit):
        rates.append(i.content)
    print("[START UP] Loaded rates.")
    async for i in client.logs_from(client.get_channel(balances_chnl), limit=limit):
        a = i.content.split(' | ')
        balances.append(a[0])
    print("[START UP] Loaded balances.")
    interaction_sys = {"hug" : hug_links,
                       "kiss" : kiss_links,
                       "pat" : pat_links,
                       "slap" : slap_links,
                       "punch" : punch_links,
                       "cuddle" : cuddle_links,
                       "bloodsuck" : bloodsuck_links,
                       "bite" : bite_links,
                       "bow" : bow_links,
                       "dance" : dance_links,
                       "dab" : dab_links,
                       "nom" : nom_links,
                       "throw" : throw_links,
                       "highfive" : highfive_links,
                       "poke" : poke_links,
                       "stare" : stare_links,
                       "spank" : spank_links,
                       "lick" : lick_links,
                       "facepalm" : facepalm_links,
                       "cry" : cry_links}
    interactions_total = []
    async for i in client.logs_from(client.get_channel(interactions_chnl), limit=limit):
        a = i.content.split(' | ')
        interaction_sys[a[0]].append(a[1])
        interactions_total.append("+1")
    print("[START UP] Loaded interactions.")
    async for i in client.logs_from(client.get_channel(ignored_chnl), limit=limit):
        ignored.append(i.content)
    print("[START UP] Loaded ignored channels.")
    async for i in client.logs_from(client.get_channel(currency_t_chnl), limit=limit):
        currency_t.append(i.content)
    print("[START UP] Loaded currency toggles.")
    async for i in client.logs_from(client.get_channel(responses_t_chnl), limit=limit):
        responses_t.append(i.content)
    print("[START UP] Loaded responses toggles.")
    async for i in client.logs_from(client.get_channel(mods_chnl), limit=limit):
        mods.append(i.content)
    print("[START UP] Loaded mods.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="m!help | m!invite |"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel(log_chnl))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    await client.send_message(client.get_channel(log_chnl), m)
       
# CURRENCY SYSTEM / AUTO-RESPONSES
@client.event
async def on_message(msg):
    if len(started) != 0:
        if msg.channel.id not in ignored and not msg.author.bot:
            con_messages.append(msg.author.id)
            if msg.author.id not in balances:
                await client.send_message(client.get_channel(balances_chnl), "{} | 0".format(msg.author.id))
                balances.append(msg.author.id)
            if msg.content.lower() in responses_msgs and msg.server.id not in responses_t:
                p = random.randint(0, 1)
                if p == 0:
                    await client.send_message(msg.channel, random.choice(responses_msgs[msg.content.lower()]))
    await client.process_commands(msg)

# }ping
@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif '}ping f' in str(ctx.message.content) or '}ping all' in str(ctx.message.content) or '}' not in str(ctx.message.content):
        t1 = time.perf_counter()
        await client.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        ping = round((t2-t1)*1000)
        if ping > 300:
            m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
        elif ping > 200:
            m = "{} The bot might be lagging.".format(pingok_e)
        else:
            m = "{} The bot isn't lagging.".format(pinggood_e)
        embed.description = "My ping is `{}ms`.\n{}".format(ping, m)
        await client.say(embed=embed)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        m = ":link: Use [this link](https://discord.gg/Er3XwBm) to invite your friends."
        embed.description = m
        await client.say(embed=embed)           
           
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif '}' not in str(ctx.message.content):
        embed.description = "{} Loading information...".format(loading_e)
        h = await client.say(embed=embed)
        m = "**ID:** `{}`".format(ctx.message.server.id)
        m += "\n**OWNER:** `{}`".format(ctx.message.server.owner)
        m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
        m += "\n**REGION:** `{}`".format(ctx.message.server.region)
        m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
        embed.description = "{} **__SERVER INFORMATION:__**\n\n{}".format(servers_e, m)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        ts = ""
        if ctx.message.server.id in currency_t:
            ts += "\n{}`Currency Rewards`{}".format(coins_e, off_e)
        else:
            ts += "\n{}`Currency Rewards`{}".format(coins_e, on_e)
        if ctx.message.server.id in responses_t:
            ts += "\n{}`Auto-Responses`{}".format(messages_e, off_e)
        else:
            ts += "\n{}`Auto-Responses`{}".format(messages_e, on_e)
        embed.add_field(name="{} TOGGLES:".format(bannedusers_e), value=ts, inline=True)
        ing = ""
        for i in ctx.message.server.channels:
            if i.id in ignored:
                ing += "  <#{}>".format(i.id)
        if ing != "":
            embed.add_field(name="{} IGNORED CHANNELS:".format(ignored_e), value=ing, inline=True)
        await client.edit_message(h, embed=embed)           
           
# }suicide
@client.command(pass_context=True)
async def suicide(ctx):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        msgs = ["**{}** tried to commit suicide but failed! Better luck next time I guess.".format(ctx.message.author.name),
                "**{}** killed themselves after losing all their diamonds on their christian minecraft server.".format(ctx.message.author.name),
                "**{}** had no internet connection for more than 5 seconds so they commited suicide.".format(ctx.message.author.name),
                "**{}** felt weird in the middle of the night, but hentaihaven was down so they killed themselves.".format(ctx.message.author.name),
                "**{}** didn't really have a life, but they still managed to kill themselves.".format(ctx.message.author.name),
                "**{}** watched boku no pico, few seconds later they jumped off the 7th floor.".format(ctx.message.author.name),
                "**{}** saw Huskie's face. They instantly commited suicide after that.".format(ctx.message.author.name),
                "All of **{}**'s memes were stolen. Not having any memes or dreams left, they decided to kill themselves.".format(ctx.message.author.name),
                "**{}** realized how shitty this server actually is. Leaving it wasn't enough so they commited suicide too.".format(ctx.message.author.name),
                "**{}** had anxiety for way too long. They couldn't live with it anymore so they took their own life away.".format(ctx.message.author.name),
                "**{}** was bipolar. That disorder was messing up their life too much so they commited suicide.".format(ctx.message.author.name),
                "**{}** suffered from depression for years. Not having any hope or motivation left, they commited suicide.".format(ctx.message.author.name),
                "**{}** was physically abused every day. They thought killing themselves would make things better.".format(ctx.message.author.name),
                "**{}** was sexually abused. That experience made them take their own life away.".format(ctx.message.author.name),
                "**{}** lived in war and chaos for a very long time. The day they had enough was the day they killed themselves.".format(ctx.message.author.name),
                "**{}** was bullied in school, outside, even at home. They couldn't take it anymore so they commited suicide.".format(ctx.message.author.name),
                "**{}** had a personality disorder that made them take their life away.".format(ctx.message.author.name),
                "**{}** had an eating disorder. They couldn't eat anything without thorwing up after that so they took their life away.".format(ctx.message.author.name),
                "**{}** was lonely all their life. Not having any friends or family, they killed themselves without anyone finding out.".format(ctx.message.author.name),
                "**{}** had a great relationship that started to fall apart. After their partner left them, they became depressed and decided to kill themselves, thinking no one would ever love them again.".format(ctx.message.author.name),
                "**{}** commited suicide. Too bad there's no one to leave a flower on their grave...".format(ctx.message.author.name),
                "**{}** killed themselves.".format(ctx.message.author.id)]
        embed.description = "{} {}".format(suicide_e, random.choice(msgs))
        await client.say(embed=embed)           
     
# }roast <user>
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if user == None:
            embed.description = "{} Please mention the user you want to roast.".format(error_e)
            await client.say(embed=embed)
        else:
            if user.id == client.user.id:
                user = ctx.message.author
            else:
                user = user
            msgs = ["Why would I bother roasting someone like **{}** when the mirror does it every morning?".format(user.name),
                    "We all hate you, **{}**. Just not quite enough to think about you.".format(user.name),
                    "**{}** don't play hard to get when you are hard to want.".format(user.name),
                    "God wasted a good asshole when he put teeth in your mouth, **{}**.".format(user.name),
                    "I can't even call **{}** ugly. Nature has beaten me to it.".format(user.name),
                    "I can't roast **{}**. I simply can't imagine the pain they go thru with that face.".format(user.name),
                    "**{}**, I would call you a cunt, but you lack the warmth or the depth.".format(user.name),
                    "**{}**, you remind me of Huskie. Get out of here!".format(user.name),
                    "**{}**'s are trash.".format(user.name),
                    "**{}**, you're a great shower when you speak.".format(user.name),
                    "I can't breathe when I see you, **{}**. Because I'm suffocating from your bullshit.".format(user.name),
                    "**{}**, the only way you'll ever get laid is if you crawl up a chicken's ass and wait.".format(user.name),
                    "**{}**, I just stepped in something that is smarter than you. It smelled better too.".format(user.name),
                    "**{}**, you're as stupid as your father when he thought he didn't need a condom.".format(user.name),
                    "**{}**, it's a joke, not a dick. You don't have to take it so hard.".format(user.name),
                    "**{}**, the only thing that would fuck you is life.".format(user.name),
                    "What's the difference between 3 dicks and a joke? **{}** can't take a joke.".format(user.name),
                    "**{}**, you have more dick in your personality than in your pants.".format(user.name),
                    "**{}**, even your father would be disappointed in your if he stayed.".format(user.name),
                    "**{}** should put a condom on their head. Cause if they're gonna act like a dick, they might as well dress like one too.".format(user.name),
                    "**{}**, you were probably birthed out of your mother's ass cause her pussy was too busy.".format(user.name),
                    "**{}** is such a pussy that fucking them wouldn't be gay.".format(user.name),
                    "If I wanted to kill myself, I'd climb up your ego and jump into your IQ, **{}**.".format(user.name),
                    "If laughter is the best medicine, **{}**'s face must be curing the world.".format(user.name),
                    "**{}**, your family tree is probably a cactus. Cause everyone on it is a prick.".format(user.name),
                    "**{}** is so ugly that when they look in the mirror, their reflection looks away.".format(user.name),
                    "**{}**, it's better to let someone think you're stupid than open your mouth and prove it.".format(user.name),
                    "**{}**, you're so ugly that you have to trick or treat over the phone.".format(user.name),
                    "**{}**, you're so fat that your school photo was a double picture.".format(user.name),
                    "**{}** is so stupid that they called me to ask me for my phone number.".format(user.name),
                    "**{}** is hating themselves too much for me to roast them.".format(user.name),
                    "**{}** is so fat that Thanos had to snap twice.".format(user.name),
                    "**{}**'s hair looks like a virginity helmet.".format(user.name)]
            embed.description = "{} {}".format(roast_e, random.choice(msgs))
            await client.say(embed=embed)           
          
# }eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if args == None:
            embed.description = "{} Please ask me a question.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 200:
            embed.description = "{} The question cannot be longer than 200 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = ":grey_question: `Question`:\n**{}**: {}\n\n:8ball: `Answer`:\n**{}**: {}".format(ctx.message.author.name, args, client.user.name, random.choice(eb))
            await client.say(embed=embed)

# }pfp
@client.command(pass_context=True)
async def pfp(ctx):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        try:
            a = []
            for i in client.servers:
                a.append(i.id)
            server = client.get_server(random.choice(a))
            b = []
            for i in server.members:
                if not i.bot:
                    b.append(i.id)
            user = await client.get_user_info(random.choice(b))
            embed.description = "Here is **{}**'s profile picture, I found it from **{}**.".format(user.name, server.name)
            embed.set_image(url=user.avatar_url)
            await client.say(embed=embed)
        except:
            embed.description = "{} An unknown error occurred.".format(error_e)
            await client.say(embed=embed)

# }calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if args == None:
            embed.description = "{} Please give a simple math problem for me to solve.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 100:
            embed.description = "{} The math problem cannot be longer than 100 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                embed.description = "{} Problem: `{}`\n{} Answer: `{}`".format(calculator_e, args, calculator_e, eval(args))
                await client.say(embed=embed)
            except:
                embed.description = "{} I'm having trouble solving that math problem.".format(error_e)
                await client.say(embed=embed)

# }battle <user>
@client.command(pass_context=True)
async def battle(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if user == None:
            embed.description = "{} Please mention the user you want to battle.".format(error_e)
            await client.say(embed=embed)
        elif user.id == ctx.message.author.id:
            embed.description = "{} You can't battle yourself.".format(error_e)
            await client.say(embed=embed)
        else:
            author = ctx.message.author
            u_health = []
            a_health = []
            rounds = []
            for i in range(1000):
                a_health.append(".")
                u_health.append(".")
            dmgs = {"punches the opponent! :right_facing_fist:" : random.randint(50, 70),
                    "kicks the opponent! :boot:" : random.randint(55, 75),
                    "grabs and throws the opponent on the ground! :raised_hands:" : random.randint(65, 85),
                    "stabs the opponent! :dagger:" : random.randint(75, 95),
                    "shoots the opponent! :gun:" : random.randint(90, 110),
                    "cuts the opponent! :knife:" : random.randint(65, 85),
                    "hits the opponent with a hammer! :hammer_pick:" : random.randint(75, 95),
                    "attacks the opponent with dark magic! :skull_crossbones:" : random.randint(280, 300),
                    "chokes the opponent using chains! :chains:" : random.randint(65, 85),
                    "casts a spell on the opponent! :sparkles:" : random.randint(155, 175),
                    "pukes on the opponent! :nauseated_face:" : random.randint(50, 70),
                    "scares the opponent! :ghost:" : random.randint(50, 70),
                    "summons a demon to attack the opponent! :smiling_imp:" : random.randint(275, 295),
                    "calls a rabot to attack the opponent! :robot:" : random.randint(125, 145),
                    "farts at the opponent! :dash:" : random.randint(50, 70),
                    "creates a tornado behind the opponent! :cloud_tornado:" : random.randint(130, 150),
                    "summons a meteor above the opponent! :comet:" : random.randint(210, 230),
                    "strikes the opponent with lightning! :zap:" : random.randint(200, 220),
                    "freezes the opponent! :snowflake:" : random.randint(140, 160),
                    "throws a bomb at the opponent! :bomb:" : random.randint(150, 170),
                    "drives over the opponent! :red_car:" : random.randint(110, 130),
                    "stuns the opponent! :dizzy:" : random.randint(60, 80),
                    "uses ear-rape to deafen the opponent! :ear:" : random.randint(50, 70),
                    "poisons the opponent! :syringe:" : random.randint(200, 220),
                    "set the opponent on fire! :fire:" : random.randint(170, 190),
                    "made the opponent not feel so good! :boom:" : random.randint(225, 245),
                    "stole the opponent's memes! :100:" : 420,
                    "deleted the opponent's hentai collections! :no_entry:" : 69,
                    "banned the opponent's memes! :no_entry_sign:" : random.randint(55, 75),
                    "pushed the opponent in the toilet! :toilet:" : 1}
            attacks = ["punches the opponent! :right_facing_fist:",
                       "kicks the opponent! :boot:",
                       "grabs and throws the opponent on the ground! :raised_hands:",
                       "stabs the opponent! :dagger:",
                       "shoots the opponent! :gun:",
                       "cuts the opponent! :knife:",
                       "hits the opponent with a hammer! :hammer_pick:",
                       "attacks the opponent with dark magic! :skull_crossbones:",
                       "chokes the opponent using chains! :chains:",
                       "casts a spell on the opponent! :sparkles:",
                       "pukes on the opponent! :nauseated_face:",
                       "scares the opponent! :ghost:",
                       "summons a demon to attack the opponent! :smiling_imp:",
                       "calls a rabot to attack the opponent! :robot:",
                       "farts at the opponent! :dash:",
                       "creates a tornado behind the opponent! :cloud_tornado:",
                       "summons a meteor above the opponent! :comet:",
                       "strikes the opponent with lightning! :zap:",
                       "freezes the opponent! :snowflake:",
                       "throws a bomb at the opponent! :bomb:",
                       "drives over the opponent! :red_car:",
                       "stuns the opponent! :dizzy:",
                       "uses ear-rape to deafen the opponent! :ear:",
                       "poisons the opponent! :syringe:",
                       "set the opponent on fire! :fire:",
                       "made the opponent not feel so good! :boom:",
                       "stole the opponent's memes! :100:",
                       "deleted the opponent's hentai collections! :no_entry:",
                       "banned the opponent's memes! :no_entry_sign:",
                       "pushed the opponent in the toilet! :toilet:"]
            title = "{} **__`D E A T H    B A T T L E`__** {}\n**{}**\n:vs:\n**{}**".format(battle_e, battle_e, author.name, user.name)
            s = "**~~`=====`~~**"
            embed.description = "{}\n{} **HEALTH** {}\n:small_red_triangle_down: **{}**\n:heart: `1000` HP\n\n:small_red_triangle_down: **{}**\n:heart: `1000` HP".format(title, s, s, author.name, user.name)
            h = await client.say(embed=embed)
            for i in range(1000):
                if len(a_health) == 0 or len(u_health) == 0:
                    await asyncio.sleep(float(5))
                    if len(a_health) > len(u_health):
                        embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: WINNER: **{}**\n:heart: `{}` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, author.name, len(a_health), user.name)
                    elif len(a_health) < len(u_health):
                        embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: WINNER: **{}**\n:heart: `{}` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, user.name, len(u_health), author.name)
                    else:
                        p = random.randint(0, 1)
                        if p == 0:
                            embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: RANDOM WINNER: **{}**\n:heart: `0` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, author.name, user.name)
                        else:
                            embed.description = "{}\n{} **BATTLE OVER** {}\n:crown: RANDOM WINNER: **{}**\n:heart: `0` HP\n\n:poop: LOSER: **{}**\n:heart: `0` HP".format(title, s, s, user.name, author.name)
                    await client.edit_message(h, embed=embed)
                    break
                else:
                    await asyncio.sleep(float(5))
                    rounds.append("+1")
                    u_d = random.choice(attacks)
                    a_d = random.choice(attacks)
                    for u in range(dmgs[u_d]):
                        if len(a_health) != 0:
                            a_health.remove('.')
                    for u in range(dmgs[a_d]):
                        if len(u_health) != 0:
                            u_health.remove('.')
                    embed.description = "{}\n{} **ROUND {}** {}\n:small_red_triangle_down: **{}** {}\n:arrow_right: `{}` DMG\n\n:small_red_triangle_down: **{}** {}\n:arrow_right: `{}` DMG\n{} **HEALTH** {}\n:small_red_triangle_down: **{}**\n:heart: `{}` HP\n\n:small_red_triangle_down: **{}**\n:heart: `{}` HP".format(title, s, len(rounds), s, author.name, a_d, dmgs[a_d], user.name, u_d, dmgs[u_d], s, s, author.name, len(a_health), user.name, len(u_health))
                    await client.edit_message(h, embed=embed)

# }dicklength [user]
@client.command(pass_context=True)
async def dicklength(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if user == None:
            author = ctx.message.author
        else:
            author = user
        c = []
        for i in dicks:
            a = i.split(' | ')
            if a[0] == author.id:
                p = int(a[1])
                c.append("+1")
                break
        if len(c) == 0:
            p = random.randint(0, 101)
            await client.send_message(client.get_channel(dicks_chnl), "{} | {}".format(author.id, p))
            dicks.append("{} | {}".format(author.id, p))
        if p <= 5:
            embed.description = "{} I'm sorry, **{}**. Your dick ran away.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        elif p <= 10:
            embed.description = "{} I'm sorry, **{}**. Your dick fell off.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        elif p >= 90:
            embed.description = "{} **{}**'s dick is too big for me to take the length of it.".format(dicklength_e, author.name)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}**'s dick is {}cm long.".format(dicklength_e, author.name, p)
            await client.say(embed=embed)

# }howgay [user]
@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0xffa3a3)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    elif ctx.message.author.id in banned_users:
        embed.description = "{} You are on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    elif ctx.message.server.id in banned_servers:
        embed.description = "{} This server is on the ban list and cannot use this bot.".format(noperms_e)
        await client.say(embed=embed)
    else:
        if user == None:
            author = ctx.message.author
        else:
            author = user
        c = []
        for i in howgays:
            a = i.split(' | ')
            if a[0] == author.id:
                p = int(a[1])
                c.append("+1")
                break
        if len(c) == 0:
            p = random.randint(0, 101)
            await client.send_message(client.get_channel(gays_chnl), "{} | {}".format(author.id, p))
            howgays.append("{} | {}".format(author.id, p))
        if p <= 5:
            embed.description = "{} **{}** is hella fucking gay.".format(howgay_e, author.name)
            await client.say(embed=embed)
        elif p <= 10:
            embed.description = "{} **{}** is not gay at all.".format(howgay_e, author.name)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}** is {}% gay.".format(howgay_e, author.name, p)
            await client.say(embed=embed)                      
                      
##################################
client.run(os.environ['BOT_TOKEN'])
