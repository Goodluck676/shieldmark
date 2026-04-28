def validate_amount (amount): 
    if not isinstance (amount, (int, float)):
    
        return False

    if amount <= 0:
        return False
    
    return True

def calculate_discrepancy(actual, logged):

    # then I subtract the logged from the actual transaction to get my result
    result = actual - logged
    
    #then I round my result to two decimal places to mirror a real currency fomart
    result = round (result, 2)
    
    #then I return my result
    return result

def process_transaction (sale):
    #check if the sale report given is in dictionary
    if not isinstance (sale, dict):
        return False
    

    if "staff_id" not in sale:
        return False
    
    if "staff_name" not in sale:
        return False
    
    if "actual" not in sale:
        return False
    
    if "logged" not in sale: 
        return False
    
    actual = sale["actual"]
    logged = sale["logged"]
    
    if not validate_amount(actual):
        return False

    if not validate_amount(logged):
        return False

    
    discrepancy = calculate_discrepancy(actual, logged)

    if discrepancy > 0:
        status = "Underreported"
    elif discrepancy < 0:
        status = "Overcharged"
    else:
        status =  "Accurate"

    
    result = {
         "staff_id" : sale["staff_id"],
         "staff_name" : sale["staff_name"],
         "discrepancy": discrepancy, 
         "status": status

    }

    return result

sale1 = process_transaction({
    "staff_id" : "Emply1",
    "staff_name" : "Kay",
    "actual" : 500,
    "logged" : 300
                         

})

# print(sale1)


    
    
  
# print (calculate_discrepancy(500, 350))
# print (calculate_discrepancy(500, 700))
# print (calculate_discrepancy(200, 50))



# TEST YOUR FUNCTION
# print(validate_amount(500))      # expect True
# print(validate_amount(500.00))   # expect True
# print(validate_amount(-500))     # expect False
# print(validate_amount("500"))    # expect False
# print(validate_amount(0))        # expect False