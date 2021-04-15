text = ["The", "fox", "jumped", "over", "the", "fence", "."]


def method(text):
    result = ""
    for i in text:
        result = result+" " + i

    return result


print(method(text))
