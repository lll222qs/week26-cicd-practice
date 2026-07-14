import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler


class HealthHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()


def start_health_server():
    server = HTTPServer(("0.0.0.0", 8000), HealthHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    print("Health server running on :8000")


if __name__ == "__main__":
    start_health_server()
    # 模拟主程序逻辑（你可以替换成你的 calculator.py）
    print("Calculator app started.")
    while True:
        time.sleep(3600)  # 永久运行
