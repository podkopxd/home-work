immutable_var = ([1, 2, 3], True, 4, 5, 'text')
print(immutable_var)
  #immutable_var[1] = False  Данное действе не ссработает, потому что кортеж нельзя изменить
mutable_list = [4, 5, 4, 4]
mutable_list[1] = 4
print(mutable_list)