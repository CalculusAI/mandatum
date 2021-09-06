from mandatum import Mode

def test_mode():
    mode = Mode("MyMode", "MyModeDescription")
    mode.init_prompt()

    def run_my_mode():
        name = mode.prompt.input("Name : ")
        print(name)

    mode.run(run_my_mode)

if __name__ == "__main__":
    test_mode()