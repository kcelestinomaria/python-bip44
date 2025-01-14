from typing import Tuple

from bip32 import HARDENED_INDEX

__all__ = ("COIN_PATHS",)


def coin_path_by_index(index: int = 0) -> Tuple[int, int]:
    # Full list is at https://github.com/satoshilabs/slips/blob/master/slip-0044.md#registered-coin-types
    return (44 + HARDENED_INDEX, index + HARDENED_INDEX)


COIN_PATHS = {
    "BTC": coin_path_by_index(),
    "TESTNET": coin_path_by_index(1),
    "LTC": coin_path_by_index(2),
    "DOGE": coin_path_by_index(3),
    "ETH": coin_path_by_index(60),
    "ETC": coin_path_by_index(61),
    "ALGO": coin_path_by_index(283), 
    # ALGO is no. 283, all Algorand ASAs are also retrievable through the same index as ALGO, though we'll have to directly query from user which ASA Token they want
    "ASA": coin_path_by_index(283)
}
