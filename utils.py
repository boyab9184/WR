

def sorted_desc_by_transaction(df, number):
    '''Takes data frame sorting desc by transctions limited to NUMBER (second argument)'''
    df_sorted_by_transactions = df.sort_values(by=['Transactions'], ascending=False)
    return df_sorted_by_transactions.head(number)
