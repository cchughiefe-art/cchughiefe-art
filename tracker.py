import requests
import os

def update():
    try:
        # 1. Get the price
        print("Fetching SOL price...")
        r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT", timeout=15)
        price = round(float(r.json()['price']), 2)
        status_line = f"  SOL/USDT: ${price} (Live Update)\n"
        
        # 2. Locate README (handles pathing issues in GitHub Actions)
        file_path = "README.md"
        
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.readlines()
        else:
            print("README.md not found, creating a new one.")
            lines = ["# Profile \n\n"]

        # 3. Update or Append the price
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
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    update()
    
