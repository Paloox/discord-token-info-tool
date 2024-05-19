# Made by https://github.com/Paloox
# You have a question? add me on discord: p4u1_

import requests
import os
from colorama import Fore
from time import sleep
import win32gui
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 100, 0, 1220, 850, True)

os.system("title Token Info Tool - by p4u1_")

def get_info(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    try:
        res = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if res.status_code == 200:
            user_data = res.json()

            id = user_data['id']
            username = user_data['username']
            avatar = user_data['avatar']
            global_name = user_data['global_name']
            mfa_enabled = user_data['mfa_enabled']
            language = user_data['locale']
            email = user_data['email']
            phone = user_data['phone']

            avatar_url = f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png"
            
            max_length = 120


            
            centered_text = "User Info"
            centered_text_length = len(centered_text)
            
            
            padding = (max_length - centered_text_length) // 2
            
            
            print(Fore.LIGHTYELLOW_EX + f"+{'=' * padding}{Fore.LIGHTCYAN_EX}{centered_text}{Fore.LIGHTYELLOW_EX}{'=' * (max_length - padding - centered_text_length)}+" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}ID: {Fore.RESET}{id}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Username: {Fore.RESET}{username}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Avatar URL: {Fore.RESET}{avatar_url}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Global Name: {Fore.RESET}{global_name}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}2FA/MFA Enabled: {Fore.RESET}{mfa_enabled}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Language: {Fore.RESET}{language}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Email: {Fore.RESET}{email}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Phone: {Fore.RESET}{phone}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + "+" + "=" * (max_length) + "+" + Fore.RESET)
            print(" ")


            res_billing = requests.get('https://discord.com/api/users/@me/billing/payment-sources', headers=headers)
            billing_data = res_billing.json()

            if billing_data:
                billing_email = billing_data[0].get('email')
                payment_method = "Card" if billing_data[0].get('payment_gateway') == 1 else "PayPal" if billing_data[0].get('payment_gateway') == 2 else "Unknown"
                billing_address = billing_data[0].get('billing_address')
                name = billing_address.get('name')
                address_line_1 = billing_address.get('line_1')
                address_line_2 = billing_address.get('line_2')
                city = billing_address.get('city')
                state = billing_address.get('state')
                country = billing_address.get('country')
                postal_code = billing_address.get('postal_code')

                max_length = 120
                centered_text = "Billing Info"
                centered_text_length = len(centered_text)
                padding = (max_length - centered_text_length) // 2

                print(Fore.LIGHTYELLOW_EX + f"+{'=' * padding}{Fore.LIGHTCYAN_EX}{centered_text}{Fore.LIGHTYELLOW_EX}{'=' * (max_length - padding - centered_text_length)}+" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Billing Email: {Fore.RESET}{billing_email}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Payment Method: {Fore.RESET}{payment_method}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Name: {Fore.RESET}{name}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Address Line 1: {Fore.RESET}{address_line_1}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Address Line 2: {Fore.RESET}{address_line_2}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}City: {Fore.RESET}{city}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|")
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}State: {Fore.RESET}{state}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|")
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Country: {Fore.RESET}{country}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|")
                print(Fore.LIGHTYELLOW_EX + f"| {Fore.LIGHTCYAN_EX}Postal Code: {Fore.RESET}{postal_code}".ljust(max_length + 10) + f" {Fore.LIGHTYELLOW_EX}|" + Fore.RESET)
                print(Fore.LIGHTYELLOW_EX + "+" + "=" * (max_length) + "+")

                input(Fore.LIGHTGREEN_EX + "Press Enter To Continue" + Fore.RESET)
                os.system("cls")
                main()
            else:
                os.system("title No Billing Information Found")
                print(Fore.LIGHTRED_EX + "No Billing Information Found" + Fore.RESET)
                input(Fore.LIGHTGREEN_EX + "Press Enter To Continue" + Fore.RESET)
                os.system("cls")
                main()
        else:
            os.system("title Invalid Token")
            print(Fore.LIGHTRED_EX + "Invalid Token" + Fore.RESET)
            sleep(3)
            os.system("cls")
            main()
    except requests.exceptions.RequestException as e:
        os.system("title Invalid Token")
        print(Fore.LIGHTRED_EX + "Invalid Token" + Fore.RESET)
        sleep(3)
        os.system("cls")
        main()

def main():
    os.system("title Token Info Tool - by Paloox")
    os.system("cls")
    print(fr"{Fore.LIGHTMAGENTA_EX} _____                                                                               _____ {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}( ___ )-----------------------------------------------------------------------------( ___ ){Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |                                                                               |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ██▓ ███▄    █   █████▒▒█████   |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   | ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |   ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░ |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░  |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |     ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░  |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |   ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒   |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |   |              ░ ░  ░  ░      ░  ░         ░     ░           ░            ░ ░   |   | {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX} |___|                         Made by https://github.com/Paloox                     |___| {Fore.RESET}")
    print(fr"{Fore.LIGHTMAGENTA_EX}(_____)-----------------------------------------------------------------------------(_____){Fore.RESET}")
    
    print("")

    token = input(f"{Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.LIGHTGREEN_EX}Token: " + Fore.RESET)
    print(" ")
    get_info(token)

if __name__ == "__main__":
    main()