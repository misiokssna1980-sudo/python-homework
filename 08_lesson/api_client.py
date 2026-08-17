import requests

class YougileProjectAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload: dict):
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get_projects(self):
        url = f"{self.base_url}/projects"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id: str, payload: dict):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=payload, headers=self.headers)
        return response