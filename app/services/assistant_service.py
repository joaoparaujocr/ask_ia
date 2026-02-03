from chains.sales_assistant_chain import sales_assistant_chain

class AssistantService:
    def answer(self, question: str) -> str:
        return sales_assistant_chain.invoke({
            "question": question
        })