from boosting import *
import httpx, random, time, datetime, json, os, hashlib
from keyauth import *
from pystyle import Colors, Colorate
if os.name == 'nt':
    import ctypes
import webbrowser

def cls(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')
webbrowser.open('https://guns.lol/itssynth', new = 2)
if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Synth Boost Tool | github.com/itssynth")
else:
    pass
    
config = json.load(open("config.json", encoding="utf-8"))

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
                     guns.lol/itssynth | t.me/sshsynth                                                                                  
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
