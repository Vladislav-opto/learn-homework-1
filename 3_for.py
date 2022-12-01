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

def print_result(preamble, name_to_print, result_to_print):
    print(f'{preamble} количество продаж {name_to_print} составило {result_to_print} шт.')


def sale_of_goods(result_sales):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    summ_all_products = 0
    qnt_all_products = 0

    for element in result_sales:
        name = element['product']
        qnt_this_product = len(element['items_sold'])
        summ_product = sum(element['items_sold'])
        print_result('Суммарное', name, summ_product)
        if qnt_this_product != 0:
            average_this_product = summ_product // qnt_this_product
            print_result('Среднее', name, average_this_product)
        else:
            print_result('Общее', name, 0)
        summ_all_products += summ_product
        qnt_all_products += qnt_this_product
    print_result('Суммарное', 'всех товаров', summ_all_products)
    if qnt_all_products != 0:
        average_all_products = int(summ_all_products/qnt_all_products)
        print_result('Среднее', 'всех товаров', average_all_products)
    else:
        print_result('Общее', 'всех товаров', 0)


if __name__ == "__main__":
    sales_history = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
        ]
    sale_of_goods(sales_history)