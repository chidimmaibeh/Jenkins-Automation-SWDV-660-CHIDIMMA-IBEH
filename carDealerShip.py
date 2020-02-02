carSales = {'red': 8, 'blue': 2, 'green': 5, 'silver': 6}
for carSalesKey in carSales:
    print(carSales[carSalesKey])
    
carSales = {'red': 8, 'blue': 2, 'green': 5, 'silver': 6}
for carSalesKey in carSales:
    print(carSalesKey)
    
carSales = {'red': 8, 'blue': 2, 'green': 5, 'silver': 6}
totalSales = 0

for carSalesKey in carSales:
    totalSales = totalSales + (carSales[carSalesKey])
    print(totalSales)