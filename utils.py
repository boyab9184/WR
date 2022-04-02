

def sorted_desc_by_transaction(df, limit):
    '''Takes data frame sorting desc by transctions limited to NUMBER (second argument)'''
    sorted_by_transactions = df.sort_values(by=['Transactions'], ascending=False)
    return sorted_by_transactions.head(limit)
