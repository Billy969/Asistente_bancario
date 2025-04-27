Asistente Virtual del Banco de Guayaquil
Este proyecto es un agente inteligente que responde preguntas frecuentes, calcula cuotas de préstamos y simula transferencias bancarias.
Fue desarrollado como parte de una prueba técnica para demostrar el uso de RAG (Retrieval Augmented Generation) combinado con herramientas externas.

📂 Estructura del proyecto
graphql
Copiar
Editar![image](https://github.com/user-attachments/assets/a1f69dae-ef59-4637-be97-aaf34fabc136)

asistente_bancario/
│
├── main.py                # Archivo principal para ejecutar el asistente
│
├── core/
│   ├── agent.py            # Orquestador: decide si usar RAG o una herramienta
│   ├── rag.py              # Motor RAG para buscar en FAQs y otros datos
│
├── tools/
│   ├── loan_calculator.py  # Calculadora de cuota de préstamos
│   ├── transfer_simulator.py # Simulador de transferencias bancarias
│
├── ui/
│   └── console_ui.py       # Interfaz de usuario en consola
│
├── data/
│   ├── faqs.json           # Preguntas frecuentes
│   ├── accounts.json       # Datos de cuentas bancarias
│   ├── loans.json          # Datos de tipos de préstamos
│   ├── examples.json       # Ejemplos de preguntas sugeridas
│
└── README.md               # Este archivo
🚀 ¿Cómo ejecutar el proyecto?
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/asistente_bancario.git
cd asistente_bancario
Instala las dependencias necesarias:

bash
Copiar
Editar
pip install scikit-learn
Ejecuta el asistente:

bash
Copiar
Editar
python main.py
💡 Funcionalidades principales
Buscar respuestas a preguntas frecuentes mediante un motor RAG basado en TF-IDF.

Calcular cuotas de préstamos de tipo Hipotecario, Automotriz o Personal.

Simular transferencias entre cuentas bancarias.

Saludo personalizado al iniciar sesión.

Despedida amigable al salir.

Sugerencias de preguntas automáticas usando ejemplos de un archivo examples.json.

🧠 Tecnologías usadas
Python 3

scikit-learn (TF-IDF Vectorizer y Cosine Similarity)

JSON para manejo de bases de datos internas (FAQs, cuentas y préstamos)

📈 Mejoras a futuro
Incorporar embeddings avanzados (por ejemplo OpenAI o Sentence Transformers) para mejorar el RAG.

Conectar a APIs reales de bancos para operaciones reales.

Desarrollar una interfaz web (usando Flask o FastAPI).

Automatizar la actualización de bases de datos.

🤝 Autor
Juan Jose Acosta Burbano

[\[Mi LinkedIn\]](https://www.linkedin.com/in/juan-acosta-a769871b9/)

✨ Ejemplo de interacción
bash
Copiar
Editar
Bienvenido a tu Asistente Virtual del Banco de Guayaquil
¿Cuál es tu nombre? Juan
Hola Juan, ¿cómo estás? Estoy aquí para ayudarte.

Puedes preguntarme cosas como:
- ¿Cuáles son los requisitos para abrir una cuenta de ahorros?
- ¿Cuál es el horario de atención de la agencia principal?
- Quiero calcular la cuota de un préstamo de $10,000 al 12% a 3 años.
- Quiero hacer una transferencia de mi cuenta 12345 a la cuenta 67890 por $500.

Juan: ¿Cuáles son los requisitos para abrir una cuenta de ahorros?
Asistente: Los requisitos son: copia de la cédula, papeleta de votación y un depósito mínimo de $100.
