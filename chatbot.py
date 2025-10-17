import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatbot_response(user_input: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant with healthcare expertise, but can answer general queries."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
