#!/usr/bin/env python3
from difflib import SequenceMatcher

def is_similar(text1, text2, threshold=0.8):
    """
    بررسی شباهت دو متن با استفاده از SequenceMatcher.
    
    پارامترها:
        text1 (str): متن اول
        text2 (str): متن دوم
        threshold (float): آستانه شباهت (پیش‌فرض: 0.8)
    
    خروجی:
        bool: True اگر شباهت بیشتر یا برابر با آستانه باشد، در غیر این صورت False
    """
    similarity = SequenceMatcher(None, text1.lower(), text2.lower()).ratio()
    return similarity >= threshold

def check_message_similarity(new_message, previous_messages, threshold=0.8):
    """
    بررسی شباهت پیام جدید با لیست پیام‌های قبلی.
    
    پارامترها:
        new_message (str): پیام جدید
        previous_messages (list): لیست پیام‌های قبلی
        threshold (float): آستانه شباهت (پیش‌فرض: 0.8)
    
    خروجی:
        tuple: (bool, str or None) - وضعیت ثبت و پیام مشابه (در صورت وجود)
    """
    for msg in previous_messages:
        if is_similar(new_message, msg, threshold):
            return False, msg
    return True, None

def main():
    # پیام جدید
    new_message = "چراغ خیابون ولیعصر خاموش شده"

    # لیست پیام‌های ثبت‌شده قبلی
    previous_messages = [
        "چراغ برق خیابون ولیعصر خاموشه",
        "درخت افتاده تو خیابون شهید بهشتی",
        "مشکل آسفالت در بلوار مدرس"
    ]

    # بررسی شباهت
    is_new, similar_msg = check_message_similarity(new_message, previous_messages, threshold=0.8)

    # خروجی
    if is_new:
        print("پیام جدید است، قابل ثبت.")
    else:
        print("پیام مشابه یافت شد:", similar_msg)

if __name__ == "__main__":
    main()

"""
README:
# Similarity Checker
یک ابزار ساده برای بررسی شباهت بین پیام‌ها با استفاده از `difflib.SequenceMatcher` در پایتون.

## استفاده
1. این فایل را اجرا کنید:
   ```bash
   python similarity_checker.py
