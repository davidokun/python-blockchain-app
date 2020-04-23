"""
Blockchain service
"""
BLOCK_CHAIN = [[0]]


def get_last_block_chain_value():
    """
    Retrieve last value in the blockchain
    :return: last value of the blockchain list
    """
    return BLOCK_CHAIN[-1]


def add_value(transaction_amount):
    """
    Add new value to the blockchain list
    :param transaction_amount: the new value
    """
    BLOCK_CHAIN.append([get_last_block_chain_value(), transaction_amount])
    print(BLOCK_CHAIN)


add_value(5.3)
