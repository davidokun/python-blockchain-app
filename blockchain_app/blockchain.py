"""
Blockchain service
"""
BLOCK_CHAIN = [[]]


def add_value(new_value):
    """
    Add new value to the blockchain list
    :param new_value: the new value
    """
    BLOCK_CHAIN.append([BLOCK_CHAIN[-1], new_value])
    print(BLOCK_CHAIN)


add_value(5.3)
