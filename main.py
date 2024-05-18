from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()


@tool
def get_text_length(text:str)->int:
    """Return the length of a string by character"""
    text=text.strip("'\n").strip('"')
    return len(text)

if( __name__ =='__main__'):
    print('hello')
    print(get_text_length("dog"))


