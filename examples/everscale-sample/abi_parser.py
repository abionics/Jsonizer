import os

from jsonizer import Jsonizer
from tonclient.types import AbiContract, AbiFunction, AbiEvent, AbiData, AbiParam

SAMPLE_ABI_FILENAME = 'SafeMultisigWallet.abi.json'


def abi_path(filename: str) -> str:
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, filename)


if __name__ == '__main__':
    path = abi_path(SAMPLE_ABI_FILENAME)
    parser = Jsonizer(AbiContract, AbiFunction, AbiEvent, AbiData, AbiParam, lowercase_keys=True, replace_space='_')
    abi_contract: AbiContract = parser.parse_file(path)
    print(type(abi_contract), abi_contract.dict)
    print(abi_contract.functions[0].inputs[0].name)
