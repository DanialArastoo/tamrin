numbers=[]
for i in range(100,401,1):
    numbers.append(i)

    if i > 1:
        for j in range(2,i):
            if (i%j) == 0:
                # قسمت پایین که کامنت شده رو زمانی بنویس که بخوای اعداد غیر اول هم نشون بده
                # print(i,"nist")
                break
        else:
            print(i,"---aval---")
print(numbers)