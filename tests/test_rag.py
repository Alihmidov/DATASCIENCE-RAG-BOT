from app.core.llm_logic import ask_bot
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.skip_if_no_ollama
def test_answer():
    question = "Who is Michael Jackson?"
    answer = ask_bot(question)
    
    assert "i'm sorry, but that information is not available in the provided document." in answer.lower()