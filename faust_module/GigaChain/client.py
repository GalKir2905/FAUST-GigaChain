from faust_module.log import logger
import json

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import load_prompt


class FAUST_GIGACHAT:
    def __init__(self, authorization_key, model="GigaChat:latest", system_role="Ты разработчик на python."):
        self.authorization_key: str = authorization_key
        self.model: str = model
        self.system_role: str = system_role
        self.giga = GigaChat(
            # Для авторизации запросов нужен ключ, полученный в проекте GigaChat API
            credentials=self.authorization_key,
            scope="GIGACHAT_API_PERS",
            model="GigaChat-Pro",
            verify_ssl_certs=False,
        )

    def get_token(self):
        response = self.giga.get_token()
        return {"access_token": response.access_token, "expires_at": response.expires_at}

    def get_models(self):
        response = self.giga.get_models()
        return response.data

    def chat_model_longer(self, system_role: str ='Ты разработчик на python.'):
        messages = [SystemMessage(content=self.system_role)]
        while True:
            # user_input = input(f"Вопрос: ")
            # if user_input.lower() == "спасибо":
            #     break
            # messages.append(HumanMessage(content=user_input))
            messages.append(HumanMessage(content="Сколько времени?"))
            res = self.giga.invoke(messages)
            messages.append(res)
            logger.info(f"Ответ: {res.content}")
            break

    def work_load_prompt(self, path_to_prompt: str):
        prompt = load_prompt(path_to_prompt)
        messages = [SystemMessage(content=self.system_role)]
        user_input = input(f"Вопрос: ")
        messages.append(HumanMessage(content=prompt.format(text=user_input)))
        resource = self.giga.invoke(messages).content
        # logger.info(f"Ответ: {resource}")
        return resource
