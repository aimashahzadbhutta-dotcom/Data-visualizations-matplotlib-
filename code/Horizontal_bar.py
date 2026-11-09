import csv
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("ggplot")

with open("drugs_dataset.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    country_counter = Counter()
    
    for row in csv_reader:
        country_counter.update(row["exportedtocountries"].split(';'))

country_name = []
drugs_imported = []

for data in country_counter.most_common(15):
    country_name.append(data[0])
    drugs_imported.append(data[1])

country_name.reverse()
drugs_imported.reverse()

plt.barh(country_name, drugs_imported)

plt.xlabel('Number of exported drugs')
#plt.ylabel('Countries')
plt.title('Record of drugs exported to different countries')

plt.tight_layout()
plt.savefig("Record of drugs exported to different countries.png")
plt.show()