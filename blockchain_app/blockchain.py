"""
Blockchain service
"""
BLOCK_CHAIN = [[0]]


def get_last_block_chain_value():
    """
    Retrieve last value in the blockchain

    :return: last value on the blockchain list
    """
    return BLOCK_CHAIN[-1]


def add_value(transaction_amount):
    """
    Add new value to add in the blockchain list.
    New value will be a new list with size 2 composed by last_value and transaction_amount

    :param transaction_amount: amount of the transaction to be added to the blockchain
    """
    BLOCK_CHAIN.append([get_last_block_chain_value(), transaction_amount])


if __name__ == '__main__':
    NUM_OF_TX = int(input('How many transaction do you want?: '))

    for i in range(NUM_OF_TX):
        tx_number = i + 1
        tx_amount = input(f'Type the amount for transaction No {tx_number} please: ')
        add_value(float(tx_amount))

    print(BLOCK_CHAIN)
