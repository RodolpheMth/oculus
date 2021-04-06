def money_convert(column):
    money_decimal = []
    for money in column:
        a = str(money).replace('million', '000000').replace('$', '').replace('B', '000000000').replace('M', '000000').replace('m', '000000').replace('billion', '000000000').replace('.', '').replace(" ","").replace("€","")
        if len(a) < 5:
            a = a + '000'
        money_decimal.append(a)
    return money_decimal

