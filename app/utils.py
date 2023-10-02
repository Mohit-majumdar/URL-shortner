import requests

def get_location_from_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return f"{data.get('city')},{data.get('country')}"
    else:
        return None
    
def get_ip(request):
    client_ip = request.META.get("REMOTE_ADDR")
    return client_ip