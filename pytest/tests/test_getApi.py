import requests
import json
import pytest




class TestCases():

    BASEPATH = "http://127.0.0.1:8000/"   
    a = []

    def test_postData(self):
        url =  self.BASEPATH +'getdata/'
        params ={
            "name": "kamlesh",
            "last": "developer"
        }
        response = requests.post(url,data=params)
        print(response.status_code)
        print(response)
        data = response.json()
        self.a.append(str(data['id']))
        print(json.dumps(response.json(),indent=2))
        assert response.status_code == 201

    def test_getData(self):

        url =  self.BASEPATH +'getdata/'+self.a[0]
        response = requests.get(url)
        print(json.dumps(response.json(),indent=2))
        assert response.status_code == 200

    def test_putData(self):
        url =  self.BASEPATH +'getdata/'+self.a[0]
        params ={
            "name": "raja",
            "last": "developer"
        }
        response = requests.put(url,data=params)
        print(response.status_code)
        print(json.dumps(response.json(),indent=4))
        assert response.status_code == 200


    def test_deleteData(self):
        url =  self.BASEPATH +'getdata/'+self.a[0]
        response = requests.delete(url)
        print(response.status_code)
        assert response.status_code == 204