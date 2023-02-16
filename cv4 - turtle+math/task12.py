def test_prvocis(a):
    for i in range(a):
        i = i+1
        if a%i == 0:
            return False
        else:
            return True

a = test_prvocis(1)
print(a)