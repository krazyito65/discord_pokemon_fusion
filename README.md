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
owner of the application needs to sync the bot.  In a private channel run the following after the bot as been added to needed servers.
```
!sync
```
once sync is completed, the slash command should work
```
/fuse mon1 mon2
```

discord slash command sync info: https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f

---
## Container Info
This project supports running in a container that is built before runtime (It's not hosted on a repo). 
It is built from the `python:3.11` base image.

### 1. Build
Run the following from the root repo directory to build a local image.
```sh
docker image build -t discord_pokemon_fusion_bot:latest .
```
### 2. Configure and Run
Initialize your `token.yml` file in your local repo directory. This file will be copied as a secret to the container runtime. See above steps for details on the content.

You can launch the container via a raw docker run command or use docker-compose if you have it installed. 

Docker-compose is recommended if available.

Alternatively, if you have docker installed already you can simply run
`./run_bot.sh`
#### Docker Compose
```sh
# Startup
docker-compose up -d

# Shutdown
docker-compose down
```

#### Docker Run
```sh
docker run -d -it --name poke-fusion-bot --mount type=bind,source="$(pwd)/token.yml,target=/app/token.yml" \
    -e PYTHONUNBUFFERED="1" discord_pokemon_fusion_bot:latest

# Shutdown and Remove (This deletes logs)
docker container stop poke-fusion-bot && docker container rm poke-fusion-bot
```

### 3. Logs
Logs can be viewed using `docker container logs <container_id> -f`. For example, if using docker-compose you could view the logs with `docker container logs discord_pokemon_fusion-fusion_bot-1 -f`
