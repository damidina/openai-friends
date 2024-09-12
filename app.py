import json
import subprocess
import os
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs

API_KEY = "vin-replace-this-with-key"

def call_openai_api(prompt):
    start_time = time.time()
    data = json.dumps({
        "model": "o1-preview",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })

    curl_command = [
        'curl', 'https://api.openai.com/v1/chat/completions',
        '-H', f'Authorization: Bearer {API_KEY}',
        '-H', 'Content-Type: application/json',
        '-d', data
    ]

    result = subprocess.run(curl_command, capture_output=True, text=True)
    end_time = time.time()
    response_time = end_time - start_time
    return result.stdout, response_time

class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        prompt = params.get('prompt', [''])[0]

        response, response_time = call_openai_api(prompt)
        parsed_response = json.loads(response)
        parsed_response['response_time'] = f"{response_time:.2f} seconds"

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(parsed_response).encode())

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

def run_server(port=8900):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
