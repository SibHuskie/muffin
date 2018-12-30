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
           
##################################
client.run(os.environ['BOT_TOKEN'])
