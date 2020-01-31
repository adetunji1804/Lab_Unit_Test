# Write a program that turns a sentence into camel case. The first word is lowercase,
# the rest of the words have their initial letter capitalized, and all of the words are joined together.

def camelCase(sentence):
    try: # t to test the special character found in user input
        #list of special / invalid characters
        invalid_char = ['/', '\\', '<', '>', '}', '{', '[', ']', '|', '?', '%', '@', '&', '!','.']
        for each_invalid_char in invalid_char: #iterate through the list of invalid charaters
            for i in range(len(sentence)): # repeat operation through the number length of sentence
                if each_invalid_char in sentence: #check if special char exist in input sentence
                    raise ValueError # raise error if special char found
                break # break out of program
        # convert the first character in each word to Uppercase
        firstLetUp = sentence.title()

                    # putting space between words
        camelCaseUp = firstLetUp.replace(' ', '')
        
                    # return sentence with space between word
                    # and first sentence word in lower case then other in capital
        return camelCaseUp[0:1].lower() + camelCaseUp[1:]
    except ValueError: # handle error raised
        return f"invalid character included" #return error message
    

def main():
    # user input
    sentence = input('Enter your sentence: ')

    # calling method camelCase
    camelCased = camelCase(sentence)
    # Output
    print(camelCased)

if __name__ == "__main__":
    main()