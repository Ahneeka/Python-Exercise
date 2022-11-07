input_file = open("vowel.txt", "r")
find_word = ''

#for word_line in input_file:
   # for char in word_line:
      #  if char in ['a', 'e', 'i', 'o', 'u']:
            #find_word += char
   # if find_word == 'aeiou':
      #  print(word_line, end='')

   # find_word = ''

    # correction

if __name__ == '__main__':

    def get_vowel_in_word(word):
        """Return vowels in string word--include repeats."""
        vowel_str = "aeiou"
        vowels_in_word = " "
        for char in word:
            if char in vowel_str:
                vowels_in_word += char
        return vowels_in_word
