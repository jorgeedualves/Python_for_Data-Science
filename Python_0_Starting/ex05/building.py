import sys, string

def main():

    try:
        if len(sys.argv) > 2:
            raise Exception("More than one argument is provided")
        assert len(sys.argv) == 2, "Usage: provide a string"

        chars = len(sys.argv[1])
        uppers = len([char for char in sys.argv[1] if char.isupper()])
        lowers = len([char for char in sys.argv[1] if char.islower()])
        punctuations = len([char for char in sys.argv[1] if char in string.punctuation])
        spaces = len([char for char in sys.argv[1] if char.isspace()])
        digits = len([char for char in sys.argv[1] if char.isdigit()])


        print(f"The text contains {chars} characters:")
        print(f"{uppers} upper letters")
        print(f"{lowers} lower letters")
        print(f"{punctuations} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
if __name__ == "__main__":
    main()    
