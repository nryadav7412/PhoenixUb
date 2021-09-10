from PhoenixUb import phoenixub 
import logging  
import PhoenixUb.modules 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

logger = logging.getLogger("__name__")

print("Starting....")
phoenixub.start()
phoenixub.run_until_disconnected()
