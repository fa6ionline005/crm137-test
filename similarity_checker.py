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

if __name__ == "__main__":
    # تست نمونه
    new_msg = "چراغ خیابون ولیعصر خاموش شده"
    prev_msgs = [
        "چراغ برق خیابون ولیعصر خاموشه",
        "درخت افتاده تو خیابون شهید بهشتی",
        "مشکل آسفالت در بلوار مدرس"
    ]
    
    is_new, similar_msg = check_message_similarity(new_msg, prev_msgs)
    if is_new:
        print("پیام جدید است، قابل ثبت.")
    else:
        print("پیام مشابه یافت شد:", similar_msg)
