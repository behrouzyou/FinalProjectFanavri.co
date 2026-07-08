import tkinter as tk
from tkinter import messagebox, scrolledtext,ttk
import sqlite3
from PIL import Image,ImageTk

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

#ساخت یوز
def register_user():
    username = entry_username_signup.get()#گرفتن اطلاعات از وردوی
    password = entry_password_signup.get()

    if not username or not password:#اگر وجود نداشت
        messagebox.showwarning("خطا", "نام کاربری و گذرواژه را وارد کنید.")
        return

    try:#بررسی احتمال خطا و ساخت کاربر
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("موفق", "ثبت‌نام انجام شد! اکنون وارد شوید.")
        signup_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("خطا", "این نام کاربری قبلاً ثبت شده است.")

#لاگین کاربر
def login_user():
    username = entry_username_login.get()#گرفتن اطلاعات از وردوی
    password = entry_password_login.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()#چک کردن وجود کاربر با (query string WHERE)
    if user:
        messagebox.showinfo("ورود موفق", f"خوش آمدید {username}!")

    else:
        messagebox.showerror("خطا", "نام کاربری یا رمز اشتباه است.")


#    TKINTER
#    جدول ساخت کاربر جدید
def open_signup():
    global signup_window, entry_username_signup, entry_password_signup
    signup_window = tk.Toplevel(root)
    signup_window.title("ثبت نام")
    signup_window.geometry("600x400")
    ttk.Label(signup_window, text="نام کاربری:").pack()
    entry_username_signup = ttk.Entry(signup_window)
    entry_username_signup.pack()

    ttk.Label(signup_window, text="رمز عبور:").pack()
    entry_password_signup = ttk.Entry(signup_window, show="*")
    entry_password_signup.pack()


    ttk.Button(signup_window, text="ثبت‌ نام", command=register_user,style="Accent.TButton").pack(pady=10)

#جدول ورود کاربر
root =tk.Tk()
root.tk.call("source","theme/forest-light.tcl")
ttk.Style(root).theme_use("forest-light")
root.title("صفحه ورود")
root.geometry("600x400")
bg_image = Image.open("background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

#  تصویر به عنوان پس‌زمینه
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

ttk.Label(root, text="نام کاربری:").pack()
entry_username_login = ttk.Entry(root)
entry_username_login.pack()

ttk.Label(root, text="رمز عبور:").pack()
entry_password_login = ttk.Entry(root, show="*")
entry_password_login.pack()

ttk.Button(root, text="ورود", command=login_user,style="Accent.TButton").pack(pady=5)
ttk.Button(root, text="ثبت‌نام جدید", command=open_signup,style="Accent.TButton").pack()
root.mainloop()
