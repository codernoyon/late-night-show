import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('iphone_price.csv')
print(data['price'])
plt.bar(data['version'], data['price'])
plt.show()