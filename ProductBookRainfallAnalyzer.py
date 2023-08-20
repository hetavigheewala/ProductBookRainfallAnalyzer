


#Task 1

# Ask the user for the number of products to purchase
num_products = int(input("Enter the number of products to purchase (between 1 and 100): "))

# Validate the input using a loop to ensure it's between 1 and 100
while num_products < 1 or num_products > 100:
    print("Invalid input. Please enter a number between 1 and 100.")
    num_products = int(input("Enter the number of products to purchase (between 1 and 100): "))

total_cost = 0  # Initialize the total cost variable

# Loop through each product to ask for cost and calculate total cost
for _ in range(num_products):
    cost = float(input("Enter the cost for product {}: ".format(_ + 1)))
    total_cost += cost

average_cost = total_cost / num_products  # Calculate the average cost

# Display the total cost and average cost
print("Total cost for all products: {:.2f}".format(total_cost))
print("Average cost per product: {:.2f}".format(average_cost))

#----------------------------------------------------------#
#Task 2

# Define the function funBook with a parameter for the number of books
def funBook(num_books):
    total_pages = 0  # Initialize the total pages variable

    # Loop through each book to ask for the number of pages
    for _ in range(num_books):
        pages = int(input("Enter the number of pages for book {}: ".format(_ + 1)))
        total_pages += pages

    average_pages = total_pages / num_books  # Calculate the average number of pages
    return average_pages

# Call the funBook function for 5 books and display the result
average_pages_5_books = funBook(5)
print("Average number of pages for 5 books: {:.2f}".format(average_pages_5_books))

#----------------------------------------------------------#
#Task 3
# Ask the user for the number of days
num_days = int(input("Enter the number of days (between 1 and 10): "))

# Validate the input using a loop to ensure it's between 1 and 10
while num_days < 1 or num_days > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    num_days = int(input("Enter the number of days (between 1 and 10): "))

rainfall_greater_than_2 = 0  # Initialize the counter for days with rainfall greater than 2 inches

# Loop through each day to ask for the rainfall and count days with greater than 2 inches
for _ in range(num_days):
    rainfall = float(input("Enter the rainfall in inches for day {}: ".format(_ + 1)))
    if rainfall > 2:
        rainfall_greater_than_2 += 1

# Display the number of days with rainfall greater than 2 inches
print("Number of days with rainfall greater than 2 inches: {}".format(rainfall_greater_than_2))


