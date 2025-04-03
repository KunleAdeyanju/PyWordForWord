import re
import os

class file_analyzer():
    
    def __init__(self):
       pass


    def func_print(self, file_name):
        f = open(file_name)
        file_list = f.readlines()
        return ("".join(file_list))

    def wc(self, word):
        # f = open(file_name)
        # file_list = f.readlines()
        
        str = "".join(word)
        split_words = re.sub(r'[^a-zA-Z0-9]', ' ', word)
        split_words = split_words.split()
        

        char_count = len(str)
        word_count = len(split_words)

        new_line = 0
        for i in word:
            if i == '\n':
                new_line += 1

        line_count = new_line

        results = (f"Character count: {char_count}", f"Word count: {word_count}", f"Line count: {line_count}")
        #results = (char_count, word_count, line_count)
        return (results)

    def wordFrequency(self, word):
        split_words = re.sub(r'[^a-zA-Z0-9]', ' ', word)
        split_words = split_words.lower().split()
        ans = {

        }
        for i in split_words:
            if i in ans:
                ans[i]+= 1
            else:
                ans[i] = 1
        
        return ans

    def letterFrequency(self, word):
        word_without = re.sub(r'[^a-zA-Z0-9]', '', word) # forgot to remove the spaces
        split_chars = list(word_without.lower())
        ans = {}
        for i in split_chars:
            if i in ans:
                ans[i]+=1
            else:
                ans[i] = 1
        return ans

    def numberOfOccurences(self, sentences, word_to_check):
        word_counter = 0
        words = re.sub(r'[^a-zA-Z0-9]', ' ', sentences)
        words = words.lower().split()
        for i in words:
            if i == word_to_check:
                word_counter += 1
        return int (word_counter)
    
    def totalNumberOfWords(self, words_input):
        words = re.sub(r'[^a-zA-Z0-9]', ' ', words_input)
        words_input_list = words.lower().split()
    
        
        return int (len(words_input_list))
    
    def frequency(self, sentences, word):
        return self.numberOfOccurences(sentences, word) / self.totalNumberOfWords(sentences)
        


# fun = file_analyzer()

# funs = fun.func_print("/Users/kunle/Python Projects/PyWordForWord/testdata/blue.txt")

# print(fun.wc(funs))
# b = "blue"
# print(f"The frequency of '{b}' is {fun.frequency(funs,b)}")

folder_path = "/Users/kunle/Python Projects/PyWordForWord/testdata"

with open('Fundamentals.txt', 'w') as txt_files:
    for file in os.listdir(folder_path):
        full_file_path = "%s/%s" % (folder_path, file)
        fun = file_analyzer()
        funs = fun.func_print(full_file_path)
        txt_files.write(file + "\n")
        txt_files.write(str(fun.wc(funs)) + "\n")
        txt_files.write(str(fun.wordFrequency(funs)) + "\n")
        txt_files.write(str(fun.letterFrequency(funs)) + "\n")
        txt_files.write("\n\n\n")
        


