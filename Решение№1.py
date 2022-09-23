x2 = open('input.txt', 'r')
x = x2.read(5 * 10 ** 7)
n1 = 0
n2 = 0
x1 = [i for i in x]
count1 = 0
count2 = 0
if (x1.count("}") + x1.count("{")) % 2 == 0 or abs(x1.count("}") - x1.count("{")) > 1:
    print(-1)
elif x1.count("}") != x1.count("{"):
    for i in range(len(x1)):
        if x1[i] == "{":
            count1 += i
            n1 += 1
    for i in range(len(x1)):
        if x1[i] == "}":
            count2 += i
            n2 += 1
    if count2 / n2 < count1 / n1:
        print(-1)


    elif x1.count("}") > x1.count("{"):
        if x1.index('}') < x1.index('{'):
            for i in range(len(x1)):
                if x1[i] == "}":
                    s = i
                    break
        else:
            s = len(x1) - x1[::-1].index('}') - 1
        print(s + 1)
    elif x1.count("}") < x1.count("{"):
        if x1[::-1].index('{') > x1[::-1].index('}'):
            for i in range(len(x1)):
                if x1[i] == "{":
                    s = i
                    break
        else:
            s = len(x1) - x1[::-1].index('{') - 1
        print(s + 1)