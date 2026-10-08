import pandas as pd


class EmployeeAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.data = None

    # Load CSV file
    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename)
            print("Employee data loaded successfully.")

        except FileNotFoundError:
            print("Error: CSV file not found.")

    # Display employee data
    def display_data(self):
        if self.data is not None:
            print("\nEmployee Data:")
            print(self.data)

    # Calculate average salary
    def average_salary(self):
        if self.data is not None:
            average = self.data["Salary"].mean()
            print(f"\nAverage Salary: ₹{average:.2f}")

    # Count employees by department
    def department_count(self):
        if self.data is not None:
            count = self.data["Department"].value_counts()

            print("\nEmployees by Department:")
            print(count)

    # Filter employees above salary threshold
    def filter_by_salary(self, salary):
        if self.data is not None:
            result = self.data[self.data["Salary"] > salary]

            print(f"\nEmployees earning more than ₹{salary}:")
            print(result)

            return result

    # Export filtered data
    def export_data(self, data, filename):
        if data is not None:
            data.to_csv(filename, index=False)
            print(f"\nData exported successfully to {filename}")


# Create EmployeeAnalyzer object
analyzer = EmployeeAnalyzer("employee_data.csv")

# Load data
analyzer.load_data()

# Display data
analyzer.display_data()

# Calculate average salary
analyzer.average_salary()

# Count employees by department
analyzer.department_count()

# Filter employees earning more than 60000
high_salary = analyzer.filter_by_salary(60000)

# Export filtered employees
analyzer.export_data(
    high_salary,
    "high_salary_employees.csv"
)