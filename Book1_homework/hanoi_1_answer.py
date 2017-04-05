# Hanoi part 1 - Answer

m_list_a = list(range(20))
m_list_b = []

def move(list_a, list_b, n):
    if n <= 0:
        return
    list_b.append( list_a[n-1] )
    del list_a[n-1]
    move(list_a, list_b, n-1)

move( m_list_a, m_list_b, len(m_list_a) )
print(m_list_a, m_list_b, sep='\n')
