import pandas as pd

card = pd.read_csv('UCI_Credit_Card.csv')
card1 = pd.DataFrame(
    [
        ['LIMIT_BAL <=10000', 'A'],
        ['LIMIT_BAL <=100000 и >10000', 'B'],
        ['LIMIT_BAL <=200000 и >100000', 'C'],
        ['LIMIT_BAL <=400000 и >200000', 'D'],
        ['LIMIT_BAL <=700000 и >400000', 'E'],
        ['LIMIT_BAL >700000', 'F']
    ],
    columns=['id', 'new']
)
print(card1)
pd.merge(
    card,
    card1,
    left_on='LIMIT_BAL',
    right_on='id'
)
