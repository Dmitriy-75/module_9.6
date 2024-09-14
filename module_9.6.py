def all_variants(text):
    len_t = len(text)
    k = 1
    while k <= len_t:
        i = 0
        while i + k <= len_t:
            yield text[i:i + k]
            i += 1
        k += 1


a = all_variants("Россия")
for i in a:
    print(i)



