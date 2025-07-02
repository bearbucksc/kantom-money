import os
import json
from solana.keypair import Keypair
from solana.rpc.api import Client
from cryptography.fernet import Fernet

client = Client("https://api.mainnet-beta.solana.com ")
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def create_wallet():
    wallet = Keypair()
    wallet_path = f"keys/bundler-wallets/{wallet.pubkey()}.json"
    os.makedirs(os.path.dirname(wallet_path), exist_ok=True)
    with open(wallet_path, "wb") as f:
        encrypted = cipher_suite.encrypt(wallet.secret_key)
        f.write(encrypted)
    return wallet

def fund_wallet(from_wallet, to_pubkey, amount):
    balance = client.get_balance(from_wallet.pubkey()).value / 1e9
    if balance < amount:
        raise ValueError("Insufficient funds in funding wallet")
    tx = client.request_airdrop(to_pubkey, int(amount * 1e9))
    return tx
