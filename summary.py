{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOU/w2q44l04XV4xirB76sJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aarnaty/Extracto/blob/main/summary.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uic3O02isu_X"
      },
      "outputs": [],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install langchain"
      ],
      "metadata": {
        "id": "1yME7T-Us_yo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pip install openai"
      ],
      "metadata": {
        "id": "G9YCxH1gtM7x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pip install tiktoken"
      ],
      "metadata": {
        "id": "B16iDOGGtY_C"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from langchain import OpenAI\n",
        "from langchain.docstore.document import Document\n",
        "from langchain.text_splitter import CharacterTextSplitter\n",
        "from langchain.chains.summarize import load_summarize_chain\n",
        "\n",
        "def generate_response(txt):\n",
        "    openai_api_key=\"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\"\n",
        "    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)\n",
        "    text_splitter = CharacterTextSplitter()\n",
        "    texts = text_splitter.split_text(txt)\n",
        "    docs = [Document(page_content=t) for t in texts]\n",
        "    chain = load_summarize_chain(llm, chain_type='map_reduce')\n",
        "    return chain.run(docs)\n",
        "\n",
        "st.set_page_config(page_title='🦜🔗 Text Summarization App')\n",
        "st.title('🦜🔗 Text Summarization App')\n",
        "\n",
        "txt_input = st.text_area('Enter your text', '', height=200)\n",
        "\n",
        "result = []\n",
        "with st.form('summarize_form', clear_on_submit=True):\n",
        "    openai_api_key = st.text_input('OpenAI API Key', type = 'password', disabled=not txt_input)\n",
        "    submitted = st.form_submit_button('Submit')\n",
        "    if submitted and openai_api_key.startswith('sk-'):\n",
        "        with st.spinner('Calculating...'):\n",
        "            response = generate_response(txt_input)\n",
        "            result.append(response)\n",
        "            del openai_api_key\n",
        "\n",
        "if len(result):\n",
        "    st.info(response)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OgE1WBustkcD",
        "outputId": "1868c6d0-c9ad-42ae-e7f4-2732f289a952"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-10-15 19:03:28.458 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ]
    }
  ]
}