#python string indexing and slicing 
def demonstrate_indexing():
    # Sample string 
    text = 'python'
    print("working with string:", text)
    print("length:", len(text))

    # Forward indexing (0 to length -1)
    print("\nForward indexing:")
    print(f"First character (index 0): {text[0]}")
    print(f"Second character (index 1): {text[1]}")
    print(f"Third character (index 2): {text[2]}")

    # Backward indexing (-1 to - length)
    print("\nBackward indexing:")
    print(f"Last character (index -1): {text[-1]}")
    print(f"Second-to-last character (index -2): {text[-2]}")
    print(f"Third-to-last character (index -3): {text[-3]}")


def demonstrate_slicing():
    text = "Python Programming"
    print("\nWorking with Slicing")

    # Basic slicing [start:end] end is exclusive
    print("\nBasic Slicing:")
    print(f"Characters from index 0 to 6: {text[0:6]}")
    print(f"Characters from index 7 to 12: {text[7:12]}")

    # Omitting indices
    print("\nOmitting indices:")
    print(f"From start to index 6: {text[:6]}")
    print(f"From index 7 to end: {text[7:]}")
    print(f"Entire string: {text[:]}")

    # Using step value [start:end:step]
    print("\nUsing Step Values:")
    print(f"Every second character: {text[::2]}")
    print(f"Every third character: {text[::3]}")

    # Negative step for reverse slicing 
    print("\nReverse Slicing ")
    print(f"Reverse entire string: {text[::-1]}")
    print(f"Reverse slice from index 6 to 0: {text[6::-1]}")


def demonstrate_practical_examples():
    text = "Hello, World!"
    print("\nPractical_Examples:")

    # Extract first word 
    first_word = text[:5]
    print(f"first word: {first_word}")
    # Extract last word
    last_word = text[7:]
    print(f"last word: {last_word}")


    # Reverse string 
    reversed_text = text[::-1]
    print(f"Reversed text: {reversed_text}")

    # Extract every other character
    alternate_chars = text[::2]
    print(f"alternate chars: {alternate_chars}")


if __name__ == "__main__":
    print("Python String Indexing and Slicing Demo\n")
    demonstrate_indexing()
    demonstrate_slicing()
    demonstrate_practical_examples()




#
#
#

