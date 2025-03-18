principal = 1000  
annual_rate = 0.07  

years = [10, 20, 30]

for number_of_years in years:
    amount_on_deposit = principal * (1 + annual_rate) ** number_of_years

    print(f"{number_of_years} years, the investment will be: ${amount_on_deposit:.2f}")
