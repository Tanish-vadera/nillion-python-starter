from nada_dsl import *

def nada_main():
    # Define parties involved
    company_a = Party(name="Company A")
    company_b = Party(name="Company B")
    company_c = Party(name="Company C")

    # Define secret inputs from each party
    secret_salary_a = SecretInteger(Input(name="company_a_salary", party=company_a))
    secret_salary_b = SecretInteger(Input(name="company_b_salary", party=company_b))
    secret_salary_c = SecretInteger(Input(name="company_c_salary", party=company_c))

    # Securely compute the total sum of the secret salaries
    total_salary = secret_salary_a + secret_salary_b + secret_salary_c

    # Securely compute the average salary
    number_of_companies = SecretInteger(3)  # We know we have 3 companies
    average_salary = total_salary / number_of_companies

    # Define outputs for each company
    output_a = Output(average_salary, "average_salary_output_a", company_a)
    output_b = Output(average_salary, "average_salary_output_b", company_b)
    output_c = Output(average_salary, "average_salary_output_c", company_c)

    return [output_a, output_b, output_c]

# Utility function for logging (if needed for debugging)
def log(message):
    print(f"[LOG]: {message}")

