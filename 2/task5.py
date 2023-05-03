def unique_words(s):
    response = []
    lst = s.split(' ')  # Спилит по умолчанию использует пробел lst = s.split()

    for i in lst:
        if i not in response:
            if i[-1] == ',' or i[-1] == '.' or i[-1] == '?': # Хорошо, что проверяете именно последний символ, так вы не удалите из центра слова, но пропустите троеточие ...
                i = i[:-1]
            response.append(i)
    return response

assert unique_words("hello world") == ["hello", "world"]
assert unique_words("apple apple banana cherry") == ["apple", "banana", "cherry"]
assert unique_words("Python is great, isn't it?") == ["Python", "is", "great", "isn't", "it"]
