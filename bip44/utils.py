from typing import Union

from coincurve import PublicKey
from Crypto.Hash import keccak

__all__ = ("get_algo_addr", "to_checksum_addr")

# Hash Function - replace with sha256, or nacl
def keccak_256(b: bytes) -> bytes:
    h = keccak.new(data=b, digest_bits=256)
    return h.digest()

# convert algo account address to algo checksum address
# no need for this, as ALGO accounts already have checksums added
def to_checksum_addr(algo_addr: str) -> str:
    """
    Convert an ALGO account address to an ALGO checksum address.

    EIP 55: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md#implementation
    """
    address = algo_addr.lower().replace("0x", "")
    addr_hash = keccak_256(address.encode()).hex()

    res = []
    for a, h in zip(address, addr_hash):
        if int(h, 16) >= 8:
            res.append(a.upper())
        else:
            res.append(a)

    return "0x" + "".join(res)

# get an ALGO account address from a public key
# No need for this, we will just use high-level Python func from SDK)
def get_algo_addr(pk: Union[str, bytes]) -> str:
    """Get ALGO address from a public key. pk - public key, sk - secret/private key"""
    pk_bytes = bytes.fromhex(pk) if isinstance(pk, str) else pk

    if len(pk_bytes) != 64:
        pk_bytes = PublicKey(pk_bytes).format(False)[1:]

    return to_checksum_addr(f"0x{keccak_256(pk_bytes)[-20:].hex()}")
