from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_experimental.tabular_synthetic_data.base import SyntheticDataGenerator
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from langchain_community.llms.ollama import Ollama


class Conversation(BaseModel):
    """A conversation between two people."""

    speaker_1: str
    speaker_2: str
    lines: list[str]


examples = [
    {
        "example": """Speaker 1: Manolo, Speaker 2: Juan, lines: ["Hola, como estas?", "Bien, y tu?"]"""
    }
]


template = PromptTemplate(input_variables=["example"], template="{example}")

prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    examples=examples,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    input_variables=["subject", "extra"],
    example_prompt=template,
)

synthetic_data_generator = SyntheticDataGenerator(
    template=prompt_template, llm=Ollama(model="mistral")
)

synthetic_results = synthetic_data_generator.generate(
    subject="create a phone conversation",
    extra="The coversation has to be between two people and it should have at least 5 lines",
    runs=2,
)
print(synthetic_results)
