def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9 :
        return list(get_characters(num)) # e.g.: num = 2 -> returns ['a', 'b', 'c']
        
    
    last_digit = num % 10 # num = 234 -> last_digit = 4
    # Recursive call
    small_output = keypad(num//10) # returns list of strings
    keypad_string = get_characters(last_digit) # returns a string

    result = list()
    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for char in keypad_string:
        for item in small_output:
            new_item = item + char
            result.append(new_item)
    return result

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")
# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)
# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)
# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)
# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)
input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)

    
