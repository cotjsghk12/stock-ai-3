import http.client
import urllib.parse

url = 'https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo'
params = {
    'serviceKey': 'yGspHcbuzdbh3HayauwSlP1OuQ43VUSn3Qv5rTKkKp7nSOev1b7gdz0LF+hPGMdvuWHUa37YTAdvKtbq6JyCQQ==',
    'numOfRows': '10',
    'pageNo': '1',
    'resultType': 'json'
}

encoded_params = urllib.parse.urlencode(params)
parsed_url = urllib.parse.urlparse(url)
conn = http.client.HTTPSConnection(parsed_url.netloc)

conn.request("GET", f"{parsed_url.path}?{encoded_params}")

response = conn.getresponse()
data = response.read()
conn.close()

print(data.decode('utf-8'))

