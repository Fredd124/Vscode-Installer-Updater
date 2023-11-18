import requests 
import subprocess
import os

def install_deb(deb_path):
    try:
        subprocess.run(['dpkg', '-i', deb_path], check=True)
        subprocess.run(['apt-get', '-f', 'install'], check=True)
        subprocess.run(['apt-get', 'autoremove'], check=True)
        os.remove(deb_path)
    except subprocess.SubprocessError as e:
        print(f"Subprocess error occurred: {e}")
    except OSError as e:
        print(f"OS error occurred: {e}")

def main():
    url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()

        with open('vscode.deb', 'wb') as f:
            f.write(response.content)

        install_deb('vscode.deb')
    except requests.RequestException as e:
        print(f"HTTP request error: {e}")

if __name__ == "__main__":
    main()