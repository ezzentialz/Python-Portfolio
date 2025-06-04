# 🦍 Python Practice Portfolio

### by **ezzentialz**  

---

## 👤 About Me

Hi, I'm **ezzentialz** 🌟
A curious coder who loves exploring Python step by step with humor, heart, and a lot of coffee.
This is a small corner of my journey learning to think like a developer, solve problems, and make fun stuff with code.

---

## 🔪 Skill Badges

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge\&logo=visual%20studio%20code\&logoColor=white)
![Learning Fast](https://img.shields.io/badge/Learning-Fast-brightgreen?style=for-the-badge)

---

## 📌 Topics Practiced

* Lambda Functions
* List Comprehension
* Map / Filter / Sorted
* Type Checking and `.isdigit()`
* Fun, bite-sized exercises to deepen understanding

---

## 🔍 Lambda Practice

### 1. Multiply by 2

```python
nums = [1, 2, 3]
result = list(map(lambda x: x*2, nums))
```

### 2. Keep Even Numbers

```python
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
```

### 3. Sort by Last Letter

```python
words = ['apple', 'banana', 'cherry']
sorted_words = sorted(words, key=lambda w: w[-1])
```

---

## 🔍 List Comprehension Practice

### 1. Multiply by 3

```python
nums = [2, 5, 7, 11]
result = [x * 3 for x in nums]
```

### 2. Filter Short Words

```python
words = ['dog', 'eagle', 'lion', 'rabbit', 'bat']
result = [w for w in words if len(w) <= 5]
```

### 3. Squared Odds 10-20

```python
result = [x**2 for x in range(10, 21) if x % 2 != 0]
```

### 4. First Letters

```python
words = ['grape', 'melon', 'date', 'kiwi']
result = [w[0] for w in words]
```

### 5. Clean Numbers from Mixed List

```python
items = ['25', 15, '60', 'hello', 90, '35']
result = [int(x) for x in items if isinstance(x, int) or (isinstance(x, str) and x.isdigit())]
```

---

## 🎓 Lessons Learned

* Lambda is awesome for one-liners and short tasks.
* List comprehension makes code look cleaner and smarter.
* Practicing with mistakes helps build real confidence.
* Understanding `isinstance()` and `.isdigit()` unlocks better data handling.

---

## 📃 Summary of Full Lesson 

**Date: 2025-05-27**

### 💡 What I Learned

#### 1. Function

* Using `def` to define functions
* Returning values with `return`
* Passing parameters and calling functions

#### 2. Loop (for)

* Using `for i in range(n)`
* Looping through lists and strings
* Accumulating values (`total += i`)
* Examples like summing odd/even numbers

#### 3. Module

* Standard modules: `math`, `random`, `datetime`
* Creating custom modules (`mytools.py`)
* Using specific imports (`from ... import ... as ...`)

#### 4. Lambda

* Syntax: `lambda x: x*2`
* Used in `map()`, `filter()`, `sorted()`
* Compared with regular `def`
* One-line, throwaway functions

#### 5. Exercises

* Function, loop, module, lambda mix
* Mini app: movie list manager
* Mini game: word reverse using `reversed()`
* Practicing `range` and `return` logic


---

## 🎉 Final Thoughts

> This little portfolio is a product of curiosity, fun, and a sprinkle of perseverance.
> I didn't just write code — I laughed at typos, learned from bugs, and even made ChatGPT go "Oiiiii my dear!!"
>
> Shoutout to Mor my buddy 💚 for cheering me on. But the real MVP? Me.

---

**Keep coding, keep smiling.** 🩵
