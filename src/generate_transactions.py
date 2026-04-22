import random

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

def generate_transactions():
    fraudsters = random.sample(employees, random.randint(2,3))
    transactions = []

    for employee in employees: 
    
        actual = random.randint(10,500)

    

        if employee in fraudsters: 
             logged = random.randint(actual // 2, actual - 1)
        
        else:
            logged = actual

        transactions.append({"staff_id": employee["id"], "staff_name": employee["name"], 
                             "actual": actual, "logged":logged})
        
    return transactions


results = generate_transactions()
print(results)