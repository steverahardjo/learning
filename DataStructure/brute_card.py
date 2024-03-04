card_lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
lst = []
operators = ["+", "-", "*", "/"]

def generate_expressions(nums, ops):
    None

def count(words):
    if not words:
        return 0
    
    num = int(words[0])
    n = 1
    l = len(words) - 1

    while n <= l:
        if words[n] == "+":
            num += int(words[n+1])
            n += 2
        elif words[n] == "-":
            num -= int(words[n+1])
            n += 2
        elif words[n] == "*":
            num *= int(words[n+1])
            n += 2
        elif words[n] == "/":
            num /= int(words[n+1])
            n += 2

    return num == 24

def evaluate_expression(expression_list):
    results = []
    for expression in expression_list:
        stack = []
        for q in expression.split():
            if q[0] in operators:
                q = q[1:]
            elif q[-1] in operators:
                q = q[:-1]
            stack.append(q)
        results.append(count(stack))
    return results

# Your input code remains unchanged
for _ in range(4):
    card_form = input("What card do you want? ")
    if card_form not in card_lst:
        print("Card is not acceptable")
    if card_form == "Jack":
        lst.append(11)
    elif card_form == "Queen":
        lst.append(12)
    elif card_form == "King":
        lst.append(13)
    else:
        lst.append(int(card_form))

expressions = generate_expressions(lst, operators, "")
results = evaluate_expression(expressions)

for i in range(len(results)):
    if results[i]:
        print(f"The expression {expressions[i]} equals 24.")
    else:
        print(f"The expression {expressions[i]} does not equal 24.")




                    
                    
