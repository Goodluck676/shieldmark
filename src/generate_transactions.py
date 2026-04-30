import random
# imports the random tool so we can generate random numbers and pick random items

employees = [
      {"id" : "emp1", "name" : "Shade"},
      {"id":"emp2", "name" : "John"},
      {"id":"emp3", "name" : "Ada"},
      {"id":"emp4", "name" : "Gabby"},
      {"id":"emp5", "name" : "Joseph"},
      {"id":"emp6", "name" : "Kemi"},
      {"id":"emp7", "name":"Ure"},
      {"id":"emp8", "name":"Ruby"},
      {"id":"emp9", "name":"Kwame"},
      {"id":"emp10", "name": "Tammy"},
]
#all of our 10 employees

def generate_transactions():
    fraudsters = random.sample(employees, random.randint(2,3))
   # randomly selects either 2 or 3 employees from the list to be the fraudsters this run
    transactions = []
    #a list that records all transactions both underreported, overcharged and actual transactions

    for employee in employees: 
    #so this is saying for one employee in employees
    
        actual = random.randint(10,500)
        #so the actual transaction can be a number between 10 to 500

    

        if employee in fraudsters:
        #this says if the employee is a fraudster
             logged = random.randint(actual // 2, actual - 1)
             #this calculation result will determine if the employee is skimming
        
        else:
            logged = actual
            #this says employee did not skim since the logged is same as the actual transaction

        transactions.append({"staff_id": employee["id"], "staff_name": employee["name"], 
                             "actual": actual, "logged":logged})
        #this appends all transaction including the employee id and empl name
        
    return transactions
    #goes through all transactions by the 10 employees and stores it


# results = generate_transactions()
# print(results)
# #call the function and the print it