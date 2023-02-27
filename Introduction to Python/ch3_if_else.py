# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program takes hourly_pay_rate and hours_worked and displays regular_pay, overtime_pay and total_pay.
# Get hourly_pay_rate
# Get hours_worked
# Calculate OVERTIME_FACTOR as 1.5
# Calculate BASE_HOURS constant
# Calculate regular_pay. If hours_worked <= 40, use hours_worked. If over 40, use BASE_HOURS.
# Calculate overtime_pay. If hours_worked is <= 40 then no OT pay. If over 40 then hours_worked - 40 * hourly_pay_rate * OVERTIME_FACTOR
# Calculate total_pay
# Display regular pay
# Display overtime_pay
# Display total_pay

def main():
    # Get hourly_pay_rate
    hourly_pay_rate = float(input('Enter the hourly pay rate '))
    # Get hours_worked
    hours_worked = float(input('Enter the hours worked last week '))
    # Calculate OVERTIME_FACTOR as 1.5
    OVERTIME_FACTOR = 1.5
    # Calculate BASE_HOURS constant
    BASE_HOURS = 40
    # Calculate regular_pay. If hours_worked <= 40, use hours_worked. If over 40, use 40.
    if hours_worked <= BASE_HOURS:
        regular_pay = hourly_pay_rate * hours_worked
    else:
        regular_pay = hourly_pay_rate * BASE_HOURS
    # Calculate overtime_pay. If hours_worked is <= 40 then overtime is 0. If over 40 then hours_worked - 40 * hourly_pay_rate * OVERTIME_FACTOR
    if hours_worked <= BASE_HOURS:
        overtime_pay = 0
    else:
        overtime_pay = (hours_worked - BASE_HOURS) * hourly_pay_rate * OVERTIME_FACTOR
    # Calculate total_pay
    total_pay = overtime_pay + regular_pay
    # Display regular pay
    print(f"Regular pay: ${regular_pay:,.2f}")
    # Display overtime_pay
    print(f"Overtime pay: ${overtime_pay:,.2f}")
    # Display total_pay
    print(f"Total pay: ${total_pay:,.2f}")

main()
