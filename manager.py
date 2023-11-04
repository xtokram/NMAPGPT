
import subprocess, openai
from config import OPENAPI_KEY, INIT_SYSTEM_MESSAGE
class Manager:
    
    def check_nmap(self):
        try:
            subprocess.check_output(["nmap", "--version"], stderr=subprocess.STDOUT)
            return True
        except subprocess.CalledProcessError:
            return False

    def check_api_key(self, api_key):
        if api_key == None:
            return False
        else:
            return True

    def open_nmap_file(self, file):
        try:
            with open(file) as f:
                return f.read()    
        except Exception as error:
            return str(error)
        
    def nmap_analysis(self, nmap_text):

        messages_user = [INIT_SYSTEM_MESSAGE]
        messages_user.append({"role": "user", "content": nmap_text})
        openai.api_key = OPENAPI_KEY

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_user
        )

        print(response['choices'][0]['message']['content'])

        
    def run_standard_nmap(self, url):
        print(f"Starting scan on target {url}")
        cmd = ["nmap", "-sS", "-sC", "-T4", url]
        nmap_scan = subprocess.run(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.nmap_analysis(nmap_text=nmap_scan.stdout)

    def run_nmap(self, cmd, url):
        print(f"Starting scan on target {url}")
        nmap_scan = subprocess.run(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.nmap_analysis(nmap_text=nmap_scan.stdout)





    