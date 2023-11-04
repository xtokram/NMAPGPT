import platform, os

OPENAPI_URL = "https://api.openai.com/v1/chat/completions"

OPENAPI_KEY = os.environ.get('OPENAPI_KEY')

OS_MACHINE = platform.system()

LANGUAGE = "portuguese"

HELP_TEXT = """
    [+] NMAPGPT - By T0kr4m [+]

    NOTE: SOME NMAP COMMANDS REQUIRES ROOT PRIVILEGES!

    IMPORTANT: SET YOUR OPENAPI KEY AS AN ENVIRONMENT VARIABLE CALLED "OPENAPI_KEY"

    USAGE: python3 nmapgpt.py [OPTIONS]

    Examples:

        Read a NMAP result text file: 
        $ python3 nmapgpt.py -r nmap.txt

        Execute Standard Nmap scan then use AI Analysis:
        $ python3 nmapgpt.py -u URL
        $ python3 nmapgpt.py -u 192.168.0.1

        Execute your favorite Nmap scan method the use AI Analysis:
        $ python3 nmapgpt.py -x NMAP_OPTIONS -u URL   
        $ python3 nmapgpt.py -x -sS -sC -u 192.168.0.1
"""

INIT_SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""
- Your name is "NMAPGPT".
- You are a helpful personal assistant for security professionals.
- You are running on {OS_MACHINE} machine.
- Please note that your answers will be displayed on the terminal.
- You will read nmap result files and sugest the best RED TEAM strategy and instructions for the security professionals to follow.
- Your instructions and strategies must be easy to understand and direct
- Write in {LANGUAGE}
""",
}

