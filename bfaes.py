import argparse
import pyAesCrypt
from colorama import init, Fore, Style

init() # Initialization module 'colorama'

parser = argparse.ArgumentParser(description="Aes encrypt & decrypt")

parser.add_argument("-p", help="Path to file")
parser.add_argument("-o", help="Path to out file")
parser.add_argument("-a", help="Action: 'e' (encrypt) or 'd' (decrypt)")
parser.add_argument("-pfile", help="File with passwords for bruteforce")
parser.add_argument("-passwd", help="set password for file")
parser.add_argument("-bs", default=64 * 1024, help="Buffer size. Default: 64 * 1024")

args = parser.parse_args()


"""For example:

ENCRYPT: bfaes.py -p C:/Users/user/Desktop/test.txt -o C:/Users/user/Desktop/testout.txt -passwd testpasswordforfile -a e
DECRYPT: bfaes.py -p C:/Users/user/Desktop/test.txt.aes -o C:/Users/user/Desktop/aestestout.txt -pfile C:/Users/user/Desktop/brutefile.txt -a d

"""


def action(*args):
	values = {
		"action": args[0].a,
		"path": args[0].p,
		"out": args[0].o,
		"passwd": args[0].passwd,
		"bs": args[0].bs,
		"dbfile": args[0].pfile 
	}

	if values["action"].lower() == "d" or "decrypt":
		if values["dbfile"] is None:
			pass
		else:
			with open(values["dbfile"], "r") as file:
				for password in file.read().split():
					try:
						if values['path'].endswith(".aes"):
							values['path'] = values['path']
						else:
							values["path"] = f"{values['path']}.aes"
							
						pyAesCrypt.decryptFile(values["path"], values["out"], password, values["bs"])
						print(f"{Fore.GREEN}\n[*] PASSWORD: {password}\n")
					except ValueError:
						print(f"{Fore.RED}[*] NOT CORRECT PASSWORD: {password}")
	if values["action"].lower() == "e" or "encrypt":
		if values["passwd"] is None:
			pass
		else:
			if values["out"].endswith(".aes"):
				values["out"] = values["out"]
			else:
				values["out"] = f"{values['out']}.aes"

			pyAesCrypt.encryptFile(values["path"], values["out"], values["passwd"], values["bs"])


action(args)