"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров

"""

def print_result(result_to_print):
    for good in result_to_print:
        if 'product' in good:
            name = good['product']
            average = good['average']
            summ = good['summ']
            print(f'Суммарное количество продаж {name} составило {summ} шт.')
            print(f'Среднее количество продаж {name} составило {average} шт.')
        elif 'average_all' in good:     
            average_all = good['average_all']
            print(f'Среднее количество проданных товаров составило {average_all} шт.')
        elif 'summ_all' in good:
            summ_all = good['summ_all']
            print(f'Суммарное количество проданных товаров составило {summ_all} шт.')


def sale_of_goods(result_sales):
    summ_all_products = 0
    qnt_all_products = 0
    list_result = []
    for element in result_sales:
        qnt_this_product = len(element['items_sold'])
        summ_product = sum(element['items_sold'])
        if qnt_this_product != 0:
            element['summ'] = summ_product
            average_this_product = summ_product // qnt_this_product
            element['average'] = average_this_product
        else:
            element['summ'] = 0
        summ_all_products += summ_product
        qnt_all_products += qnt_this_product
        list_result.append(element)
    if qnt_all_products != 0:
        list_result.append({'summ_all': summ_all_products})
        average_all_products = int(summ_all_products/qnt_all_products)
        list_result.append({'average_all': average_all_products})
    else:
        list_result.append({'summ_all': 0})
    return list_result


if __name__ == "__main__":
    sales_history = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
        ]
    result_sale_of_goods = sale_of_goods(sales_history)
    print_result(result_sale_of_goods)