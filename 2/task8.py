def filter_capitalized_words(lst):
    response = []
    for i in lst:
        if not i.islower():
            response.append(i)
    return response

assert filter_capitalized_words(["Apple", "Banana", "cherry"]) == ["Apple", "Banana"]
assert filter_capitalized_words(["Python", "java", "C++"]) == ["Python", "C++"]
assert filter_capitalized_words(["Red", "green", "Blue"]) == ["Red", "Blue"]
