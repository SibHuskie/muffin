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
             "zero" : ["zero is actually a girl", "zero should really take a shower", "zero's ass is flatter than earth", "aint zero gay?"],
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

loading_e = "<a:loading:484705261609811979>"
slotsgif1_e = "<a:slotsgif1:519832184039669760>"
slotsgif2_e = "<a:slotsgif2:519832184622940160>"
slotsgif3_e = "<a:slotsgif3:519832184383733761>"
slotsgif4_e = "<a:slotsgif4:519832184123686922>"
error_e = "<:error:515909294575845406>"
bug_e = "<:bug1:515909292491014144>"
close_e = "<:close:515909294818983936>"
log_e = "<:log:515909294818983936>"
msg_e = "<:msg:515909301051850753>"
noperms_e = "<:noperms:515909299461947402>"
pingbad_e = "<:pingbad:515911795307970565>"
pinggood_e = "<:pinggood:515911795492257793>"
pingok_e = "<:pingok:515911795693715476>"
reload_e = "<:reload:515909299755548672>"
servers_e = "<:servers:515909300271448080>"
support_e = "<:support:515909300275904512>"
users_e = "<:users:515909300334362624>"
worked_e = "<:worked:516244345473597470>"
check_e = "<:check:515909294042906665>"
interactions_e = "<:interactions:515909296043851796>"
game_e = "<:game:515909300338556928>"
battle_e = "<:battle:515909292403195914>"
messages_e = "<:messages:515909299495763968>"
bannedservers_e = "<:bannedservers:515909292101074945>"
bannedusers_e = "<:bannedusers:515909292419973130>"
cointoss_e = "<:cointoss:515909300393213972>"
suicide_e = "<:suicide:515909300347207680>"
roast_e = "<:roast:515909300330299392>"
calculator_e = "<:calculator:515909292545802240>"
ship_e = "<:ship1:515909300984741898>"
kill_e = "<:kill:515909300149944321>"
rate_e = "<:rate:515909299793428501>"
dicklength_e = "<:dicklength:515909294546485248>"
howgay_e = "<:howgay:515909296043589633>"
suggestion_e = "<:suggestion:515909299914932250>"
coins_e = "<:coins:515909294059814913>"
divorce_e = "<:divorce:515909294080786434>"
marriage_e = "<:marriage:515909297272651794>"
convert_e = "<:convert:515909300330430476>"
slots_e = "<:slots:515909300196212747>"
on_e = "<:on1:515911795836321802>"
off_e = "<:off:515911795454509057>"
ignored_e = "<:ignored:515909296303767552>"
work_e = "<:work:519837021850566667>"
generator_e = "<:generator:519841353077751809>"
steal_e = "<:steal:519845656928452632>"
gift_e = "<:gift1:519849587100614658>"
ban_e = "<:ban:519859483330215936>"
link_e = "<:link1:520593270494199819>"

started = []
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
    
##################################
client.run(os.environ['BOT_TOKEN'])
