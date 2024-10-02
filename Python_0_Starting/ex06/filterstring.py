import sys
from ft_filter import ft_filter

def main(argv: any):
    try:
        assert len(sys.argv) == 3, "Quantidade de argumentos incorreta"
        
        assert argv[2].isdigit(), "bad argument"
        n = int(argv[2])

        text_to_list = argv[1].split()
        words_lst: list = [x for x in text_to_list if x.isalpha()]
        response = ft_filter(lambda word: len(word) > n, words_lst)

        print(response)

    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv)
