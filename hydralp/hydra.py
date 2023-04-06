import json
import requests

HYDRA_ADMIN_URL = "http://127.0.0.1:4445/admin"
REQUESTS_URL = HYDRA_ADMIN_URL + "/oauth2/auth/requests"

def accept_login(challenge, subject, extras):
  url = REQUESTS_URL + "/login/accept"
  resp = requests.put(
    url, 
    params={
      "login_challenge": challenge
    },
    json={
      "subject": subject, 
      "context": extras
    }
  )

  return json.loads(resp.text)

def get_consent(challenge):
  url = REQUESTS_URL + "/consent"
  resp = requests.get(
    url, 
    params={
      "consent_challenge": challenge
    }
  )

  return json.loads(resp.text)

def accept_consent(challenge, extras):
  url = REQUESTS_URL + "/consent/accept"
  resp = requests.put(
    url,
    params={
      "consent_challenge": challenge
    },
    json={
      "session": {
        "access_token": extras,
         "id_token": extras 
      }
    }
  )

  return json.loads(resp.text)
