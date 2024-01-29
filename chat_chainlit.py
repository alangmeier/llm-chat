
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl

import variables as var

@cl.on_chat_start
async def on_chat_start():
    model = LlamaCpp(
        model_path=var.model_path,
        temperature=0,
        max_tokens=2000,
        top_p=0.5,
        streaming=True,
    )

    prompt_template = """[INST] {prompt} [/INST]"""
    prompt_template = PromptTemplate(template=prompt_template, input_variables=["prompt"])
    
    llm_chain = prompt_template | model | StrOutputParser() # LangChain LCEL
    
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