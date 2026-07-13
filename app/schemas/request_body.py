from pydantic import BaseModel, Field 

class ChatRequest(BaseModel):
    query: str = Field(..., examples=["What is Git?",
                                      "How do I save changes to my repository?",
                                      "How can I create a new branch?"])