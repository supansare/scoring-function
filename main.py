import os
from ibm_watson_machine_learning import APIClient

def main(params):
  WML_CREDENTIALS = {
                   "url": "https://cpd-dswxgov50.wxgov50ocp-7eabc591f572c353722ab5ea37d3b2f1-0000.us-south.containers.appdomain.cloud",
                   "username": os.environ['username'],
                   "password" : os.environ['password'],
                   "instance_id": "wml_local",
                   "version" : "5.0"
                  }
  space_id="d4ebd858-f9aa-439a-ac56-c9cd01f6269f"
  deployment_id="eed0266c-9539-4073-8970-ed419d028cb2"
  
  wml_client = APIClient(WML_CREDENTIALS)
  wml_client.set.default_space(space_id)
  name = params.get("name", "world")
  greeting = "Hello " + name + "!"
  print("hello")

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": os.environ['username'],
  }
