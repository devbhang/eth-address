import json
import time

from eth_account import Account
from eth_account.hdaccount import generate_mnemonic


def generate():
    Account.enable_unaudited_hdwallet_features()

    counter = 0
    iterator = 0
    mnemonic = generate_mnemonic(num_words=24, lang="english")
    print("MNEMONIC -->", mnemonic)

    data = {
        "mnemonic": mnemonic,
        "accounts": [],
    }

    while(counter < max):
        acct = Account.from_mnemonic(mnemonic, account_path=f"m/44'/60'/0'/0/{iterator}")
        print("PUBLIC & PRIVATE KEY -->", acct.address, acct.key.hex())

        if (acct.address.startswith(prefix) and acct.address.endswith(suffix)):
            print("FOUND IT! -->", acct.address)

            data["accounts"].append({
                "private_key": acct.key.hex(),
                "public_key": acct.address,
            })

            counter += 1

        iterator += 1
    
    with open(r'address-data/' + "address_" + str(time.time()) + '.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))

    print("SAVED!")


if __name__ == '__main__':

    prefix = "0x62"
    suffix = ""
    max = 1

    try:
        generate()
    except Exception as e:
        print(e)
