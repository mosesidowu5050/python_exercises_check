principal = 1000  
annual_rate = 0.07  



for number_of_years in range(1, 31):
    amount_on_deposit = principal * (1 + annual_rate) ** number_of_years

    print(f"End of year {number_of_years}, the investment will be: ${amount_on_deposit:.2f}")
