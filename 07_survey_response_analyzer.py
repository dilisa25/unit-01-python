#Created input function for the survey name and number of responses 
survey_name = input("Enter survey name: ")
num_responses = int(input("Enter number of responses: "))
#Created placehoder variables for the total rating and new customers
total_rating = 0
new_customers = 0
#created a for loop so it would ask the the customer type and rating the amount of time of responses 
for x in range(num_responses):
    customer_type = input("Are they new customer?(type y/n): ")
    rating = int(input("What is the rating?(1-5): "))
    #Created this so each rating would add to the total rating 
    total_rating += rating
    #If statment so that if it was anything other than 1-5 it would be invalid 
    if total_rating < 1 and total_rating > 5:
        print("Invaild")
    #If statment so that if they type y which represent y that would add on too the number of new customers
    if customer_type == "y":
        new_customers +=1
    else:
        new_customers +=0
#Find the average by taking the total rating and divided it by number of responses and print that and amount of new customers
avg_rating =total_rating/num_responses
print(avg_rating)
print(new_customers)