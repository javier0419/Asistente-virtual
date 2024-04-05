from openai import OpenAI


def chat_with_gpt(prompt, api_key):

    client = OpenAI(api_key=api_key)
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
            stop=None,
        )

        if response.choices:
            return response.choices[0].text.strip()
        else:
            print("La respuesta está vacía.")
            return None

    except Exception as e:
        print(f"Error al interactuar con OpenAI: {e}")
        return None
