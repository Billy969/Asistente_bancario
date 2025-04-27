def calculate_loan_payment(amount, interest_rate, term_years):
    """Calcula la cuota mensual de un préstamo."""
    try:
        amount = float(amount)
        interest_rate = float(interest_rate)
        term_years = int(term_years)

        monthly_interest_rate = interest_rate / 12
        num_payments = term_years * 12

        payment = (amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
        total_payment = payment * num_payments

        return {
            "Pago_Mensual": round(payment, 2),
            "Pago_Total": round(total_payment, 2)
        }
    except ValueError:
        return "Error: Por favor, ingrese valores numéricos válidos."
    except Exception as e:
        return f"Error inesperado: {e}"