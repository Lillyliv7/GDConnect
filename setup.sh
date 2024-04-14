#!/bin/bash

echo "GDConnect setup script\n"
echo "Make sure you have Guilded and Discord bots with full permissions' tokens ready"
echo "The Discord bot must also have \"Message Content Intent\" turned on in the Discord Developer Portal"
echo "Press enter to continue"
read nothing

pip install python-dotenv
pip install asyncio

echo -n "Enter your Guilded token: " 
read guilded
echo "# .env\nGUILDED_TOKEN=$guilded\n" > .envGuilded
echo -n "Enter your Discord token: " 
read discord
echo "# .env\nDISCORD_TOKEN=$discord\n" > .envDiscord

python3 main.py
