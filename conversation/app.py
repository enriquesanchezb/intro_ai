import streamlit as st
from typing import List
import json

from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.tabular_synthetic_data.base import SyntheticDataGenerator
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from langchain_community.llms.ollama import Ollama
from langchain.output_parsers import PydanticOutputParser


class Conversation(BaseModel):
    """A conversation between two people."""

    speaker_1: str = Field(description="The first speaker")
    speaker_2: str = Field(description="The second speaker")
    sentences: List[str] = Field(description="The lines of the conversation")


examples = [
    {
        "example": """Manolo, Juan, sentences: ["Hola, como estas?", "Bien, y tu?, "Muy bien, gracias, y tu?", "Yo tambien muy bien, gracias", "Que bueno, nos vemos luego!", "Adios!"]"""
    }
]


prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    examples=examples,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    input_variables=["subject", "extra"],
    example_prompt=PromptTemplate(input_variables=["example"], template="{example}"),
)


def generate_response(topic: str):
    synthetic_data_generator = SyntheticDataGenerator(
        template=prompt_template, llm=Ollama(model="mistral")
    )

    synthetic_results = synthetic_data_generator.generate(
        subject="create a phone conversation using a json format {speaker1: <name>, speaker2: <name>, sentences: <list of sentences>}",
        extra=f"the {topic} for the conversation is {topic}",
        runs=1,
    )

    st.info(f"📝 Generated conversation:\n{synthetic_results[0]}")
    result = json.loads(synthetic_results[0])
    # Extraer los nombres de los participantes
    col1, col2 = st.columns(2)
    col1.write(f"👨‍💻 {result['speaker1']}")
    col2.write(f"👩‍💻 {result['speaker2']}")
    sentences = result["sentences"]
    for i, sentence in enumerate(sentences):
        if i % 2 == 0:
            col1.write(sentence)
            col2.write("")
        else:
            col1.write("")
            col2.write(sentence)


st.title("📲 Conversation Quickstart App")

with st.form("my_form"):
    text = st.text_area("Enter topic to discuss:", "Write a topic for the conversation")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
