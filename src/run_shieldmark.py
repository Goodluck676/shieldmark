#we call process transaction and generate transcations
from validate_amount import process_transaction
from generate_transactions import generate_transactions

#generate transactions is called first so that we can get the actual and fraudulent transactions
transactions = generate_transactions()



#build the user front interface report that the small business owner sees
print("====================================")
print("   SHIELDMARK TRANSACTION REPORT")
print("====================================")

#call all transactions in generate_transaction
for transaction in transactions:
    #tranfer all those transcations to process_transaction
    result = process_transaction(transaction)

    
    #display all employee transaction record to the owner of the business
    print("Employee: " + result["staff_name"] ) 
    print("Discrepancy: $" + str(result["discrepancy"]))
    print("Status: " + result["status"]) 
    print("ID: " + result["staff_id"])
    print("----------------------------------------------------")