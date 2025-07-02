from solana.transaction import Transaction
from solana.rpc.api import Client
from random import randint
import time

client = Client("https://api.mainnet-beta.solana.com ")

def execute_bundle_buy(mint_pubkey, wallet, delay=0):
    if delay > 0:
        time.sleep(delay)

    # Check if another wallet interacted
    sigs = client.get_signatures_for_address(mint_pubkey)
    if len(sigs) > 1:
        print("⚠️ Another wallet interacted. Aborting buy.")
        return

    # Execute buy
    tx = Transaction().add(
        transfer(
            from_pubkey=wallet.pubkey(),
            to_pubkey=mint_pubkey,
            lamports=int(0.1 * 1e9)
        )
    )
    client.send_transaction(tx, wallet)
    print("✅ Buy executed!")
