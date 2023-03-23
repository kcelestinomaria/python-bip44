from algosdk import account, mnemonic, encoding
from coincurve import PrivateKey
from bip44 import Wallet

# generate an account
private_key, address = account.generate_account()
print("Private key:", private_key)
print("Address:", address)
print(f"mnemonic: {mnemonic.from_private_key(private_key)}")

private_keyMnem = mnemonic.from_private_key(private_key)

# check if the address is valid
if encoding.is_valid_address(address):
    print("The address is valid!")
else:
    print("The address is invalid.")

# Create bip44 standard wallet from Algorand Account Mnemonic
w = Wallet(private_keyMnem)

# derive the newly created master key account details
master_private_key, master_address = w.derive_account("ALGO", account=0) # account index is 0

master_private_key = PrivateKey(master_private_key)

#check 1
#master_private_key.master_address.format() == master_address
# should output Boolean=True




