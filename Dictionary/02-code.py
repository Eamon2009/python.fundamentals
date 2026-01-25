d = {}
# For testing, you might want to change range(5) to range(2) 
for i in range(5):
    name = input("Enter the name: ")
    salary = float(input("Enter the salary: "))
    alo = float(input("Enter allowance: "))
    deduction = float(input("Enter Deduction: "))
    d[name] = [salary, alo, deduction]

while True:
    print('''
          1. Display the total salary
          2. Display the total allowance and deduction
          3. Search an employee
          4. Exit''')
    
    cho = int(input("Enter your choice: "))
    
    if cho == 1:
        print(f"{'Name':<15} {'Gross':<10} {'Net':<10}") # Added header for clarity
        for key, value in d.items():
            gross = value[0] + value[1]
            net = gross - value[2]
            print(f"{key:<15} {gross:<10} {net:<10}")

    elif cho == 2:
        total_allowance = 0
        total_deduction = 0
        for key, value in d.items():
            total_allowance += value[1]
            total_deduction += value[2]
        # Moved print statements OUTSIDE the for loop
        print(f"Total allowance of all employees: {total_allowance}")
        print(f"Total deduction of all employees: {total_deduction}")

    elif cho == 3:
        n = input("Enter employee name to be searched: ")
        # Using 'in' is more efficient than a loop for dictionaries
        if n in d:
            details = d[n]
            print(f"Name: {n} | Salary: {details[0]} | Allowance: {details[1]} | Deduction: {details[2]}")
        else:
            print("Employee not found.")

    elif cho == 4:
        print("Exiting program...")
        break
    else:
        print("INVALID CHOICE")
