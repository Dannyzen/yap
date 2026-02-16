import os
import sys
import subprocess
import time
import webbrowser
from yap.config import Config
from .daemon import ensure_daemon_running

def main():
    """
    Launch the Yap Web Client.
    
    1. Ensures the server daemon is running.
    2. Opens the WebUI HTML file in the default browser.
    """
    print("🌐 Launching Yap Web Client...")
    
    # Load config to get host/port
    config = Config()
    host = config.get("server.host", "0.0.0.0")
    port = config.get("server.port", 9090)
    
    # 1. Start Server if needed
    if not ensure_daemon_running(host, port):
        print("❌ Failed to start server daemon.")
        sys.exit(1)
        
    # 2. Open Browser
    # Locate the index.html file relative to the project root or package
    # We moved it to examples/web-client/index.html
    
    # Try creating absolute path assuming we are running from project root
    project_root = os.getcwd()
    web_client_path = os.path.join(project_root, "examples", "web-client", "index.html")
    
    if not os.path.exists(web_client_path):
        # Fallback: maybe we are installed as a package?
        # In a real package install, we might need to ship this file as package_data
        # For now, let's assume dev environment
        print(f"⚠️  Could not find Web Client at: {web_client_path}")
        print("   Please ensure you are running from the project root.")
        return

    print(f"📂 Opening: {web_client_path}")
    webbrowser.open(f"file://{web_client_path}")
    print("✅ Browser opened. Use the web interface to record.")

if __name__ == "__main__":
    main()
