import requests
import time
import os
from colorama import init, Fore

# Initialize Colorama (Fix for Color Codes Not Showing Properly)
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    clear_screen()
    logo_lines = [
        ("╭──────────────────── < ~ ᴍᴜʟᴛɪ ᴄᴏɴᴠᴏ ᴛᴏᴏʟ ~ > ──────────────────╮", Fore.CYAN),
        ("│                                                                │", Fore.YELLOW),
        ("│                       ᴀʟᴇx ᴛᴏᴏʟ ʀᴜɴɴɪɪɴɢ                       │", Fore.YELLOW),
        ("│                                                                │", Fore.YELLOW),
        ("╰────────────────────────< ~ ᴀʟᴇx   ᴛᴏᴏʟ ~  >────────────────────╯", Fore.CYAN),
        ("╔════════════════════════════════════════════════════════════════╗", Fore.YELLOW),
        ("║  NAME       : ᴀʟᴇx                                             ║", Fore.CYAN),
        ("║  RULLEX     : ＥＲＲＯＲ                                       ║", Fore.GREEN),
        ("║  FORM       : ＥＲＲＯＲ                                       ║", Fore.CYAN),
        ("║  BRAND      : ᴍᴜʟᴛɪ-ᴄᴏɴᴠᴏ                                      ║", Fore.GREEN),
        ("║  GitHub     : ＥＲＲＯＲ                                       ║", Fore.CYAN),
        ("║  TOOL       : For convo loader                                 ║", Fore.GREEN),
        ("╚════════════════════════════════════════════════════════════════╝", Fore.YELLOW),
    ]

    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

    typing_effect("<<━━━━━━━━━━━━━━━━━━<< Running Tool >>━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<═════════════════════════════════════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:                                                                                                                                                                                 response = requests.get(pastebin_url)
        response.raise_for_status()                                                                                                                                                      return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def fetch_profile_name(access_token):                                                                                                                                                try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})                                                                                  response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException:
        return "Unknown Target"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    token_profiles = {token: fetch_profile_name(token) for token in tokens}
    target_profile_name = fetch_target_name(target_id, tokens[0])

    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

                print(Fore.YELLOW + f"\n<<══════════════════════════════════════════════════════════════════════>>")
                print(Fore.CYAN + f"[+] MESSAGE {message_index + 1} SUCCESSFULLY SENT!")
                print(Fore.CYAN + f"[+] SENDER: {Fore.WHITE}{sender_name}")
                print(Fore.CYAN + f"[+] TARGET: {Fore.WHITE}{target_profile_name} ({target_id})")
                print(Fore.CYAN + f"[+] MESSAGE: {Fore.LIGHTGREEN_EX}{full_message}")
                print(Fore.CYAN + f"[+] TIME: {Fore.LIGHTWHITE_EX}{current_time}")
                print(Fore.YELLOW + f"<<═══════════════════════════════════════════════════════════════════════>>\n")

            except requests.exceptions.RequestException:
                continue

            time.sleep(speed)

        print(Fore.CYAN + "\n[+]  process...\n")

def main():
    clear_screen()
    display_animated_logo()

    entered_password = animated_input("ENTER OWNER NAME")

    if entered_password != "Alex":  # OWNER NAME UPDATED HERE
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting program.")
        exit(1)

    tokens_file = animated_input("  Accece Token Fiile :")
    target_id = animated_input("  Thread id :")
    haters_name = animated_input("  Haters Name :")
    messages_file = animated_input("  Loader Fiile")
    speed = float(animated_input("  Delay (in seconds) FOR MESSAGES "))

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
