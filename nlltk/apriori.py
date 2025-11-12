import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def market_basket(filepath, min_support=0.01, min_confidence=0.3):
    df = pd.read_csv(filepath, header=None)
    transactions = df.apply(lambda row: row.dropna().tolist(), axis=1).tolist()
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_trans = pd.DataFrame(te_ary, columns=te.columns_)
    frequent = apriori(df_trans, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent, metric="confidence", min_threshold=min_confidence)
    print(frequent.sort_values('support', ascending=False).head())
    print(rules.head())
