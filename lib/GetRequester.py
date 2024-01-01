import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
        pass

    def load_json(self):
        # result_list=[]
        results =json.loads(self.get_response_body())
        return results
        pass

req = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
out = req.get_response_body()
ind = req.load_json()
print(ind)