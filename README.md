from difflib import SequenceMatcher

def is_similar(text1, text2, threshold=0.8):
    similarity = SequenceMatcher(None, text1.lower(), text2.lower()).ratio()
    return similarity >= threshold

# پیام جدید شهروند
new_message = "چراغ خیابون ولیعصر خاموش شده"

# لیست پیام‌های ثبت‌شده قبلی
previous_messages = [
    "چراغ برق خیابون ولیعصر خاموشه",
    "درخت افتاده تو خیابون شهید بهشتی",
    "مشکل آسفالت در بلوار مدرس"
]

for msg in previous_messages:
    if is_similar(new_message, msg):
        print("پیام مشابه یافت شد:", msg)
        break
else:
    print("پیام جدید است، قابل ثبت.")
