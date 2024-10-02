import sys

def main(argv: any):

    thisdict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----','2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        word_list = argv[1].split()

        for word in word_list:
              assert word.isalpha(), "the arguments are bad"
        
        text = argv[1].upper()

        for char in text:
            print(thisdict[char],end = '')
        print('')

    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main(sys.argv)