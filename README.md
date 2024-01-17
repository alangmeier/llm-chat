---
title: Personal CPU-powered AI Chat-Assistant
author: alangmeier
date: 09 January 2024
keywords: [AI, LLM, Chatbot, llama-cpp, LangChain, Chainlit, CPU]
---

# Personal CPU-powered AI Chat-Assistant
***README IN PROGRESS***

At first, I wondered *if* and *how* I could implement a LLM-powered chatbot on my own laptop, without crazy computing power. And that's how this mini-project came to life.

This repository contains a simple implementation of an AI chatbot based on lightweight / quantized LLM models. The idea is to run a chat-like app powered by a pre-trained LLM model, on a regular CPU.

---
<!-- TODO -->
*Showcase a video demonstration*

---

## Setup configuration
### Environment
The application is implemented in Python and leverages the following libraries / packages :
- [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) : a Python binding for [`llama.cpp`](https://github.com/ggerganov/llama.cpp), indirectly called through `langchain`
- [`langchain`](https://github.com/langchain-ai/langchain) : a framework for developing applications powered by language models
- [`chainlit`](https://github.com/Chainlit/chainlit) : an async framework to build ChatGPT-like applications

In order to install the required packages, use the following command using `pip` :

```
$ pip install -r requirements.txt
```

### Models
The LLM models that are used here are called [*quantized models*](https://huggingface.co/docs/optimum/concept_guides/quantization). While still maintaing good performance, these models are lighter and can be used to perform inference at a lesser computational cost.

Quantized models can be found in GGUF format ([the successor of GGML format](https://medium.com/@phillipgimmi/what-is-gguf-and-ggml-e364834d241c)). The procedure to download quantized models is explained in [`models/README.md`](models/README.md).

### LangChain
LangChain is a framework which integrates `llama-cpp-python`. Together, these packages allow the instantiation of the quantized models that are used in this repo. Some examples are available [here](https://python.langchain.com/docs/integrations/llms/llamacpp#usage), where only the CPU sections have been considered.

In addition, LangChain provides an easy-to-use syntax ([LCEL](https://python.langchain.com/docs/expression_language/)) for writing LLM chains that allows, in particular, streaming of the models's answer.

### Chainlit
TODO :
- chainlit with langchain (https://docs.chainlit.io/integrations/langchain)
- `make_async` for Llama-cpp models (does not support async calls) 
- `run` command

## TODO
- [x] Modification of `chainlit.md` as Welcome page for the chat
- [ ] Chainlit chat customization
- [ ] A video/GIF of the LLM in action
- [ ] `models`/`README.md`
- [ ] Change paths to models
- [ ] `.local/share/applications/llm_chat.desktop` with explainations for desktop icons
- [ ] Roadmap

## Roadmap
- [ ] Memory buffer ?
- [ ] RAG implementation ?
- [ ] Test some other models ?