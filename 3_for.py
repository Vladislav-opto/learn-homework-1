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

def main(result_sales):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    summ_all_products = 0
    qnt_all_products = 0

    for element in result_sales:
      name = element['product']
      qnt_this_product = len(element['items_sold'])
      summ_product = 0
      summ_product = sum(element['items_sold'])
      print(f'Суммарное количество продаж {name} составило {summ_product} шт.')
      if qnt_this_product != 0:
        average_this_product = int(summ_product/qnt_this_product)
        print(f'Среднее количество продаж {name} составило {average_this_product} шт.')
      else:
        print(f'Не было продано ни одного {name}')
      summ_all_products += summ_product
      qnt_all_products += qnt_this_product
    print(f'Суммарное количество продаж всех товаров составило {summ_all_products} шт.')
    if qnt_all_products != 0:
      average_all_products = int(summ_all_products/qnt_all_products)
      print(f'Среднее количество продаж всех товаров составило {average_all_products} шт.')
    else:
      print(f'Не было продано ни одного товара')


if __name__ == "__main__":
    
    sales_history = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
            ]
    
    main(sales_history)
