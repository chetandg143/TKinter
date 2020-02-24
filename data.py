import  pandas as pd

df = pd.read_csv('/home/tibil/Downloads/Automobile_data.csv')
print(df)

print("first five records \n")
print(df.head(5))

print("last five records \n")
print(df.tail(5))
#
# df = pd.read_csv("/home/tibil/Downloads/Automobile_data.csv", na_values={
#     'price':["?","n.a"],
#     'stroke':["?","n.a"],
#     'horsepower':["?","n.a"],
#     'peak-rpm':["?","n.a"],
#     'average-mileage':["?","n.a"]})
# print (df)
#
# df.to_csv("/home/tibil/Downloads/Automobile_data.csv")

dfmax  = df[['company' ,'price']][df.price ==df['price'].max()]
print(dfmax)

dfmin  = df[['company' ,'price']][df.price ==df['price'].min()]
print(dfmin)

car = df.groupby('company')
toyo = car.get_group('toyota')
print(toyo)

print(df['company'].value_counts())

# cardf = df.groupby('company')
# price = cardf['company','price'].max()
# print(price)
#
# avgmile = cardf['company' , 'average-mileage'].mean()
# print(avgmile)
#

#
# car_Manufacturers = df.groupby('company')
# mileageDf = car_Manufacturers['company','average-mileage'].mean()
# print(mileageDf)
#



Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)