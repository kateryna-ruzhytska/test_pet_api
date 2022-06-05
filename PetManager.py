from HttpConnection.HttpMethods import HttpMethods
from HttpConnection.HttpRequest import HttpRequest


class PetManager:

    URL = "https://petstore.swagger.io/v2"

    def find_pets_by_status(self, status):
        api_endpoint = "/pet/findByStatus"
        options = {
            "headers": {"Content-Type": "application/json;charset=UTF-8"},
            "params": {"status": f"{status}"}
        }
        response = HttpRequest.send_request(uri=f"{self.URL}{api_endpoint}", method=HttpMethods.GET, options=options)
        if response.status_code == 200:
            json_response = response.json()
        else:
            json_response = response.text
        print(f"Find by status '{status}': {json_response}")

    def add_new_pet(self):
        api_endpoint = "/pet"
        options = {
            "headers": {"Content-Type": "application/json;charset=UTF-8"},
            "data": {"id": 16,
                     "category": {"id": 16,
                                  "name": "Marik"},
                     "name": "Shih-tsu",
                     "photoUrls": ["string"],
                     "tags": [{"id": 0,
                               "name": "string"}],
                     "status": "available"}
        }
        response = HttpRequest.send_request(uri=f"{self.URL}{api_endpoint}", method=HttpMethods.POST, options=options)
        if response.status_code == 200:
            json_response = response.json()
        else:
            json_response = response.text
        print(f"Add new: {json_response}")

    def find_pet_by_id(self, pet_id):
        api_endpoint = f"/pet/{pet_id}"
        options = {
            "headers": {"Content-Type": "application/json;charset=UTF-8"}
        }
        response = HttpRequest.send_request(uri=f"{self.URL}{api_endpoint}", method=HttpMethods.GET, options=options)
        if response.status_code == 200:
            json_response = response.json()
        else:
            json_response = response.text
        print(f"Find by id: {json_response}")

    def delete_pet(self, pet_id):
        api_endpoint = f"/pet/{pet_id}"
        options = {
            "headers": {"Content-Type": "application/json;charset=UTF-8"}
        }
        response = HttpRequest.send_request(uri=f"{self.URL}{api_endpoint}", method=HttpMethods.DELETE, options=options)
        if response.status_code == 200:
            json_response = response.json()
        else:
            json_response = response.text
        print(f"Delete by id: {json_response}")
