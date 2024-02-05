def replace_chars(input_str, k):    # define function and inputs
    replaced_str = ''   # define replaced_str
    seen_chars = {}     # define seen chars

    for i, char in enumerate(input_str):    # get each number and char of the input string
        if char in seen_chars and i - seen_chars[char] <= k:    #the char is occured in the previous k chars
            replaced_str += '-'     # replaced by '-'
        else:
            replaced_str += char    # or use the original char
        seen_chars[char] = i

    return replaced_str     # return the new string

test_case1 = replace_chars('abcdefaxc ', 10)
print(test_case1)
test_case2 = replace_chars('abcdefaxcqwertba', 10)
print(test_case2)