apple_price = input('ねぇ、このりんごいくらなの？')
count = input('ふーん...で、いくつ買うの？')

total_price = int(apple_price) * int(count)


print('合計' + str(total_price) +'円ね') 

if total_price > 10000:
    print('ちょっと高すぎない？')
else:
    print('いい買い物したわね!')
