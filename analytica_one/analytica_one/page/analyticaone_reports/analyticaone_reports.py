# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time

METABASE_SITE_URL = "http://localhost:3000"
METABASE_SECRET_KEY = "7e23d26c780e29df3d291d2b0ab52a6df7c31cd5250fff5312205d90feadb864"

payload = {
  "resource": {"dashboard": 2},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 60) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode('utf8') + '#bordered=true&titled=false'

print(iframeUrl)