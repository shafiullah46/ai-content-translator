import os
from openai import OpenAI

# Initialize the OpenAI client with environment variables
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def translate_to_language(text: str, language: str) -> str:
    """
    Translates English text into specific target languages.
    """
    parameterized_prompt = (
        f"Translate the following English text into Spanish and French. "
        f"Provide both translations clearly labeled.\n\n"
        f"Text to translate:\n{text}"
    )
    
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": parameterized_prompt}
        ],
        max_tokens=100,
        temperature=0.7
    )
    
    try:
        translation_text = response.choices[0].message.content.strip()
    except (TypeError, AttributeError):
        try:
            choice = response['choices'] if isinstance(response, dict) else response.choices
            if isinstance(choice, list) and len(choice) > 0:
                item = choice[0]
                if isinstance(item, dict):
                    translation_text = item['message']['content'].strip()
                else:
                    translation_text = item.message.content.strip()
            elif isinstance(choice, dict):
                translation_text = choice['message']['content'].strip()
            else:
                translation_text = str(response)
        except Exception:
            translation_text = str(response)
            
    return translation_text

if __name__ == "__main__":
    english_text = "Good morning, how are you?"
    translations = translate_to_language(english_text, language="Spanish and French")
    print("--- Translated Outputs ---")
    print(translations)
