import os
from models import Cliente, Projeto, Contrato, Chunk
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
)

def determinar_segmento(texto_contrato):
    segmentos_texto = ", ".join([valor for valor, _ in Cliente.SEGMENTO_CHOICES])

    prompt_template = """Você é um analista da empresa NovaTec responsável por
categorizar clientes em segmentos de mercado, com base no texto de um contrato.

Segmentos disponíveis: {segmentos}

Retorne apenas o nome do segmento que mais se encaixa com o cliente.

Texto do contrato:
\"\"\"
{texto_contrato}
\"\"\"
"""

    prompt_final = prompt_template.format(
        segmentos=segmentos_texto,
        texto_contrato=texto_contrato
    )

    response = llm.invoke(prompt_final)
    return response

def determinar_valor(texto_contrato):
    prompt_template = """Você é um analista da empresa NovaTec responsável por
obter o valor de um contrato, a partir de um texto deste.

Retorne apenas o valor do contrato dado.

Texto do contrato:
\"\"\"
{texto_contrato}
\"\"\"
"""

    prompt_final = prompt_template.format(
        texto_contrato=texto_contrato
    )

    response = llm.invoke(prompt_final)
    return response

