# Bruteforce AES

### Install ✔
git clone https://github.com/Fsoky/bfaes.git \
pip install -r requirements.txt

### Arguments ⚙
|Parameters|Value|
|----------|-----|
|-p|Path to file|
|-o|Path to out file|
|-passwd|Set password for file|
|-bs|Buffer size, default: 64 * 1024|
|-pl|File with passwords for bruteforce|
|-a|Action: 'd' (decrypt) or 'e' (encrypt)|

### Examples 👀
Encrypt file:

    bfaes.py -p target.txt -o outfile.aes -passwd 12345 -a e

Decrypt file:

    bfaes.py -p target.aes -o outdecryptedfile.txt -pl passwords.txt -a d
