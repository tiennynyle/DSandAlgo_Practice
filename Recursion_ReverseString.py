def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        last_char = s[len(s) - 1] #e
        current_s = s[0:len(s) - 1] # abcd
        tmp = reverse_string(current_s) #reverse_string(abcd)
        tmp = last_char + tmp
        return tmp
print(reverse_string("abcde"))
