print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?$"))
tip = int(input("How much tip you would like to give?10,12 or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
#use format to print 2 decimal points 
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")