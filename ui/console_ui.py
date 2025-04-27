from core.agent import BankingAgent

def run_console_ui():
    agent = BankingAgent("data/faqs.json")

    print("Bienvenido a tu Asistente Virtual del Banco de Guayaquil")
    
    # Pedimos el nombre al usuario
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Hola {nombre}, ¿cómo estás? Estoy aquí para ayudarte.\n")

    # Mostrar ejemplos de lo que puede preguntar
    print("Puedes preguntarme cosas como:")
    print("- ¿Cuáles son los requisitos para abrir una cuenta de ahorros/corriente?")
    print("- ¿¿Cómo solicito una Tarjeta de Crédito/Débito?")
    print("- ¿Cuál es el horario de atención de las agencias?")
    print("- Quiero calcular la cuota de un préstamo de $10,000 al 36% a 3 años.")
    print("- Transferir de la cuenta 12345 a la cuenta 67890 por $500.\n")

    print("Escribe 'salir' para finalizar.\n")

    while True:
        query = input(f"{nombre}: ")
        if query.lower() == "salir":
            print("\nAsistente: Fue un placer atenderte, estoy aquí si tienes otra inquietud. ¡Hasta pronto!")
            break
        response = agent.handle_query(query)
        print("Asistente:", response)

if __name__ == '__main__':
    run_console_ui()