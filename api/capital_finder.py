from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url = parse.urlsplit(path)
    query_list = parse.parse_qsl(url.query)
    dic = dict(query_list)

    if "name" in dic:
      base_url = "https://restcountries.com/v3.1/name/"
      requested = requests.get(base_url + dic["name"])
      data = requested.json()

      country_name = str(data[0]["name"]["common"])
      capital_name = str(data[0]["capital"][0])
      message = f"The capital of {country_name} is {capital_name}."

    else: 
      message = "Please enter a valid country name"


    self.send_response(200)
    self.send_header('Content-type','text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return


