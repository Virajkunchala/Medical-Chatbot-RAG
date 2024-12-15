from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini


import os

# load documents
documents = SimpleDirectoryReader(input_files=["MetaGPT_Meta_Programming.pdf"]).load_data()

splitter = SentenceSplitter(chunk_size=1024)
nodes = splitter.get_nodes_from_documents(documents)

## Define LLM and Embedding model

model_name = "models/embedding-001"
embed_model = GeminiEmbedding(
    model_name=model_name, api_key=os.environ["GOOGLE_API_KEY"], title="this is a document"
)

Settings.llm = Gemini( model="models/gemini-1.5-flash")
Settings.embed_model = GeminiEmbedding(model=model_name)

embeddings = embed_model.get_text_embedding("Google Gemini Embeddings.")

## Define Summary Index and Vector Index over the Same Data
from llama_index.core import SummaryIndex, VectorStoreIndex

summary_index = SummaryIndex(nodes)
vector_index = VectorStoreIndex(nodes)

## Define Query Engines and Set Metadata
summary_query_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",
    use_async=True,
)
vector_query_engine = vector_index.as_query_engine()

from llama_index.core.tools import QueryEngineTool


summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    description=(
        "Useful for summarization questions related to MetaGPT"
    ),
)

vector_tool = QueryEngineTool.from_defaults(
    query_engine=vector_query_engine,
    description=(
        "Useful for retrieving specific context from the MetaGPT paper."
    ),
)
## Define Router Query Engine
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector


query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        summary_tool,
        vector_tool,
    ],
    verbose=True
)
response = query_engine.query("How do agents share information with other agents?"
)
print(str(response))