from core.rag import RAG
from tools.loan_calculator import calculate_loan_payment
from tools.transfer_simulator import simulate_transfer
import re  # Importar el módulo re

class BankingAgent:
    def __init__(self, faqs_path):
        self.rag = RAG(faqs_path)

    def handle_query(self, query):
        if "calcular la cuota de un préstamo" in query.lower():
            try:
                # Usar expresiones regulares para extraer los parámetros
                match = re.search(r"\$(\d+[\.,]?\d*)[\s]*al[\s]*(\d+[\.,]?\d*)%[\s]*a[\s]*(\d+)[\s]*años", query, re.IGNORECASE)
                if match:
                    amount = float(match.group(1).replace(",", "."))
                    interest_rate = float(match.group(2).replace(",", ".")) / 100
                    term_years = int(match.group(3))
                    return calculate_loan_payment(amount, interest_rate, term_years)
                else:
                    raise ValueError  # Provocar el ValueError si no se encuentran los parámetros
            except ValueError:
                return "Por favor, proporcione la información del préstamo en el formato correcto (ej: $10000 al 12% a 3 años)."
        elif "transferir" in query.lower() and "cuenta" in query.lower() and "$" in query.lower():
            try:
                from_account = query.split("cuenta ")[1].split(" a")[0]
                to_account = query.split("cuenta ")[-1].split(" por")[0]
                amount = float(query.split("$")[1])
                return simulate_transfer(from_account, to_account, amount)
            except ValueError:
                return "Por favor, proporcione la información de la transferencia en el formato correcto (ej: transferir de la cuenta 12345 a la cuenta 67890 por $500)."
        else:
            return self.rag.get_answer(query)

if __name__ == '__main__':
    agent = BankingAgent("C:/Users/Juan/Documents/asistente_bancario/data/faqs.json", 
                    "C:/Users/Juan/Documents/asistente_bancario/data/accounts.json", 
                    "C:/Users/Juan/Documents/asistente_bancario/data/loans.json")
    print(agent.handle_query("¿Cuáles son los requisitos para abrir una cuenta de ahorros?"))
    print(agent.handle_query("Quiero calcular la cuota de un préstamo de $10,000 al 12% a 3 años."))
    print(agent.handle_query("Quiero transferir de la cuenta 12345 a la cuenta 67890 por $500."))