import requests
import pandas as pd
import json
class Connect:
    def __init__(self,email, password):
        self.email = email
        self.password = password

        self.settings=self.get_settings()
        
    def table(self,db,schema,tbl):
        # Define the API endpoint and query parameters
        url = 'http://54.166.184.183:5555/get_table'
        params = {
            'email': self.email,
            'password': self.password,
            'db': db,
            'schema': schema,
            'tbl': tbl,
            'page': 1
        }
        
        # Make the GET request
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return pd.DataFrame(data['data'])
            print("Data:", data['data'])
            print("Pagination Info:", data['pagination'])
        else:
            return response
            print(f"Error: {response.status_code}, {response.text}")

    def update_settings(self,param_type,data):
        # Define the API endpoint and query parameters
        url = 'http://54.166.184.183:5555/update_settings'
        params = {
            'email': self.email,
            'password': self.password,
            'param_type': param_type,
            'data': json.dumps(data)
        }
        # Make the GET request
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            return response
            print(f"Error: {response.status_code}, {response.text}")

    def create_user(self,email,password,invite_code):
        # Define the API endpoint and query parameters
        url = 'http://54.166.184.183:5555/create_user'
        params = {
            'email': email,
            'password': password,
            'invite_code': invite_code,
        }
        # Make the GET request
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            return response
            print(f"Error: {response.status_code}, {response.text}")
    def get_settings(self):
        url = 'http://54.166.184.183:5555/get_settings'
        params = {
            'email': self.email,
            'password': self.password
        }
        # Make the GET request
        response = requests.get(url, params=params)
        
        
        data=response.json()
        
        account_settings = data.get('account_settings',[{}])[0]
        
        user_settings = data.get('user_settings',[{}])[0]
        
        account_settings['POLICIES']=json.loads(account_settings.get('POLICIES'))
        account_settings['USERS']=json.loads(account_settings.get('USERS'))
        
        if 'SECRETS' in list(account_settings.keys()):
            account_settings['SECRETS']=json.loads(account_settings.get('SECRETS'))
            
        self.settings={'user_settings':user_settings,'account_settings':account_settings}
        return {'user_settings':user_settings,'account_settings':account_settings}




class New:
    def __init__(self,email,password,invite_code):
        # Define the API endpoint and query parameters
        url = 'http://54.166.184.183:5555/create_user'
        params = {
            'email': email,
            'password': password,
            'invite_code': invite_code,
        }
        self.email=email
        self.password = password
        # Make the GET request
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print("New user added to account")
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def client(self):
        return Connect(self.email, self.password)

