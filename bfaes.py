import argparse
import pyAesCrypt

import rich

parser = argparse.ArgumentParser(description="Aes encrypt/decrypt")
parser.add_argument("-f", "--file", help="Path to file")
parser.add_argument("-o", "--output", help="Path to out file")
parser.add_argument("-a", "--action", help="Action:\n\te - encrypt\n\td - decrypt")
parser.add_argument("-pl", "--passwords-list", help="File with passwords for bruteforce")
parser.add_argument("-passwd", "--password", help="Set password for file")
parser.add_argument("-bs", "--buffer-size", default=64 * 1024, help="Buffer size. Default: 64 * 1024 (65536)")

args = parser.parse_args()

try:
	if args.action.lower() == "d":
		with open(args.passwords_list, "r") as file:
			passwords = file.read().split()
			attempt = 0

			for password in passwords:
				try:
					if not args.file.endswith(".aes"):
						args.file = f"{args.file}.aes"

					pyAesCrypt.decryptFile(args.file, args.output, password, args.buffer_size)
					rich.print(f"Password found: [green]{password}[/green]")

					break
				except ValueError:
					continue
	if args.action.lower() == "e":
		if not args.output.endswith(".aes"):
			args.output = f"{args.output}.aes"

		pyAesCrypt.encryptFile(args.file, args.output, args.password, args.buffer_size)
except AttributeError:
	banner = """Examples:
	[red]Encrypt[/red]
	bfaes.py -f [yellow]target.txt[/yellow] -a [purple]e[/purple] -passwd [green]12345[/green] -o [yellow]outfile.aes[/yellow]

	[red]Decrypt[/red]
	bfaes.py -f [yellow]target.aes[/yellow] -a [purple]d[/purple] -pl [green]passwords.txt[/green] -o [yellow]outfile.txt[/yellow]
	"""
	rich.print(banner)