import sys

def main():
    try:

        assert len(sys.argv) <= 2, "more than one argument is provided"

        if(int(sys.argv[1]) % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print("Argument is not a valid integer.")
    except IndexError as e:
        print("AssertionError: list index out of range")
    
if __name__ == "__main__":
    main()