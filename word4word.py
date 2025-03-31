
def func_print(file_name):
    f = open(file_name)
    file_list = f.readlines()
    return ("".join(file_list))

def wc(file_name):
    f = open(file_name)
    file_list = f.readlines()
    
    str = "".join(file_list)
    
    split_words = str.split()
    

    char_count = len(str)
    word_count = len(split_words)
    line_count = len(file_list)
    results = (f"Character count: {char_count}", f"Word count: {word_count}", f"Line count: {line_count}")
    return (results)

def wordFrequency(word):
    split_words = word.split()
    ans = {

    }
    for i in split_words:
        if i in ans:
            ans[i]+= 1
        else:
            ans[i] = 1
    
    return ans


n = "/Users/kunle/Python Projects/PyWordForWord/testdata/testdata1.txt"
print(func_print(n))
print(wc(n))
print(wordFrequency("this this fun"))