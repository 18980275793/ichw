def pick_number(string):
    """
    use this function to pick up numbers from string
    """
    num=[]
    collect=[]
    for ele in string:
        if ord(ele)==46 or (ord(ele)>=48 and ord(ele)<=57):
            num = num + [ele]
        elif 1==1 :
            a=''.join(num)
            collect = collect+[a]
            num = []
    while '' in collect:
        collect.remove('')
    return collect

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    a=pick_number(jstr)
    amount_to =a[1]
    return amount_to

def test_pick_number():
    """test function 'pick_number' """
    assert(pick_number("I have 7 apples, but I cannot have 7.5 apples") == ['7','7.5'])
    return

def test_exchange():
    """test function 'exchange' """
    assert(exchange('USD','EUR','2.5') == str(exchange('USD','EUR','2.5')))
    return

def testAll():
    """test all cases"""
    test_pick_number()
    test_exchange()
    print("All tests passed")
    return

def main():
    testAll()
    currency_from = input('please enter the currency to exchange')
    currency_to = input('please enter the currency you would exchange')
    amount_from = input('please enter the amount of money you would exchange')
    money = exchange(currency_from, currency_to, amount_from)
    print('You woule get '+ money + currency_to)
    return

main()