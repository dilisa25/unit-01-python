survey_name = input("Enter survey name: ")
num_responses = int(input("Enter number of responses: "))

total_rating = 0
new_customers = 0

for x in range(num_responses):
    customer_type = int(input("Is it a returning or new customer?: "))
    rating = int(input("What is the rating?(1-5): "))
    if total_rating > 1 or total_rating < 5:
        print("Invaild")
    if customer_type == "new":
        new_customers +=1
    else:
        new_customers +=0