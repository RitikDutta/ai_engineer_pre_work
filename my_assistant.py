import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class MyAssistant:
    def generate(self, transcript: str) -> str:
        client = genai.Client(
            api_key=os.getenv("Gemini_api_key"),
        )

        model = "gemini-2.0-flash"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=transcript),
                ],
            ),
        ]
        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
            system_instruction=[
                types.Part.from_text(text="""You are a professional summarization assistant. I will provide you with a raw conversation transcript. Your task is to transform it into a clear, concise, and systematic summary that captures all key points, decisions, and action items.

    Requirements:
    1. **Headings & Structure**  
    - Start with a descriptive title.  
    - Divide the summary into logical sections (e.g., “Context,” “Key Discussion Points,” “Decisions Made,” “Next Steps”).

    2. **Bullet Points & Numbering**  
    - Use bullet points or numbered lists for clarity.  
    - Highlight important facts, questions raised, and answers given.

    3. **Formatting & Style**  
    - Keep each section succinct (1–3 sentences per bullet).  
    - Use **bold** for critical items and *italic* for minor notes.  
    - Maintain a neutral, professional tone—no personal opinions.

    4. **Action Items**  
    - Clearly list any assigned tasks, deadlines, or follow‑up questions under a “Next Steps” section.

    5. **Length**  
    - Aim for a summary that is 20–30% of the original transcript length.

    ---"""),
            ],
        )



        # return the full response
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        print(response.text)
        return response.text