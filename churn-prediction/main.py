import json
#import json, requests

def main(params):
  header = {"Content-Type": "application/json", "x":"y"} 
  scoring_url="http://169.60.148.132:9443/predictions"
  data = [['Male','No','No','No',2,'Yes','No','DSL','Yes','Yes','No','No','No','No','Month-to-month','Mailed check',53.85,3239]]
  params = {
    "input_data": [{
        "values" : data
    }]
  }
#  scoring_response = requests.post(scoring_url, json=params, headers=header, verify=False)
#   jsonify_scoring_response = scoring_response.json()

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": "hello",
  }
