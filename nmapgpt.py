import sys, re
from manager import Manager
from config import HELP_TEXT, OPENAPI_KEY

##By tokram

manager = Manager()

if manager.check_nmap() != True:
    print("Nmap not found! \n Aborting...")
    exit(1)

if manager.check_api_key(OPENAPI_KEY) != True:
    print("Insert your OPENAPI KEY as a Enviroment Variable!")
    exit(1)

if __name__ == '__main__':
    args = sys.argv[1:]

    if args[0] == '--help' or args[0] == '-h':
        print(HELP_TEXT)
        exit(1)

    if len(args) <= 1:
        print(HELP_TEXT, "Aborting...")
        exit(1)

    if args[0] == "-r":

        nmap_text = manager.open_nmap_file(args[1])

        manager.nmap_analysis(nmap_text)

              
    elif args[0] == "-u":
        try:
            assert len(args[1]) > 8, "Endereço inválido!"

            manager.run_standard_nmap(url=args[1])

        except AssertionError as error:
            print(str(error))
        except Exception as error:
            print(error)
    
    elif args[0] == "-x":
        cmd = ["nmap"]
        url = ""
        try:
            for x in range(1, len(args)):
                if args[x] != "-u":
                    assert args[x].startswith("-"), "Comando inválido, exemplo: -sS"
                    cmd.append(args[x])
                else:
                    url = args[x+1]
                    assert len(url) > 8, "Endereço inválido!"
                    break
            manager.run_nmap(cmd, url)
        except AssertionError as error:
            print(str(error))
        

        




        

    

