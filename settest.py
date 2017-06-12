from sets import Set

def test():
    my_set = Set()
    
    print('If 1 is in the empty set:', my_set.Contains(1))
    
    print('Adding 1 to set...')
    my_set.Add(1)
    print('Size of set:', my_set.Size())
    
    print('Adding 2 to set...')
    my_set.Add(2)
    print('Size of set:', my_set.Size())
    
    print('If 1 is in the set now:', my_set.Contains(1))
    
    print('Removing 1 from the set...')
    my_set.Remove(1)
    print('Size of set:', my_set.Size())
    
    print('If 1 is in the set now:', my_set.Contains(1))
    print('If 2 is in the set now:', my_set.Contains(2))
    
    
    my_set_2 = Set()
    print('Building another set with 1, 2, 3, 4 in it...')
    my_set_2.Add(1)
    my_set_2.Add(2)
    my_set_2.Add(3)
    my_set_2.Add(4)
    
    print('my_set:', my_set.elements)
    print('my_set_2:', my_set_2.elements)
    
    print('my_set | my_set_2:', (my_set | my_set_2).elements)
    
    print('my_set & my_set_2:', (my_set & my_set_2).elements)
    
    print('my_set - my_set_2:', (my_set - my_set_2).elements)
    
    print('my_set_2 - my_set:', (my_set_2 - my_set).elements)
    
if __name__ == '__main__':
    test()