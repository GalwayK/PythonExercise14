import openai
import os

KEY = os.getenv("OpenAI_SecretKey")


class Chatbot:
    def __init__(self, key=KEY):
        openai.api_key = key

    def get_response(self, user_input):
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt=user_input,
                                            max_tokens=4000,
                                            temperature=0.5).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a funny joke that is not about fish.")
    print(response)
