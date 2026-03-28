def detect_roast(beans: str):
    splitup = list(beans)
    total = 0
    for i in splitup:
        if i == "'":
            total += 1
        if i == "-":
            total += 2
        if i == ".":
            total += 3

    beanAvg = total / len(beans)
    match beanAvg:
        case beanAvg if beanAvg < 1.75:
            return "Light"
        case beanAvg if beanAvg >= 1.75 and beanAvg <= 2.5:
            return "Medium"
        case beanAvg if beanAvg > 2.5:
            return "Dark"


assert detect_roast("''-''''''-'-''--''''") == "Light"
assert detect_roast(".'-''-''..'''.-.-''-") == "Medium"
assert detect_roast("--.''--'-''.--..-.--") == "Medium"
assert detect_roast("-...'-......-..-...-") == "Dark"
assert detect_roast(".--.-..-......----.'") == "Medium"
assert detect_roast("..-..-..-..-....-.-.") == "Dark"
assert detect_roast("-'-''''''..-'.''-'.'") == "Light"
