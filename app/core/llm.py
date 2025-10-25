import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

prompt_template = """
You are an expert research assistant. Your task is to provide a factual and concise answer to the user's query based on the provided context.
If the context does not contain the answer, state that you don't know.

**Context:**
{document_context}

---

**Few-shot Examples:**

*   **Query:** What were the company's net profits in 2023?
    **Context:** The annual report states that the company's revenue was $5 million in 2023, with expenses totaling $3 million.
    **Answer:** The company's net profit in 2023 was $2 million.

*   **Query:** What is the capital of France?
    **Context:** The Eiffel Tower is a famous landmark in Paris.
    **Answer:** The provided context does not mention the capital of France.

---

**User Query:** {user_query}

**Answer:**
"""

def generate_answer(user_query: str, context_documents: list):
    """Generates an answer using the LLM based on the user query and context."""
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    
    llm_engine = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        groq_api_key=groq_api_key
    )
    
    conversation_prompt = ChatPromptTemplate.from_template(prompt_template)
    
    chain = conversation_prompt | llm_engine
    
    response = chain.invoke({"user_query": user_query, "document_context": context_text})
    
    return response.content