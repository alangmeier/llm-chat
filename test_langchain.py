
# Inspired by the procedure available on :
#   - LangChain : https://python.langchain.com/docs/integrations/llms/llamacpp

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig, get_config_list
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# LLM model
# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
model = LlamaCpp(
    model_path='./models/mistral-7b-instruct-v0.1.Q3_K_M.gguf',
    temperature=0,
    max_tokens=2000,
    top_p=0.5,
    streaming=True,
    verbose=True,
    callback_manager=callback_manager,
)
# Prompt template
prompt_template = """[INST] {prompt} [/INST]"""
prompt_template = PromptTemplate(template=prompt_template, input_variables=["prompt"])
# Chain prompt and model following LangChain LCEL
llm_chain = prompt_template | model | StrOutputParser()

# Call LLM on prompt
prompt = "Write 2 paragraphs about flowers"
llm_chain.invoke({"prompt":prompt})