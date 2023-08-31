# AutoFilter

~~The original application was meant for a wider usage area, for multiple people, but ended up just giving up since people don't trust me with their vps's ips! (what a shocker)
Which should explain why I made the discord bot ("server") seperate from the "client"~~

Works good... enough...

# Setup
## For now, this only works on Linux! Windows support will be added later... maybe.

## Discord Setup

1. Create a private server

![1](https://github.com/Macro-HQ/AutoFilter/assets/84185962/5264e1ea-1474-4144-9704-6a5e69f29e6a)

![2](https://github.com/Macro-HQ/AutoFilter/assets/84185962/4f53abff-9ffa-4153-ab84-623fb2d3727c)

![3](https://github.com/Macro-HQ/AutoFilter/assets/84185962/decf6b8e-7b72-4ce0-aaad-d51b2d067fcc)


3. Create a webhook

![4](https://github.com/Macro-HQ/AutoFilter/assets/84185962/637038d4-d268-44bc-9249-bb06851794de)

![5](https://github.com/Macro-HQ/AutoFilter/assets/84185962/84e49eff-2301-4a85-aa83-800f83cbbcc9)

![6](https://github.com/Macro-HQ/AutoFilter/assets/84185962/d0f4777e-a21e-4deb-bf97-fa8ac9f470d1)

![7](https://github.com/Macro-HQ/AutoFilter/assets/84185962/83633878-aa99-4429-ac9b-d0d9a3f63b8c)


5. Copy the webhook and paste it into the `config.yaml` file

![8](https://github.com/Macro-HQ/AutoFilter/assets/84185962/a89821b6-bd36-4abe-b5e9-6bfd6c9e39b8)


7. Enable developer mode (guide [here](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/)) and copy the channel ID

![9](https://github.com/Macro-HQ/AutoFilter/assets/84185962/e170e560-04e7-4c4c-89e5-66c827f50032)

![8](https://github.com/Macro-HQ/AutoFilter/assets/84185962/5f1c9775-5558-42d0-a7fc-606e860e9290)


9. Create a Discord bot

Visit the [Discord Developer Portal](https://discord.com/developers/applications/)

![1](https://github.com/Macro-HQ/AutoFilter/assets/84185962/46f87cd9-2714-451c-b8fa-d9ff3c45afb4)

![2](https://github.com/Macro-HQ/AutoFilter/assets/84185962/50d114b2-55ff-4403-b91e-5a8294634d5d)

![3](https://github.com/Macro-HQ/AutoFilter/assets/84185962/f9c372c4-1f02-444d-91fc-3e695e4cce69)

![4](https://github.com/Macro-HQ/AutoFilter/assets/84185962/3ca33c77-cc54-4b35-a73f-7dc35456ce7a)


11. Invite the bot

![5](https://github.com/Macro-HQ/AutoFilter/assets/84185962/44ce0b19-2bcd-40e7-bb6b-da98cf04cf7d)

![6](https://github.com/Macro-HQ/AutoFilter/assets/84185962/c37ab052-df3e-4359-a8ef-fa3ad77d61e2)

![7](https://github.com/Macro-HQ/AutoFilter/assets/84185962/c662802f-a0f7-4d2c-8a72-1a59308b7bf4)

13. Paste the URL into your browser and select your private server

14. Follow the config channel

![1](https://github.com/Macro-HQ/AutoFilter/assets/84185962/fbd1a846-437e-4fa9-a8d9-42508a2054ad)

![2](https://github.com/Macro-HQ/AutoFilter/assets/84185962/89485906-d156-4ff1-b9e5-fa32f0aa05bd)

## Server Setup

1. Google `how to install python3 for <your os>`
2. Install `python3` alongwith `pip3`
3. Once installed, `git clone https://github.com/Macro-HQ/AutoFilter/`
4. CD into the folder `cd AutoFilter-main`
5. Install discord.py with `pip3 install discord.py`
6. Give permission to the `start.sh` file with `chmod +x start.sh`
7. Start the AutoFilter with `./start.sh`

# Contact
If you have any suggestions or issues, create a issue on github or join our Discord [here](https://discord.gg/8FSJWpQBHk)! We are working on other things like slayer macro, auto dungeons!
