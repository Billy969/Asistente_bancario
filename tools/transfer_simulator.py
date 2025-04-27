import datetime
import random

def simulate_transfer(from_account, to_account, amount):
    """Simula una transferencia entre cuentas."""

    try:
        from_account = str(from_account)
        to_account = str(to_account)
        amount = float(amount)

        transfer_id = random.randint(100000, 999999)
        transfer_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "Mensaje_de_Confirmación": f"Transferencia de ${amount} desde la cuenta {from_account} a la cuenta {to_account} exitosa.",
            "transfer_id": transfer_id,
            "transfer_date": transfer_date
        }
    except ValueError:
        return "Error: Por favor, ingrese un monto válido."
    except Exception as e:
        return f"Error inesperado: {e}"

if __name__ == '__main__':
    # Ejemplo de uso
    result = simulate_transfer("12345", "67890", 500)
    print(result)