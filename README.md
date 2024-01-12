# Intro AI

This repo is a collection of simple script to show how to work with AI.

## Setup

Simply run the Makefile

```
make
```

and install dependencies

```
pip3 install poetry
poetry install
```

To execute any script:

```
poetry run python <name_of_the_script>.py
```

## Access to the model

```
make run
```

You can modify the model using `Modelfile` and use it with

```
make run-new-model
```

## Scripts

### 1. Basic chat

Execute a shell with a simple chat where you can interact with the Model

```
poetry run python basic_chat.py
```

### 2. Langchain chat

This time, we use [langchain](https://python.langchain.com/docs/get_started/introduction) to interact with the model

```
poetry run python langchain_chat.py
```

### 3. Langchain add files

Show you how to add files into the model and how to interact with them

```
poetry run python langchain_add_files.py
```

### 4. Langchain summarize

Access to a website and extract a summarization of it

```
poetry run python langchain_summarize.py
```

### 5. Synthetic data

How to generate synthetic data from a prompt

```
poetry run python synthetic_data.py
```


