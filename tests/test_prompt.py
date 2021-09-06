from mandatum import Prompt

def test_prompt():
    prompt = Prompt()

    input = prompt.input("Prompt : ")
    print(input)

if __name__ == "__main__":
    test_prompt()