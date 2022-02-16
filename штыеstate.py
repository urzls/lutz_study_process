class InstState: # Дескриптор использует атрибут экземпляра
def __get__(self, instance, owner):
print(‘InstState get’) # Предполагает наличие атрибута
return instance._Y * 100 # в клиентском классе
def __set__(self, instance, value):
print(‘InstState set’)
instance._Y = value