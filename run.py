import platform
import os
from server import app

def run_server():
    host = '0.0.0.0'
    port = int(os.getenv('PORT', 8000))
    
    # Check the operating system
    if platform.system() == 'Windows':
        # Use Waitress on Windows
        from waitress import serve
        print(f"Starting Waitress server on {host}:{port}")
        serve(app, host=host, port=port)
    else:
        # Use Gunicorn on Unix-like systems (Linux, macOS)
        import subprocess
        print(f"Starting Gunicorn server on {host}:{port}")
        subprocess.run([
            'gunicorn',
            '--bind', f'{host}:{port}',
            'server:app'
        ])

if __name__ == "__main__":
    run_server() 