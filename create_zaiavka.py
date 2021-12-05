"""модуль призначенно для формування заявки,
 що формується з файлів 'prices' i 'groups'
"""

from data_service import get_price, get_group



TITLE = "Аналіз середніх ринкових цін на основі продуктів споживчого кошика"
HEADER = \
"""
======================================================================================================================================
 Найменування товарної групи :   Рік :         Товарообіг :                   Торгова скидка :            Валовий доход :
======================================================================================================================================                                       
                                        План :   Очіковане виконання :                              План :  Очіковане виконання :
======================================================================================================================================                                                     
""" 

prices = get_price()
groups = get_group()


def find_price_name(price_code):
    """шукає в довіднику назву товару по його коду"""

    for price in prices:
        if price_code == price[0]:
           return price[1]

    return "нема назви"


def str_to_num(str_num):
    """повертає строкове число в число"""
    if str_num.isnumeric():
        return float(str_num)
    else:
        return float(str_num[:-1])
    
      

 
def show_income(incum):

    print(TITLE)
    print(HEADER)
    for row in incum:
        print(f"{row['group name']:5}",
        f"{row['year']:20}",
        f"{row['plan']:20}",
        f"{row['expected']:15}",
        f"{row['discount']:15}",
        f"{row['income plan']:15}",
        f"{row['income expected']:10.2f}")
         

    
income = {
    'group name'              : "",     # найменування товарної групи   (groups)
    'year'           : 0,     # рік      (prices)
    'plan'             : 0.0,     # план                    (prices)
    'expected'  : 0.0,    #  очіковане виконання        (prices)
    'discount'    : 0.0,    # торгова скидка           (groups)
    'income plan'   : 0.0,    # валовий дохід план            (plan / 100 * discount)
    'income expected'  : 0.0     # валовий дохід очіковане виконання           (expected / 100 * discount)
}

 

incomes = []
for group in groups:
    income['group name']= group[0]
    income['discount'] = group[2]
     
for price in prices:
    income['year'] = price[3]
    income['plan'] = price[1]
    income['expected'] = price[2]
    
    incomes.append(income) 
    
for item in incomes:
    income['income plan'] = str_to_num(price[1]) / 100 * str_to_num(group[2])
    income['income expected'] = str_to_num(price[2]) / 100 * str_to_num(group[2])
 
pass
