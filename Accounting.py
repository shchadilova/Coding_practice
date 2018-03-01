import numpy as np

# How many years will the mortgage loan last?
mortgage_length = 30

# How many mortgage payment periods are there in a year?
annual_payment_periods = 12

# What is the annual mortgage interest rate?
mortgage_rate = 0.0375

# Derive the equivalent monthly mortgage rate from the annual rate
mortgage_rate_periodic = (1+mortgage_rate)**(1/annual_payment_periods)-1

# How many payment periods will there be in total?
mortgage_payment_periods = mortgage_length*annual_payment_periods

# Calculate the monthly mortgage payment (multiply by -1 to keep it positive)
periodic_mortgage_payment = -1*np.pmt(rate=mortgage_rate_periodic, nper=mortgage_payment_periods, pv=mortgage_loan)
print("Monthly Mortgage Payment: " + str(round(periodic_mortgage_payment, 2)))

# Calculate the amount of the first loan payment that will go towards interest
initial_interest_payment = mortgage_rate_periodic*mortgage_loan
print("Initial Interest Payment: " + str(round(initial_interest_payment, 2)))

# Calculate the amount of the first loan payment that will go towards principal
initial_principal_payment = periodic_mortgage_payment-initial_interest_payment
print("Initial Principal Payment: " + str(round(initial_principal_payment, 2)))

import numpy as np

# Initialize the principal remaining array with length equal to the number of payment periods
principal_remaining = np.repeat(0.0, mortgage_payment_periods)

# Loop through each mortgage payment period
for i in range(0, mortgage_payment_periods):
    
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = mortgage_loan
    else:
        previous_principal_remaining = principal_remaining[i-1]
        
    # Calculate the interest and principal payments
    interest_payment = round(previous_principal_remaining*mortgage_rate_periodic, 2)
    principal_payment = round(periodic_mortgage_payment-interest_payment, 2)
    
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
        
    # Collect the principal remaining values in an array
    principal_remaining[i] = previous_principal_remaining - principal_payment
    
    # Output the results
    print("Period " + str(i) + ": " + \
    "Interest Paid: " + str(interest_payment) + \
    " | Principal Paid: " + str(principal_payment) + \
    " | Remaining Balance: " + str(principal_remaining[i])) 

import numpy as np

# Calculate the cumulative home equity (principal) over time
cumulative_home_equity = np.cumsum(principal_paid)

# Calculate the cumulative interest paid over time
cumulative_interest_paid = np.cumsum(interest_paid)

# Calculate your percentage home equity over time
cumulative_percent_owned = down_payment_percent + (cumulative_home_equity/home_value)
print(cumulative_percent_owned)

# Plot the cumulative interest paid vs equity accumulated
plt.plot(cumulative_interest_paid, color='red')
plt.plot(cumulative_home_equity, color='blue')
plt.legend(handles=[interest_plot, principal_plot], loc=2)
plt.show()