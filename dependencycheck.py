import requests

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Success:", response.text)
    else:
        print("Failed to fetch URL")

if __name__ == "__main__":
    fetch_url("http://google.com")
