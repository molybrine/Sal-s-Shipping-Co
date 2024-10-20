import time

#added time so its not overelming
#that name is a random name but it's a funny company name

print("Welcome to Sal's Shipping Co")

time.sleep(1)

print("We offer three different services")

time.sleep(1)

print("ground shipping")

time.sleep(1)

print("premium shipping")

time.sleep(1)

print("drone shipping")

time.sleep(1)

print("Please note that they all have different prices,")

time.sleep(1)

print("please refer to the tables bellow:")

time.sleep(1)
print("""
+----------------------------------------------------------+
|                   Ground Shipping                        |
+--------------------------+-------------------------------+
| Weight of Package        | Price per Pound | Flat Charge |
+--------------------------+-----------------+-------------+
| 2 kg or less             | £1.50           | £20.00      |
+--------------------------+-----------------+-------------+
| Over 2 kg but under 6kg  | £3.00           | £20.00      |
+--------------------------+-----------------+-------------+
| Over 6kg but under 10kg  | £4.00           | £20.00      |
+--------------------------+-----------------+-------------+
| Over 10 kg               | £4.75           | £20.00      |
+--------------------------+-----------------+-------------+

""")
time.sleep(2)
print("""
+----------------------------------------------------------+
|                   Premium Shipping                       |
+--------------------------+-------------------------------+
| Weight of Package        | Price per Pound | Flat Charge |
+--------------------------+-----------------+-------------+
| 2 kg or less             | £1.50           | £125.00     |
+--------------------------+-----------------+-------------+
| Over 2 kg but under 6kg  | £3.00           | £125.00     |
+--------------------------+-----------------+-------------+
| Over 6kg but under 10kg  | £4.00           | £125.00     |
+--------------------------+-----------------+-------------+
| Over 10 kg               | £4.75           | £125.00     |
+--------------------------+-----------------+-------------+

""")
time.sleep(2)
print("""
+----------------------------------------------------------+
|                     drone Shipping                       |
+--------------------------+-------------------------------+
| Weight of Package        | Price per Pound | Flat Charge |
+--------------------------+-----------------+-------------+
| 2 kg or less             | £4.50           | £0.00       |
+--------------------------+-----------------+-------------+
| Over 2 kg but under 6kg  | £9.00           | £0.00       |
+--------------------------+-----------------+-------------+
| Over 6kg but under 10kg  | £12.00          | £0.00       |
+--------------------------+-----------------+-------------+
| Over 10 kg               | £14.25          | £0.00       |
+--------------------------+-----------------+-------------+

""")
time.sleep(2)

print("Please note that we currently offer either premium or drone shipping,")
time.sleep(1)
print("but not both simultaneously.")

#weight in kg
weight = float(input("Please enter the weight of your package: "))

time.sleep(1)

# y or n for premium so there isnt too much code
premium = input("would you like premium shipping y or n: ")

time.sleep(1)

# y or n for drone so there isnt too much code
drone = input("would you like drone shipping y or n: ")
time.sleep(1)

#flat charge
Flat_charge = 20

#GSC (ground shipping cost)
GSC = 0

# price per pound
ppp = [1.50, 3.00, 4.00, 4.75]

# Check if both premium and drone are selected
if premium == "y" and drone == "y":
    print("You've selected both premium and drone.")
    time.sleep(1)
    print("Sadly, we don't offer premium drone shipping.")
    time.sleep(1)
    #i can already see this being tried
    
# Premium shipping
elif premium == "y":
    Flat_charge = 125

# Drone shipping
elif drone == "y":
    Flat_charge = 0
    ppp = [4.50, 9.00, 12.00, 14.25]

#ground shipping

if weight <= 2:
  #the price per kg
  GSC = Flat_charge + (weight * ppp[0])
elif weight <= 6:
  #the price per kg
  GSC = Flat_charge + (weight * ppp[1])
elif weight <= 10:
  #he price per kg
  GSC = Flat_charge + (weight * ppp[2])
else:
  #the price per kg
  GSC = Flat_charge + (weight * ppp[3])

print("That would be £",GSC)
