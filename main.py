from boosting import *
import httpx, random, time, datetime, json, os, hashlib
from keyauth import *
from pystyle import Colors, Colorate
if os.name == 'nt':
    import ctypes

def cls(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Synth Boost Tool")
else:
    pass
    
config = json.load(open("config.json", encoding="utf-8"))

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "Synth Boost Bot",
    ownerid = "EIUWOPtnF9",
    secret = "93d47ddd0c25a4ec4e5af0f8b71150c0de866aecf256f6d85d8ec4d1cb971cd4",
    version = "1.0",
    hash_to_check = getchecksum()
)

cls()

if keyauthapp.checkblacklist():
    print(Fore.BLUE + "You are blacklisted from our system." + Fore.BLUE)
    quit()
    
def validate():
    if keyauthapp.license(config["license_key"]):
        quit()
    else:
        print(Fore.BLUE + "Successfully Logged Into License | Created by sshsynth" + Fore.BLUE)
        time.sleep(2)
        

def answer():
    try:
        key = input(Fore.BLUE + """License Key: """+ Fore.RESET)
        x = {"license_key": key}
        config.update(x)
        json.dump(config, open("config.json", "w"), indent = 4)

    except KeyboardInterrupt:
        os._exit(1)

if "license_key" not in str(config):
    answer()

validate()


def getinviteCode(invite_input): #gets invite CODE
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

def menu():
    print(Colorate.Vertical(Colors.purple_to_blue, """
      ╔═╗╦ ╦╔╗╔╔╦╗╦ ╦
      ╚═╗╚╦╝║║║ ║ ╠═╣
      ╚═╝ ╩ ╝╚╝ ╩ ╩ ╩  
╔╗ ╔═╗╔═╗╔═╗╔╦╗  ╔╦╗╔═╗╔═╗╦  
╠╩╗║ ║║ ║╚═╗ ║    ║ ║ ║║ ║║  
╚═╝╚═╝╚═╝╚═╝ ╩    ╩ ╚═╝╚═╝╩═╝
═════════════════════════════                                                                                  
                                                                                   
1. Boost Server
2. View Stock
          """, 1))
    
    choice = input(f"{Fore.BLUE}[>] " + Fore.RESET)
    
    if choice == "1":
        invite = getinviteCode(input(f"{Fore.BLUE}Invite Link/Code (Example: discord.gg/Synth): {Fore.CYAN}"))
        amount = input(f"{Fore.BLUE}Amount of Boosts: {Fore.BLUE}")
        while amount.isdigit() != True:
            print(Fore.CYAN + "Amount cannot be a string." + Fore.RESET)
            amount = input(f"{Fore.BLUE}Amount of Boosts: {Fore.BLUE}")
        months = input(f"{Fore.BLUE}Number of months: {Fore.BLUE}")
        while amount.isdigit() != True:
            print(Fore.BLUE + "Months cannot be a string." + Fore.RESET)
            months = input(f"{Fore.BLUE}Number of months: {Fore.BLUE}")
        start = time.time()
        boosted = thread_boost(invite, int(amount), int(months), config['nickname'])
        end = time.time()
        print()
        sprint(f"Boosted https://discord.gg/{invite} {variables.boosts_done} times in {round(end - start, 2)} seconds.", True)
        print()
        input(Fore.RED + "Press enter to return to menu" + Fore.RESET)
        cls()
        menu()
        
    if choice == "2":
        print(f'{Fore.GREEN}1 Month Nitro Tokens: {len(open("input/1m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Fore.GREEN}1 Month Boosts: {len(open("input/1m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        print(f'{Fore.GREEN}3 Month Nitro Tokens: {len(open("input/3m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Fore.GREEN}3 Month Nitro Tokens: {len(open("input/3m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        input(Fore.RED + "Press enter to return to menu" + Fore.RESET)
        cls()
        menu()
        
    if choice == "3":
        quit()
        
if __name__ == "__main__":
    cls()
    menu()
