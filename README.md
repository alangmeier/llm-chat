---
title: Personal CPU-powered AI Chat-Assistant
author: alangmeier
date: 09 January 2024
keywords: [AI, LLM, Chatbot, llama-cpp, LangChain, Chainlit, CPU]
---

# Personal CPU-powered AI Chat-Assistant

This repository contains a simple implementation of an AI chatbot based on lightweight / quantized LLM models. The idea is to run a chat-like app powered by a pre-trained LLM model, on a regular CPU.

The application is implemented in Python and leverages the following libraries / packages :
- [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) : a Python binding for [`llama.cpp`](https://github.com/ggerganov/llama.cpp)
- [`langchain`](https://github.com/langchain-ai/langchain) : a framework for developing applications powered by language models
- [`chainlit`](https://github.com/Chainlit/chainlit) : an async framework to build ChatGPT-like applications

---
***README IN PROGRESS***

## Some demonstrations
- [ ] A video/GIF of the LLM in action

## Setup configuration and installation
List of main components + some words on them + how to install them :
- [ ] Models (`TheBloke` on HuggingFace and GGUF models -> models/README.md)
- [ ] Llama-cpp (does not support async calls)
- [ ] Langchain (LCEL)
- [ ] Chainlit (`make_async` for Llama-cpp models)
- [ ] `.local/share/applications/llm_chat.desktop` with explainations for icons as well

## TODO
- [ ] This README
- [ ] `models`/`README.md`
- [ ] Change paths to models
- [ ] Modification of `chainlit.md` as Welcome page for the chat
- [ ] Chainlit chat customization
- [ ] Roadmap

## Roadmap
- [ ] Memory buffer ?
- [ ] RAG implementation ?
- [ ] Test some other models ?