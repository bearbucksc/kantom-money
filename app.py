from flask import Flask, render_template, request, jsonify
from pump_launcher import launch_token
from wallet_manager import create_wallet, fund_wallet
from bundler import execute_bundle_buy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/launch-token", methods=["POST"])
def launch():
    data = request.json
    name = data["name"]
    symbol = data["symbol"]

    # Create token
    dev_wallet = load_wallet("keys/dev-wallet.json")
    mint = launch_token(dev_wallet, name, symbol, {})

    # Fund and execute bundle
    bundler_wallet = create_wallet()
    fund_wallet(load_wallet("keys/funding-wallet.json"), bundler_wallet.pubkey(), 0.2)
    execute_bundle_buy(mint, bundler_wallet, delay=5)

    return jsonify({"status": "success", "mint": mint})

if __name__ == "__main__":
    app.run()
