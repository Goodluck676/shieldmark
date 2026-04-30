#first ensure that we are only recieving amounts in positive numbers
def validate_amount (amount):
    #ensure that the amount is an integer or float
    if not isinstance (amount, (int, float)):
    
        #lets guard first and reject if the character is not interger/float
        return False

    #check if amount is less than or equal to zero, if so, reject too
    if amount <= 0:
        return False
    
    #but if the character is an integer or a float, accept it
    return True

#calculate the difference in the actual and the logged transaction
def calculate_discrepancy(actual, logged):

    # then I subtract the logged from the actual transaction to get my result
    result = actual - logged
    
    #then I round my result to two decimal places to mirror a real currency fomart
    result = round (result, 2)
    
    #then I return my result
    return result

#this function compiles the input and calls the guard function and the helper function to calculate
#then, this function assigns each transcation result, to show to the business owner
def process_transaction (sale):
    #check if the sale report given is in dictionary as the first guard, if not reject
    if not isinstance (sale, dict):
        return False
    

    #check if staff_id is in the sale report
    if "staff_id" not in sale:
        return False
    
    #check if staff_name is in the sale report
    if "staff_name" not in sale:
        return False
    
    #check if actual is in the sale report
    if "actual" not in sale:
        return False
    
    #check if logged is in the sale report
    if "logged" not in sale: 
        return False
    
    #lets get two variables that stores actual and logged transactions that are positive numbers
    actual = sale["actual"]
    logged = sale["logged"]
    
    #check if actual is an integer or float
    if not validate_amount(actual):
        return False
    
    #check if logged is an integer or float
    if not validate_amount(logged):
        return False

    
    #calculate the difference between actual and logged transaction
    discrepancy = calculate_discrepancy(actual, logged)

    #if the discrepancy of actual and logged after substracting logged from actual is greater than zero, 
    # status will be underreported
    if discrepancy > 0:
        status = "Underreported"
    
     #if the discrepancy of actual and logged after substracting logged from actual is less than zero, 
    # status will be overcharged
    elif discrepancy < 0:
        status = "Overcharged"
    
     #if the discrepancy of actual and logged after substracting logged from actual is same than zero, 
    # status will be accurate
    else:
        status =  "Accurate"

    
    #create a result dictionary that states the staff_id, staff_name, discrepancy, status
    result = {
         "staff_id" : sale["staff_id"],
         "staff_name" : sale["staff_name"],
         "discrepancy": discrepancy, 
         "status": status

    }

    return result

# sale1 = process_transaction({
#     "staff_id" : "Emply1",
#     "staff_name" : "Kay",
#     "actual" : 500,
#     "logged" : 300
                         

# })

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