import pandas as pd

df = pd.read_csv("drugs_dataset.csv")
print(df["activity"].tolist())



data = pd.read_csv("drugs_dataset.csv")

bins = [1,2,3,4,5,6,7,8,9,10]



with open("drugs_dataset.csv","r") as f:
    csv_reader = csv.DictReader(f)

    country_counter = Counter()

    for row in csv_reader:
        country_counter.update(row["exportedtocountries"].split(';'))

    country = []
    bins = []

    for info in country_counter.most_common(15):
        country.append(info[0])
        bins.append(info[1])



sort_bin = pd.Series(bin)
sort_bin.sort_values()
bins = sort_bin.reverse()