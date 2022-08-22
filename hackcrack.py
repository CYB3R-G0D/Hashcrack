import argparse,hashlib

if __name__ == '__main__':
    #Initialize the parser
    parser = argparse.ArgumentParser(
        description="Decrypt and crack your md5, sha1, sha224, sha256, sha384 and sha512 hashes with is script"
    )

    # Add the parameters
    # metavar with empty strings is used for the cleaner look in arguments help (aligned formats)
    parser.add_argument('--hash', help="Add your hash", required=True)
    parser.add_argument('--wordlist', '-w', help='Word list textfile', required=False, default="100K.txt")
    parser.add_argument('--salt', '-s', help='Add salt', required=False, default="")

    # Parse the arguments
    args = parser.parse_args()
    #do something here
    def print_banner():
        print("""
     _               _                         _
    | |__   __ _ ___| |__   ___ _ __ __ _  ___| | __
    | '_ \ / _` / __| '_ \ / __| '__/ _` |/ __| |/ /
    | | | | (_| \__ | | | | (__| | | (_| | (__|   <
    |_| |_|\__,_|___|_| |_|\___|_|  \__,_|\___|_|\_\\

    https://github.com/CYB3R-G0D/hashcrack
    by CYB3R G0D

    Available hashing algorithms: 
    md5 sha1 sha224 sha256 sha384 sha512
        """)
        print('\n\n\n')

    def not_found():
        print("[-] Sorry, couldn't crack the hash. Try different wordlist")

    hash = str(args.hash)
    salt = str(args.salt)
    wordlist = str(args.wordlist)
    

    try:
        print_banner()

        with open(wordlist,'r',encoding ='iso-8859-1') as file:
            lines = file.read().splitlines()
            cracked_str = 0
            print("[*] Cracking the hash")
            for line in lines:
                salted = str(line+salt)
                if str(hashlib.md5(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : "+line +"\n[+] Algorithm : md5")
                    cracked_str = line
                    break
                elif str(hashlib.sha1(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : " +line +"\n[+] Algorithm : sha1")
                    cracked_str = line
                    break
                elif str(hashlib.sha224(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : " +line +"\n[+] Algorithm : sha224")
                    cracked_str = line
                    break
                elif str(hashlib.sha256(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : " +line +"\n[+] Algorithm : sha256")
                    cracked_str = line
                    break
                elif str(hashlib.sha384(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : " +line +"\n[+] Algorithm : sha384")
                    cracked_str = line
                    break
                elif str(hashlib.sha512(salted.encode('utf-8')).hexdigest()) == hash:
                    print("[+] Cracked : " +line +"\n[+] Algorithm : sha512")
                    cracked_str = line
                    break
            if cracked_str == 0:
                not_found()
            file.close()

    except FileNotFoundError:
        print(f"[-] {wordlist} doesn't exist !")