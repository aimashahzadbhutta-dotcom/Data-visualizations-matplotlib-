import csv
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter 
plt.style.use("fivethirtyeight")

with open("drugs_dataset.csv","r") as f:
    csv_reader = csv.DictReader(f)

    country_counter = Counter()

    for row in csv_reader:
        country_counter.update(row["exportedtocountries"].split(';'))

    country = []
    bins = []

    for info in country_counter.most_common():
        country.append(info[0])
        bins.append(info[1])

bin = bins.sort()



plt.hist(country, bins=bins, color="pink", edgecolor='black')

plt.title("Drugs importing countries")
plt.ylabel("Number of Drugs")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()