from solana.keypair import Keypair
from solana.rpc.api import Client
import requests
import json

client = Client("https://api.mainnet-beta.solana.com ")

def launch_token(dev_wallet, name, symbol, metadata):
    url = "https://pump.fun/api/create "
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": name,
        "symbol": symbol,
        "metadata": metadata,
        "creator": str(dev_wallet.pubkey()),
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["mint"]
    else:
        raise Exception("Token creation failed:", response.text)
