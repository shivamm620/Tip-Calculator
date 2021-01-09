print('Welcome to tip calculator')
total = float(input("What is the total bill?\n$"))
percentage= float(input("What percentage would you like to gave tip?"))
person = float(input("How many people to spilt the bill ?\n"))
bill = percentage/100 *  total + total 
final_bill =float(bill / person)
next = (round(final_bill,2))
print (f"Each person have to pay ${next}")

