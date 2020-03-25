import pandas as pd

results = pd.DataFrame([])

for chunk in iter(pd.read_csv("gnaf_feb_2020_address_view.csv", chunksize = 1000)):
    results = results.append(chunk[chunk.AddressText.str.contains(pat = 'CAPITAL HILL')])
    if results.shape[0] > 0:
        break    # break here
    
print(results.iloc[0])
