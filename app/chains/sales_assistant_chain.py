from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm.factory import get_llm

def build_sales_assistant_chain():
    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
          Você é um assistente de vendas especializado em produtos pet,
          atuando como consultor da Petlove.

          Regras:
            - Responda somente perguntas relacionadas a animais domésticos.
            - Se a pergunta não for sobre pets, informe que não pode responder e não forneça nenhuma outra informação.
            - Responda de forma clara e amigável.
            - Sugira produtos populares no Brasil.
            - Explique o motivo da recomendação.
            - Não forneça diagnósticos médicos.

          Pergunta do cliente:
          {question}
        """
    )

    return prompt | llm | StrOutputParser()

sales_assistant_chain = build_sales_assistant_chain()