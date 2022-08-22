# Hashcrack
Decrypt and crack your md5, sha1, sha224, sha256, sha384 and sha512 hashes with wordlist


## Installation

```bash
git clone https://github.com/CYB3R-G0D/Hashcrack
cd Hashcrack
python3 hashcrack.py -hh
```

## Usage

```bash
# usage: hackcrack.py [-h] --hash HASH [--wordlist WORDLIST] [--salt SALT]

python3 hashcrack.py --hash e10adc3949ba59abbe56e057f20f883e

# with custom wordlist
python3 hashcrack.py --hash e10adc3949ba59abbe56e057f20f883e -w custom.txt

# with salt
python3 hackcrack.py --hash 60d8fd0602b2247b3c13e7481ca0b811 -s foo.com
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/CYB3R-G0D/Hashcrack/blob/main/LICENSE)
