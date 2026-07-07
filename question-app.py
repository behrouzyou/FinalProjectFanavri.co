import sqlite3


#setup database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

#ساخت جدول کاربران  (querystring)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")


# جدول سوالات
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

# افزودن سوالات
cursor.execute("SELECT COUNT(*) FROM questions")
if cursor.fetchone()[0] == 0:#اگر جدول خالی بود
    sample_questions = [
        ("تفاوت لیست و تاپل در پایتون چیست؟", "لیست ها قابل تغییرند ولی تاپل‌ها غیرقابل تغییر هستند (immutable)."),
        ("هوش مصنوعی چیست؟", "هوش مصنوعی شاخه‌ای از علوم کامپیوتر است که هدف آن ساخت سیستم‌هایی با قابلیت یادگیری و تصمیم‌گیری همانند انسان است."),
        ("کتابخانه numpy در پایتون برای چه کاری استفاده می‌شود؟", "کتابخانه numpy برای محاسبات عددی و کار با آرایه‌های چندبعدی استفاده می‌شود."),
        ("مدل زبانی چیست؟", "مدل زبانی سیستمی است که برای پیش‌بینی یا تولید متن بر اساس داده‌های زبانی آموزش دیده است."),
        ("مفهوم یادگیری نظارت‌شده چیست؟", "در یادگیری نظارت‌شده داده‌ها دارای برچسب هستند و مدل آموزش می‌بیند تا خروجی صحیح را تولید کند.")
    ]
    cursor.executemany("INSERT INTO questions (question, answer) VALUES (?, ?)", sample_questions)
    conn.commit()
