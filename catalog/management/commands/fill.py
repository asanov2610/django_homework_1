import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_categories_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)



    @staticmethod
    def json_read_products():
        with open('catalog_products_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)


    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'],
                         name=category['fields']['name'],
                         information=category['fields']['information'])
            )




        Category.objects.bulk_create(category_for_create)



        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                        id=product['pk'],
                        name=product['fields']['name'],
                        information=product['fields']['information'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

            Product.objects.bulk_create(product_for_create)
