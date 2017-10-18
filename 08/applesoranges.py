def apples(a, m_distance, s, t):
    count_apple = 0
    for i in range(len(m_distance)):
        sum_apple = a + m_distance[i]
        if s <= sum_apple <= t:
            count_apple += 1
    return count_apple
def oranges(b, n_distances, s, t):
    count_oranges = 0
    for i in range(len(n_distance)):
        sum_oranges = b + n_distance[i]
        if s <= sum_oranges <= t:
            count_oranges += 1
    return count_oranges

s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
m_distance = [-2, 2, 1]
n_distance = [-4, 8]

print (apples(a, m_distance, s, t))
print (oranges(b, n_distance, s, t))