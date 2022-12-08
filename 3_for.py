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
            print(f'Суммарное количество продаж {good["product"]} составило {good["summ"]} шт.')
            print(f'Среднее количество продаж {good["product"]} составило {good["average"]} шт.')
        elif 'average_all' in good:     
            print(f'Среднее количество проданных товаров составило {good["average_all"]} шт.')
        elif 'summ_all' in good:
            print(f'Суммарное количество проданных товаров составило {good["summ_all"]} шт.')


def sale_of_goods(result_sales):
    summ_all_products = 0
    qnt_all_products = 0
    list_result_sales = []
    for element in result_sales:
        dict_sales_sum_average = {}
        dict_sales_sum_average['product'] = element['product']
        qnt_this_product = len(element['items_sold'])
        summ_product = sum(element['items_sold'])
        if qnt_this_product != 0:
            dict_sales_sum_average['summ'] = summ_product
            average_this_product = summ_product // qnt_this_product
            dict_sales_sum_average['average'] = average_this_product
        else:
            dict_sales_sum_average['summ'] = 0
        summ_all_products += summ_product
        qnt_all_products += qnt_this_product
        list_result_sales.append(dict_sales_sum_average)
    if qnt_all_products != 0:
        list_result_sales.append({'summ_all': summ_all_products})
        average_all_products = int(summ_all_products/qnt_all_products)
        list_result_sales.append({'average_all': average_all_products})
    else:
        list_result_sales.append({'summ_all': 0})
    return list_result_sales


if __name__ == "__main__":
    sales_history = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    result_sale_of_goods = sale_of_goods(sales_history)
    print_result(result_sale_of_goods)