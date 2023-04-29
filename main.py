# This is a sample Python script.
from dotenv import load_dotenv, find_dotenv


# Load Environmental Variables
load_dotenv(find_dotenv())


def test():
    llm = OpenAI(model_name='text-davinci-003')
    prompt = ""
    print(llm(prompt))


if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
