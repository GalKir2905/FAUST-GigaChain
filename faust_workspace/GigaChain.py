from gigachat import GigaChat
import json
import argparse
from faust_module.log import logger
from faust_module.GigaChain.client import FAUST_GIGACHAT
import sys
sys.tracebacklimit = 0



def main(args):
    client_gigachat = FAUST_GIGACHAT(
        "Y2EzYWUxZGEtN2ZhYi00NmIzLTk2NzYtZDI5NDcyYzY5MDFkOjIwYjBlNWI1LWU2OTQtNDdlYi1iYTJjLWUxMzg5MTkwOGQwOQ==",
        "GigaChat-Pro", "Ты быдло, который пишет каждое слово через мат."
    )

    # client_gigachat.chat_model_longer() ## Еще не работает. Нет выхода интернет и прав на "тачку"
    qwerty = client_gigachat.work_load_prompt("Z:\\Program\\FAUST\\FAUST-GigaChain\\faust_module\\GigaChain\\prompts\\contents\\correction.yaml")
    logger.info(qwerty)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--workspace", type=str, default="", help="Путь до рабочей диры", dest="workspace")
    args = args.parse_args()
    main(args)
