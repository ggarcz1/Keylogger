from datetime import datetime

x = 5
y = 5
print(x + y)

# Define the two dates
current = datetime.today()
# install date
start = datetime(2024, 3, 1)

print((current - start).days)
# Calculate the difference between the dates
# if (current - start).days > 3:
#     return True
