def encode(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += (str(count) if count > 1 else "") + s[i - 1]
            count = 1

    if s:
        result += (str(count) if count > 1 else "") + s[-1]

    return result

def decode(s):
    result = ""
    count = ""

    for char in s:
        if char.isdigit():
            count += char
        else:
            result += char * (int(count) if count else 1)
            count = ""

    return result