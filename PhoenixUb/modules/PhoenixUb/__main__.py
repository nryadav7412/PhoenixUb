from PhoenixUb import rimuru, rafael
import logging  
import PhoenixUb.modules 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Starting....")
phoenixub.parse_mode = 'md'
phoenix.parse_mode = 'md'
phoenixub.start()
phoenixub.run_until_disconnected()
