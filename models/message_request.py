from typing import Optional
from pydantic import BaseModel

class MessageRequest(BaseModel):
    user_id: Optional[str]
    intent: Optional[str]
    message: Optional[str]