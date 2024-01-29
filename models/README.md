# How to use quantized models

In order to use quantized models in this project, some steps must be followed.

1. First, find a GGUF model that suits your needs (storage, compute, accuracy). There are many models available on HuggingFace, for example [TheBloke](https://huggingface.co/TheBloke) releases quantized versions of most of the LLM models..

1. After finding the right model, one must verify that it is compatible with `llama.cpp`. This can be done on the repo (https://github.com/ggerganov/llama.cpp#description) or it is sometimes mentioned in the model cards.

1. At that point, the GGUF model can be downloaded. The procedure to download models from HuggingFace is described here :
    1. `huggingface_hub` must be installed, using `conda` :
    ```
    conda install -c conda-forge huggingface_hub
    ```
    Or using `pip` :
    ```
    pip install --upgrade huggingface_hub
    ```
    For more details, refer to the [installation page](https://huggingface.co/docs/huggingface_hub/installation).
    
    - Then download the model from the repo :
    ```
    huggingface-cli download <repo_id> <model file> --local-dir . --local-dir-use-symlinks False
    ```
    For example, in order to download a model from [this repository](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF), `<repo_id>` must be replaced by `TheBloke/Llama-2-13B-chat-GGUF` and `<model file>` can be replaced by `llama-2-13b-chat.Q4_0.gguf`.

    - It's also possible to generate a GGUF file from an existing model. For this, refer to [`llama.cpp`'s repo](https://github.com/ggerganov/llama.cpp).

1. The models that have been used so far are subjectively listed below from the most accurate to the least :
    1. [Mistral 7B Instruct v0.1](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) : Q3_K_M
    1. [Llama 2 7B Chat](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF) : Q3_K_M