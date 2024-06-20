"""
Wenx Structure Prompt Template:
"""

import requests
import json

wenx4_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-4.0-8k-0329"
wenx3_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-3.5-8k-0329"


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=yW94TYcnt2YcK5dT1uEs2ipv&client_secret=XLWu0n8jOsb9NIFo4GG91MIsioGVebYr&grant_type=client_credentials"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json().get("access_token"))
    return response.json().get("access_token")


def wenx_request(url, prompt):
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    dictionary = json.loads(response.text)
    return dictionary["result"]


def wenx4_request(prompt):
    url = wenx4_url + get_access_token()
    return wenx_request(url, prompt)


def wenx3_request(prompt):
    url = wenx3_url + get_access_token()
    return wenx_request(url, prompt)