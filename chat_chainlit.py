
# Inspired by the procedures available on :
#   - Chainlit : https://docs.chainlit.io/integrations/langchain
#   - LangChain : https://python.langchain.com/docs/integrations/llms/llamacpp

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    # LLM model
    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    model = LlamaCpp(
        model_path='./models/mistral-7b-instruct-v0.1.Q3_K_M.gguf',
        temperature=0,
        max_tokens=2000,
        top_p=0.5,
        streaming=True,
        # verbose=True,
        # callback_manager=callback_manager,
    )
    # Prompt template
    prompt_template = """[INST] {prompt} [/INST]"""
    prompt_template = PromptTemplate(template=prompt_template, input_variables=["prompt"])
    # Chain prompt and model following LangChain LCEL
    llm_chain = prompt_template | model | StrOutputParser()
    # Set the LLM runnable into the user session
    cl.user_session.set("runnable", llm_chain)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    msg = cl.Message(content="")
    
    # Need to use the sync method and call `make_async` because llama-cpp does not support async calls
    for chunk in await cl.make_async(runnable.stream)(
        {"prompt": message.content},
        config = RunnableConfig(callbacks=[cl.AsyncLangchainCallbackHandler()]),
    ) :
       await msg.stream_token(chunk)
    
    await msg.send()