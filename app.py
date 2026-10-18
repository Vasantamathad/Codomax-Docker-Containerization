from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>My Docker Web Application</title><style>
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;color:#182230;background:linear-gradient(135deg,#eef5ff,#f7fbff);min-height:100vh;display:grid;place-items:center;padding:24px}main{width:min(720px,100%);background:#fff;padding:40px;border-radius:20px;box-shadow:0 16px 45px #14325e1f}.badge{display:inline-block;padding:7px 12px;border-radius:99px;background:#e3f7ec;color:#17663a;font-size:13px;font-weight:bold}h1{margin:18px 0 12px;font-size:clamp(30px,5vw,44px)}p{color:#536273;line-height:1.7}.panel{margin-top:24px;padding:18px;background:#f3f7fc;border-radius:12px}a{color:#145dcc}footer{margin-top:25px;font-size:13px;color:#728095}
</style></head><body><main><span class="badge">● Docker container is running</span><h1>Hello from my Docker web application!</h1><p>This is your own web application running inside a Docker container. You built the image from a Dockerfile and published the app on port 8000.</p><div class="panel"><strong>Try these endpoints</strong><p><a href="/health">/health</a> — check application status</p><p><a href="/info">/info</a> — view application information</p></div><footer>Built for Docker learning practice.</footer></main></body></html>"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b'{"status":"ok"}'
            content_type = "application/json; charset=utf-8"
        elif self.path == "/info":
            body = b'{"application":"My Docker Web Application","port":8000}'
            content_type = "application/json; charset=utf-8"
        else:
            body = PAGE.encode("utf-8")
            content_type = "text/html; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print("%s - %s" % (self.address_string(), format_string % args), flush=True)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), MyHandler)
    print("Web application running on port 8000", flush=True)
    server.serve_forever()
