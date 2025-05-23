import configparser
import sys
import argparse

from faust_module.common.log import logger
from faust_module.GigaChain.client import FAUST_GIGACHAT
from faust_module.common.global_vars import *
sys.tracebacklimit = 0
from pathlib import Path


def main(args):
    module_dir = Path("faust_workspace")
    config_dir = Path("configs")
    config = configparser.ConfigParser()
    config.read(f"{config_dir}/conf.ini")
    profile = config['faust_giga']
    client_gigachat = FAUST_GIGACHAT(profile.get('authorization_key'), "GigaChat-Pro")

    ## Еще не работает. Нет выхода интернет и прав на "тачку"
    # client_gigachat.chat_model_longer()

    ## Работает.
    # resp = client_gigachat.correct_mistakes(f"{workspace_prompts}\\correction.yaml")
    # client_gigachat.work_load_prompt(f"{workspace_prompts}\\translation.yaml", resp)

    ## Работает.
    # client_gigachat.lol_prompt(
    #     "Придумай анегдот про то, как сидели {персона} и {персона_2} в баре и болтали про игры. !Условие {персона} плохо играет в стрелялки",
    #     {"персона": "Вадим", "персона_2": "Кирилл"})
    #


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--workspace", type=str, default="", help="Путь до рабочей диры", dest="workspace")
    args = args.parse_args()
    main(args)
