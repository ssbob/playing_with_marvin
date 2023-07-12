import os

import marvin
from dotenv import load_dotenv
from marvin import ai_model
from pydantic import BaseModel, Field

load_dotenv()

marvin.settings.openai_api_key = os.getenv("OPENAI_API_KEY")


@ai_model
class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")


print(Location("The Big Apple"))
