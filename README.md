# **G**enerate **E**ntropy **S**eed **B**ased on **R**andom **E**nvironmental **V**ariables

This project allows you to generate your own **BIP39 seed** of 256 bit length, by inputting any number(From 0-9) and using random variance by environmental factors(On Raspberry pi) to generate the rest of the numbers. So that you don't have to trust any organisation to track the random seed you used to generate your mnemonic.

This is a python script that accepts as a parameter a string of decimals created with your own entropy and also by environmental factors and generates a bip39 mnemonic seed. This seed is then used to generate the private key, public key and address of the crypto wallet on both the BTC and ETH blockchain.


## Usage example:
Download the project as a zip, open a terminal in the directory and type:

```
python3 main.py
```

then follow the script instructions.

## Warnings
This project is meant to use in sync with a hardware crypto wallet to generate a totally random seed based on random variables with no possible interferences from potentail hackers! If you are not using it together with a hardware crypto wallet, you are exposing yourself to the same risks and it can become compromisable!!

## Don't trust, verify!
In order to avoid that you have to review the bip39 words list, it is in a separate file and you can just delete that one and download it again from https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt and save it as `english.txt`


## Disclaimer:
Use this project at your own risk. 

I DON'T have any responsability of how you will use it and eventual money loss.

Don't use this project to generate your actual wallet if you don't know what you are doing!!
