import random;
import math;
from collections import Counter;
from datetime import datetime;

lista = [1, 2, 3, 4, 5, 6, 7];
lista2 = ['Fede', 'Melina', 'Sofia', 'Julian','Fede','Fede','Fede','Sofia']

#print(random.randint(1,6));
#print(random.choice(lista2));


#print(math.pi);
#print(math.e);

#print(math.floor(15.373737)) #Redondea para abajo
#print(math.ceil(15.373737))#Redondea para arriba
#print(math.trunc(15.373737))

a = Counter(lista2);
#print(a.most_common());

dt = datetime.now();
'''print(dt.year);
print(dt.month);
print(dt.day);
print(dt.minute);
print(dt.second);
print(dt.microsecond);'''

date = datetime(2022,10,19,23,20,35);
print(date);