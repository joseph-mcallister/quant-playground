import os
from dotenv import load_dotenv
load_dotenv()
import ccxt

class Coinbase:

    def __init__(self):
        if os.getenv("ENV") != "PRODUCTION" and "sandbox" not in os.getenv("COINBASE_API_URL"): 
            raise "INCORRECT_ENVIRONMENT_VARIABLES"

        self.exchange = ccxt.coinbasepro({
            'apiKey': os.getenv("COINBASE_API_KEY"),
            'secret': os.getenv("COINBASE_SECRET"),
            'urls': {
                'api': {
                    'public': os.getenv("COINBASE_API_URL"),
                    'private': os.getenv("COINBASE_API_URL"),
                },
            },    
            'password':os.getenv("COINBASE_PASSWORD")
        })
    
        

    