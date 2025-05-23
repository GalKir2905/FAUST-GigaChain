from faust_module.common.log import logger

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import load_prompt, ChatPromptTemplate, PromptTemplate
from langchain_experimental.smart_llm import SmartLLMChain


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
            temperature=2
        )

    def get_token(self):
        response = self.giga.get_token()
        return {"access_token": response.access_token, "expires_at": response.expires_at}

    def get_models(self):
        response = self.giga.get_models()
        return response.data

    def chat_model_idea(self, hard_question, ideas=3):
        prompt = PromptTemplate.from_template(hard_question)
        chain = SmartLLMChain(llm=self.giga, prompt=prompt, n_ideas=ideas, verbose=True)
        chain.run({})

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

    def correct_mistakes(self, path_to_prompt: str):
        prompt = load_prompt(path_to_prompt)
        messages = [SystemMessage(content=self.system_role)]
        user_input = input(f"Вопрос: ")
        messages.append(HumanMessage(content=prompt.format(text=user_input)))
        response = self.giga.invoke(messages).content
        return response

    def work_load_prompt(self, path_to_prompt: str, question: str):
        prompt = load_prompt(path_to_prompt)
        messages = [SystemMessage(content=self.system_role)]
        messages.append(HumanMessage(content=prompt.format(text=question)))
        response = self.giga.invoke(messages).content
        logger.info(response)

    def lol_prompt(self, joke_prompt, dict_chain):
        prompt = ChatPromptTemplate.from_template(joke_prompt)
        output_parser = StrOutputParser()
        chain = prompt | self.giga | output_parser
        result = chain.invoke(dict_chain)
        logger.info(result)
        return result
