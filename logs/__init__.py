# logs
import builtins
import logging
import os
from logging.handlers import TimedRotatingFileHandler

log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

log_file = os.path.join(log_folder, 'pokemon_fusion_bot.log') 

timed_handler = TimedRotatingFileHandler(log_file, when='d', interval=1, backupCount=10)

logging.basicConfig(
    # filename=log_file, 
    encoding='utf-8', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)-8s - %(filename)13s:%(lineno)-4d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[timed_handler]
)

builtins.logging = logging