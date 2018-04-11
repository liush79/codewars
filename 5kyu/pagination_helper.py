def deco(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return -1
    return wrapper


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.len_collection = len(self.collection)
    def item_count(self):
        return self.len_collection
    def page_count(self):
        return self.len_collection / self.items_per_page + 1
    @deco
    def page_item_count(self, page_index):
        page = self.len_collection / self.items_per_page
        if self.len_collection / self.items_per_page > page_index:
            return self.items_per_page
        elif self.len_collection / self.items_per_page == page_index:
            return self.len_collection - (page * self.items_per_page)
        else:
            return -1
    @deco
    def page_index(self, item_index):
        if item_index >= self.len_collection:
            return -1
        return item_index / self.items_per_page if item_index >= 0 else -1

collection = range(1,25)
helper = PaginationHelper(collection, 10)

print helper.page_count()       # 3
print helper.page_index(23)     # 2
print helper.item_count()       # 24
