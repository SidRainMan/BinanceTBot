from datetime import datetime, timedelta

# Input date in the format "DDMMYYYY"
input_date = input("Enter the date (DDMMYYYY): ")
date = datetime.strptime(input_date, '%d%m%Y')

for i in range(10):
    past_date = date - timedelta(weeks=i+1)
    print(past_date.strftime("%d%m%Y"))
