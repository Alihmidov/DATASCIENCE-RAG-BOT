from app.core.llm_logic import ask_bot
import pytest

@pytest.mark.skip(reason="Ollama server is not available in the CI environment")
def test_answer():
    question = "Who is Michael Jackson?"
    answer = ask_bot(question)
    
    assert "i'm sorry, but that information is not available in the provided document." in answer.lower()