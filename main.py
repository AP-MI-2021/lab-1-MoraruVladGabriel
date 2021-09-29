'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  '''
  Determina daca un numar este prim.
  :param n: intreg
  :return: True , daca n este prim ; False daca n nu este prim.
  '''

  if n < 2 :
    return False
  else :
    for i in range(2,n//2 +1) :
      if n % i == 0 :
        return False
    return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  '''
  Determina produsul elementelor dintr-o lista.
  :param lst: tablou unidimensional
  :return: produsul elementelor din lista
  '''
  prod = 1
  for i in range(len(lst)):
    prod = prod * lst[i]

  return prod
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
