from flask import Flask, render_template, request
import subprocess
import socket
import os

app = Flask(__name__)

@app.context_processor
def inject_global_vars():
    return dict(request=request)

@app.route("/")
@app.route("/gazeinsight")
def gazeinsight():
    # Live browser-based eye tracking demo with MediaPipe
    return render_template("gazeinsight.html", title="GazeInsight Live Demo")

def find_available_port(start_port=5000, max_port=5010):
    """Find an available port starting from start_port"""
    for port in range(start_port, max_port + 1):
        try:
            # Try to create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            
            # If port is not in use (connection refused means port is available)
            if result != 0:
                return port
        except:
            continue
    return None

if __name__ == "__main__":
    # Try to find an available port
    port = find_available_port(5001, 5010)
    
    if port:
        print(f"🚀 Starting Flask app on port {port}")
        print(f"📱 Open your browser and go to: http://localhost:{port}")
        app.run(debug=True, port=port)
    else:
        print("❌ No available ports found. Trying default port...")
        try:
            app.run(debug=True, port=5000)
        except OSError as e:
            print(f"❌ Error: {e}")
            print("\n💡 Try these solutions:")
            print("1. Close other applications using port 5000")
            print("2. Run in Command Prompt as Administrator:")
            print("   netstat -ano | findstr :5000")
            print("   taskkill /PID <PID> /F")
            print("3. Restart your computer")