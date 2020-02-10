class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

     def hash_fun(self, value):
         p = 0.33
         summ = 0
         for i in value:
             summ += ord(i) * p
         return int(summ % self.size)

     def seek_slot(self, value):
         # находит индекс пустого слота для значения, или None
         return None

     def put(self, value):
         # записываем значение по хэш-функции

         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить
         return None

     def find(self, value):
         # находит индекс слота со значением, или None
         return None
'''
    def seek_slot(self, value):
        None in self.slots:
            index = hash_fun(value)
            while
            if self.slots[index] == None:
                return index
        else:
            # находит индекс пустого слота для значения, или None
            return None
'''