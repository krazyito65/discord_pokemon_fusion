# discord_pokemon_fusion

![image](https://user-images.githubusercontent.com/479738/222197281-bc92dad2-6aa8-46e3-bc9f-c25e118f8f79.png)


Built using python 3.11

```
python3.11 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

ensure you have a 'token.yml' file with a single entry
```
dev_token: ######
```

----
owner of the application needs to sync the bot.  In a private channe run the following after the bot as been added to needed servers.
```
!sync
```
once sync is completed, the slash command should work
```
/fuse mon1 mon2
```
