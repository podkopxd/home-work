print('hi')

x = 38

print('дратути')
if x < 0:
    print('Меньше ноля')
print('дотвидания')

#
a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a < 0:
    print('success1')

if a > b and (a > 0 or b < 6743822497384):
    print('success2')

if 5 < b and b < 10:
    print('success3')

#
if '34' > '123':
    print('success11')

if '123' > '12':
    print('success22')

if [1, 2] > [1, 1]:
    print('success33')

# that can't be equaled, cause of dif types
if '6' > 5:
    print('success111')

if [4, 5] > 5:
    print('success222')

# but
if '6' != 5:
    print('success1111')

print('bb')