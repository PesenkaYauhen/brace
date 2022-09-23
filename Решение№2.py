x2 = open('input.txt', 'r')
x = x2.read(5 * 10**7)

#x = "a{b {}}+ c} = ab + bc"

x1 = [i for i in x]
s = 0
if (x1.count("}") + x1.count("{")) % 2 == 0 or abs(x1.count("}") - x1.count("{")) > 1:
    print(-1)
else:
    if x1.count("}") > x1.count("{"):
        for i in range(len(x1)):
            if x1[i] == "}":
              s = i
              break
    elif x1.count("}") < x1.count("{"):
        for i in range(len(x1)):
            if x1[i] == "{":
              s = i
              break
    print(s+1)