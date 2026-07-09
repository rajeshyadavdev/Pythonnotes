import requests

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    
    try:
        response = requests.get(
          url, timeout=10)
        data = response.json()
        
        print("\n" + "="*30)
        print(f"  IP TRACKER RESULT")
        print("="*30)
        print(f"IP        : {data.get('ip', 'N/A')}")
        print(f"City      : {data.get('city', 'N/A')}")
        print(f"Region    : {data.get('region', 'N/A')}")
        print(f"Country   : {data.get('country', 'N/A')}")
        print(f"Location  : {data.get('loc', 'N/A')}")  # latitude,longitude
        print(f"Org/ISP   : {data.get('org', 'N/A')}")
        print(f"Timezone  : {data.get('timezone', 'N/A')}")
        print(f"Postal    : {data.get('postal', 'N/A')}")
        print("="*30 + "\n")
        
    except requests.exceptions.RequestException:
        print("Error: Internet connection problem")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Python IP Tracker ===")
    print("Type 'myip' to check your own public IP")
    print("Type 'exit' to quit\n")
    
    while True:
        ip = input("Enter IP address: ").strip()
        
        if ip.lower() == 'exit':
            print("Goodbye!")
            break
        elif ip.lower() == 'myip':
            ip = requests.get('https://api.ipify.org').text
            print(f"Your Public IP: {ip}")
        
        get_ip_info(ip)

if __name__ == "__main__":
    main()