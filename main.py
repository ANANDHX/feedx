from FunctionData.somefun import*
from instabot import*
from time import sleep
import random

bot = Bot(
    min_likes_to_like=1,
    max_likes_to_like=10,
    like_delay=9,
    max_likes_per_day=250
    )

console_clear()
print('\u001b[31;1m                                                                                   '),time.sleep(.1)
print('   █████  ███    ██  █████  ███    ██ ██████  ██   ██ ██    ██ '),time.sleep(.1)
print('  ██   ██ ████   ██ ██   ██ ████   ██ ██   ██ ██   ██ ██    ██'),time.sleep(.1)
print('  ███████ ██ ██  ██ ███████ ██ ██  ██ ██   ██ ███████ ██    ██ \u001b[0m'),time.sleep(.1)
print('  ██   ██ ██  ██ ██ ██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██  \u001b[0m'),time.sleep(.1)
print('  ██   ██ ██   ████ ██   ██ ██   ████ ██████  ██   ██  ██████ \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print('\u001b[32mOwner:⚙️  αηαη∂нυ  🤖🔒           Last Update: 19.11.2021\u001b[0m'),time.sleep(.1)
print('\u001b[33;1m                                                                           \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m                   𝒻Ẹ𝐄Ｄ LI𝕂ε𝔯        \u001b[0m'),time.sleep(.1)

print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print(' [🐞] L O G I N')
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)

USERNAME = input("\u001b[32m[+]\u001b[0m Enter username:-")
PASSWORD = input("\u001b[32m[+]\u001b[0m Enter password:-")

print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
bot.login(username=USERNAME, password=PASSWORD, use_cookie=False)
console_clear()

print('\u001b[31;1m                                                                                   '),time.sleep(.1)
print('   █████  ███    ██  █████  ███    ██ ██████  ██   ██ ██    ██ '),time.sleep(.1)
print('  ██   ██ ████   ██ ██   ██ ████   ██ ██   ██ ██   ██ ██    ██'),time.sleep(.1)
print('  ███████ ██ ██  ██ ███████ ██ ██  ██ ██   ██ ███████ ██    ██ \u001b[0m'),time.sleep(.1)
print('  ██   ██ ██  ██ ██ ██   ██ ██  ██ ██ ██   ██ ██   ██ ██    ██  \u001b[0m'),time.sleep(.1)
print('  ██   ██ ██   ████ ██   ██ ██   ████ ██████  ██   ██  ██████ \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m-----------------------------------------------------------------\u001b[0m'),time.sleep(.1)
print('\u001b[32mOwner:⚙️  αηαη∂нυ 🤖🔒           Last Update: 19.11.2021\u001b[0m'),time.sleep(.1)
print('\u001b[33;1m                                                                           \u001b[0m'),time.sleep(.1)
print('\u001b[33;1m                 𝒻Ẹ𝐄Ｄ LI𝕂ε𝔯 >-       \u001b[0m'),time.sleep(.1)

while True:
    bot.like_timeline(amount=None)
    delay_counter(random.randint(15,16))
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[00m')
