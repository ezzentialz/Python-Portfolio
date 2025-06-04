#🧪 ข้อที่ 1: Double It!
#จงใช้ lambda และ map() เพื่อแปลง list ตัวเลขให้เป็น 2 เท่าทุกตัว
#nums = [1, 2, 3, 4, 5]
# Expected result: [2, 4, 6, 8, 10]

nums = [1, 2, 3, 4, 5]
new_num = list(map(lambda x : x * 2, nums))

print(new_num)

#2. filter(function, iterable)
#เอาไว้คัดกรองเฉพาะค่าที่เป็น True
#nums = [1, 2, 3, 4, 5]
#odd = list(filter(lambda x: x % 2 != 0, nums))  # [1, 3, 5]   

nums = [1, 2, 3, 4, 5]
odd = list(filter(lambda x: x %2 !=0, nums))
print(odd)

#3. sorted(iterable, key=function)
#ใช้จัดเรียงตามกฎเฉพาะ
#words = ['apple', 'banana', 'cherry']
#sorted_by_len = sorted(words, key=lambda w: len(w))  # ['apple', 'cherry', 'banana']

words = ['apple', 'banana', 'cherry', 'orange','ant','mango']
sorted_by_len = sorted(words, key=lambda w: len(w) )
print(sorted_by_len)