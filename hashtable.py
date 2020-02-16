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

    def seek_slot(self, value): # находит индекс пустого слота для значения, либо None
        if None in self.slots:
            i = self.hash_fun(value)
            step = self.step

            while True:
                try:
                    if self.slots[i] is None:
                        return i
                    else:
                        i += step
                except IndexError:
                    i = 0
                    step //= 2
        else:
            return None

    def put(self, value):
        valueIndex = self.hash_fun(value)

        if self.slots[valueIndex] is None:
            self.slots[valueIndex] = value # записываем значение по хэш-функции
            return valueIndex
        elif None in self.slots:
            idexSeekSlot = self.seek_slot(valueIndex)
            self.slots[idexSeekSlot] = value 
            return idexSeekSlot # возвращается индекс слота
        else:
            return None

    def find(self, value): # находит индекс слота со значением, или None
        try:
            return self.slots.index(value)
        except ValueError:
            return None
