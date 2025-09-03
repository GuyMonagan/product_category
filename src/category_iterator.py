class CategoryIterator:
    """Считает товары по категориям"""

    def __init__(self, category):
        self._products = category.products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            result = self._products[self._index]
            self._index += 1
            return result
        raise StopIteration
