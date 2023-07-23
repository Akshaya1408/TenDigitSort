def tens_digit(num):
    num //= 10
    return num % 10

def tens_digit_sort(array):
    array.sort(key=lambda x: (tens_digit(x), -x))
    return array

array=list(map(int,input().split()))
print(tens_digit_sort(array))