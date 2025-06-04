words = {
    "apple": "แอปเปิ้ล",
    "banana": "กล้วย",
    "dog": "หมา",
    "car": "รถ",
    "book": "หนังสือ"
}

print("🎮 ยินดีต้อนรับสู่เกมทายคำ!")
print("เดี๋ยวหมอจะบอกคำศัพท์ภาษาอังกฤษ แล้วน้องต้องทายความหมายภาษาไทยให้ถูก!")

score = 0

for eng, thai in words.items():
    ans = input(f"คำว่า '{eng}' แปลว่าอะไร? : ").strip()
    if ans == thai:
        print("✅ ถูกต้อง!")
        score += 1
    else:
        print(f"❌ ผิดจ้า! เฉลยคือ: {thai}")

print(f"\nจบเกมแล้ว! ได้คะแนน: {score}/{len(words)} คะแนนจ้า 🎉")



number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4" : "four",
    "5" : "five"
}

score = 0

for numbers, eng in number.items():
    ans = input(f"{numbers} what is this number? : ").strip()
    if ans == eng:
        
        print(f"you're right!!")
        score += 1
    else:
        print(f"you're wrong, it is {eng}")
        
print(f"\n Game Over your score is {score}/{len(number)} congratulation!!")




