#def reverse_text(text):
#    return ''.join((reversed(text)))

#text = input(f"please enter your name: ")
#print(f" your name is {text}, and your reversed name is {reverse_text(text)}")


'''
เขียนฟังก์ชันชื่อ reverse_message(msg)
รับข้อความจากผู้ใช้ แล้วคืนค่า “ข้อความกลับด้าน”

เช่น: "Python" → "nohtyP"
'''

#def reverse_message(msg):
#    return ''.join(reversed(msg))

#msg = input(f"please enter message: ")
#print(f"your message: {msg} has been reversed to {reverse_message(msg)}")



'''
ให้ list แบบนี้:
numbers = [1, 2, 3, 4, 5]
ใช้ reversed() แสดงผลแบบย้อนกลับ → [5, 4, 3, 2, 1]

อย่าลืมใช้ list() ครอบ reversed() ด้วยน้า
'''
#numbers = [1, 2, 3, 4, 5]
#print(f"there is list number [1,2,3,4,5], the reversed number is {list(reversed(numbers))} ")

'''
✅ ข้อที่ 3: กลับคำในประโยค
รับข้อความจากผู้ใช้ เช่น

"i love python"
แล้วใช้ split() + reversed()

ให้แสดงผลกลับคำเป็น:
"python love i"
'''

#msg = ['i', 'love', 'python']
#print(f"the is msg of ['i', 'love', 'python'], the reverse is: {' '.join(reversed(msg))}")



'''
def play_reverse_game():
    words = ["banana", "python", "reverse", "hello", "chat"]
    score = 0

    print("🎮 ยินดีต้อนรับสู่เกม 'ถอดรหัสกลับด้าน!'")
    print("ทายคำจากคำที่ถูกกลับด้านนะจ๊ะ 😁")

    for word in words:
        reversed_word = ''.join(reversed(word))
        print(f"\n🔄 คำกลับด้าน: {reversed_word}")
        guess = input("✨ ทายคำจริง: ").strip().lower()

        if guess == word:
            print("✅ ถูกต้อง! เก่งมากกกก!")
            score += 1
        else:
            print(f"❌ ผิดจ้า คำที่ถูกต้องคือ: {word}")

    print(f"\n🎉 จบเกมแล้ว! คุณได้ {score} คะแนน จากทั้งหมด {len(words)} คำ")

play_reverse_game()
'''

def reverse_game():
    words = ['anaconda', 'apocallypse', 'amagedon', 'faith', 'love']
    score = 0
    
    
    for word in words:
        reverse_word = ''.join(reversed(word))
        print(f"what is this reversed word?: {reverse_word}")
        guess = input(f"what is the word: ").strip().lower()
        
        if guess == word:
            print(f"correct")
            score += 1
        else:
            print(f"wrong! the correct is {word}")
            
    print(f"Game over, your score is {score} / {len(words)}")

reverse_game()