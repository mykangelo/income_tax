


#create a function to calculate the payable income tax
def calculate_income_tax(income):
    if income <= 10000: #the tax should be remain to 0 if the income is less than or equal to 10000
        return 0
    elif income <= 20000: #the income exceeds to 10000 calculates the tax at a rate of 10%
        return (income - 10000) * 10 / 100
    else: #if the income is greater than 20000, the calculation should proceed to the addition of first 10000 at 10% and the exceeding 20000 at a rate of 20% to find the payable tax
        return (10000 * 10 / 100) + (income - 20000) * 20 / 100 


#store the total income to a variable
income = 45000
tax_payable = calculate_income_tax(income) #call the function to calculate the income tax payable
    
#display the output
print("Given income:", income)
print("Total tax to pay is", tax_payable)



