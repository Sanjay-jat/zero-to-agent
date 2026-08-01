from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

text="""This is a sample text that we will use to demonstrate the functionality of the SemanticChunker. The splitter will divide this text into smaller chunks based on the specified chunk size and overlap. Each chunk will be separated by a period, and we will see how the text is split accordingly

Terrorism is a global threat that requires a comprehensive and coordinated response from the international community. It is essential to address the root causes of terrorism, including political, social, and economic factors, and to promote dialogue and understanding among different cultures and religions. Additionally, it is crucial to strengthen international cooperation and intelligence sharing to prevent terrorist attacks and bring perpetrators to justice. By working together, we can create a safer and more secure world for future generations.
"""

text_splitter = SemanticChunker(
    embeddings,breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.0

)

splits = text_splitter.split_text(text)
print(splits)