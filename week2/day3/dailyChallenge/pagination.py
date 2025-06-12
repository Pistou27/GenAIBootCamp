import math
class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_index = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start = self.current_index * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            print("Pas de page présente")
        self.current_index = page_num -1

    def first_page(self):
        self.current_index = 0
        return self
    
    def last_page(self):
        self.current_index = self.total_pages - 1
        return self
    
    def next_page(self):
        if self.current_index < self.total_pages - 1:
            self.current_index += 1
        return self 
    
    def previous_page(self):
        if self.current_index > 0:
            self.current_index -= 1
        return self
    
    def __str__(self):
        return '\n'.join(self.get_visible_items())



alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p)

p.go_to_page(0)
# # # Raises ValueError

print(p.get_visible_items())
# # ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# # # ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# # # ['y', 'z']

p.go_to_page(7)
print(p.current_index + 1)
# # # Output: 7

