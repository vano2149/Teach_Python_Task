"""
Страница 599. Глава 20 Включения и генераторы.
"""

def two_oldest_ages(ages):
    """
    """
    l = []
    l.append(max(ages))
    ages.remove(max(ages))
    l.append(max(ages))
    l.reverse()
    return l



a = [1, 5, 87, 45, 8, 8]

two_oldest_ages(a)