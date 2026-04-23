import requests

def get_multiple_jokes(n):
    url = "https://official-joke-api.appspot.com/random_joke"
    
    jokes = []
    
    for i in range(n):
        try:
            response = requests.get(url, timeout=3)

            if response.status_code != 200:
                raise Exception("Bad response")

            data = response.json()
            jokes.append(data)

        except Exception as e:
            jokes.append({"error": str(e)})
    
    return jokes