company = {
    "HR": {
        "John Doe": {"role": "HR Manager"},
        "Jane Smith": {"role": "Recruiter"}
    },
    "IT": {
        "Alice Johnson": {"role": "Software Developer"},
        "Bob Brown": {"role": "Data analytic"}
    },
    "Finance": {
        "Michael Green": {"role": "Financial Analyst"},
        "Sara White": {"role": "Accountant"}
    },
    "Sales": {
        "Tom Blue": {"role": "Sales Manager"},
        "Emma Black": {"role": "Sales Associate"}
    }
}

def display_company_structure():
    for department, employees in company.items():
        print(f"Department: {department}")
        for name, details in employees.items():
            print(f"  Employee Name: {name}, Role: {details['role']}")
        print()

# an example usage of displaying the company strcuture
display_company_structure()
