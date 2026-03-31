import requests

def get_price():
    # Getting SOL price from Binance
    r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT")
    price = round(float(r.json()['price']), 2)
    return f"  SOL/USDT: ${price} (Live Update)"

def update_readme():
    with open("README.md", "r") as f:
        lines = f.readlines()

    with open("README.md", "w") as f:
        for line in lines:
            if "SOL_PRICE" in line:
                f.write(get_price() + "\n")
            else:
                f.write(line)

if __name__ == "__main__":
    update_readme()
  
