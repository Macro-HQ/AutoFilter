# AutoFilter

~~The original application was meant for a wider usage area, for multiple people, but ended up just giving up since people don't trust me with their vps's ips! (what a shocker)
Which should explain why I made the discord bot ("server") seperate from the "client"~~

Yeah I kinda copy pasted client to server. I don't know if it works hopefully someone tells me.

# Install
install.sh doesnt and I wont bother trying to fix it since everyone's linux is different

1. install `python3` and `pip3`
2. run `pip3 install -r requirements.txt`
3. `tmux`
4. run `python3 main.py`

you will only need to install it once. if your vps restarts, just do steps 3-4

# Usage
1. Go edit `config.yaml`
2. Create a discord bot (google it)
3. Create a private server with yourself in it
4. Follow the config channel and direct it to your private server
5. Copy the channel id (google it)
6. Paste it in `server_channel_id`
7. Generate the bot token
8. Paste it in `token`
9. Go to where your binmaster's webhook is
10. Copy it and paste it in `webhook_url`

Start it using: `tmux new-session -d -s bin 'python3 main.py'`

# Contact
Just make an issue [here](https://github.com/wtfismyname69420/AutoFilter/issues)
