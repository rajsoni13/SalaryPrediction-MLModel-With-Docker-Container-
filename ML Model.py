import pandas

db = pandas.read_csv("SalaryData.csv")

y = db['Salary']

x = db['YearsExperience'].values.reshape(30,1)

from sklearn.linear_model import LinearRegression

mind = LinearRegression()

mind.fit(x,y)

years=input("Enter Experience of Employee(in years): ")
print("Salary: " ,mind.predict([[float(years)]]))
