import requests
import os

def update():
    try:
        print("Fetching SOL price...")
        # 1. Fetch data from Binance
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT", timeout=20)
        data = r.json()

        # Check if 'price' is actually in the response
        if 'price' in data:
            price = round(float(data['price']), 2)
            status_line = f"  SOL/USDT: ${price} (Live Update)\n"
            print(f"Price found: {price}")
        else:
            print(f"API Error: {data}")
            return # Stop here if the API is acting up

        # 2. Locate README
        file_path = "README.md"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.readlines()
        else:
            lines = ["# Profile \n\n"]

        # 3. Update or Append
        new_lines = []
        found = False
        for line in lines:
            if "SOL_PRICE" in line or "SOL/USDT:" in line:
                new_lines.append(status_line)
                found = True
            else:
                new_lines.append(line)
        
        if not found:
            new_lines.append("\n" + status_line)

        # 4. Save
        with open(file_path, "w") as f:
            f.writelines(new_lines)
        print("Successfully updated README.md")
            
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    update()
    
