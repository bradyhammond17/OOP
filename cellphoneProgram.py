import cellphoneClass as c

def main():
    #get phone data

    man = 'Apple'
    mod= 'iPhone 13'
    retail = 899

    #create instance of Phone class
    phone = c.Phone(man, mod, retail)

    print(phone.get_manufact)
    print(phone.get_model)
    print(phone.get_retail_price)

main()