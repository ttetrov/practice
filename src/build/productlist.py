from swagger_server.models.models_products_list import ModelsProductsList


class ProductListBuilder:

    def __init__(self):
        self.product_list = ModelsProductsList()

    def set_has_more(self, has_more):
        self.product_list.has_more = has_more
        return self

    def set_page(self, page):
        self.product_list.page = page
        return self

    def set_products(self, products):
        self.product_list.products = products
        return self

    def set_size(self, size):
        self.product_list.size = size
        return self

    def set_total_count(self, total_count):
        self.product_list.total_count = total_count
        return self

    def set_total_pages(self, total_pages):
        self.product_list.total_pages = total_pages
        return self

    def get_product_list(self):
        return self.product_list