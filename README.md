# bfaes
Bruteforce AES

|Parameters|Value|
|----------|-----|
|-p|Path to file|
|-o|Path to out file|
|-passwd|Set password for file|
|-bs|Buffer size, default: 64 * 1024|
|-pfile|File with passwords for bruteforce|
|-a|Action: 'd' (decrypt) or 'e' (encrypt)|

## Encrypt file:

`bfaes.py -p C:/Users/user/Desktop/test.txt -o C:/Users/user/Desktop/testout.txt -passwd testpasswordforfile -a e`

## Decrypt file:

`bfaes.py -p C:/Users/user/Desktop/test.txt.aes -o C:/Users/user/Desktop/aestestout.txt -pfile C:/Users/user/Desktop/brutefile.txt -a d`
