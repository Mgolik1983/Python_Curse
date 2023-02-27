#class Rectangle:
 #   def __int__(self,x1 ,y1, x2, y2):
#      self.width = abs(x1-x2)
#        self.height = abs(y1-y2)
#    def perimeter(self):
#        return (self.width+self.height) * 2
#    def area(self):
#        return self.width * self.height

class Category:
    categoryes = []

    @classmethod
    def add(cls, value):
        if value.title() not in cls.categoryes:
            cls.categoryes.append(value.title())
            return len(cls.categoryes) - 1
        else:
            raise ValueError('Category is not unique')
    @classmethod
    def get(cls,idex):
        return cls.categoryes[idex]
    @classmethod
    def delete(cls, index):
        if cls.categoryes[index] in cls.categoryes:
            cls.categoryes.pop(index)
        else:
            None
    @classmethod
    def update(cls, index, value):
        if index in range(len(cls.categoryes)):
            if value.title() not in cls.categoryes:
                cls.categoryes[index] = value.title()
            else:
                return cls.add(value)



