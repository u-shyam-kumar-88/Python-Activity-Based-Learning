# Case Study 8: Text Compression Using Character Runs

texts = ["aaabbbcccd", "abcd", "aaaaaaaaaa", "wwwwbbbwwwwww", ""]

for text in texts:
    if len(text) == 0:
        print("'' -> Empty string, nothing to encode")
        continue

    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1
        else:
            encoded = encoded + text[i - 1] + str(count)
            count = 1
    encoded = encoded + text[-1] + str(count)  # last run

    if len(encoded) < len(text):
        verdict = "Encoding is beneficial"
    elif len(encoded) == len(text):
        verdict = "Same length"
    else:
        verdict = "Encoding NOT beneficial"

    print(f"{text} ({len(text)}) -> {encoded} ({len(encoded)}) : {verdict}")
