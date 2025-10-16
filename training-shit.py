import requests  # کتابخانه مخصوص درخواست به API

# آدرس API عمومی برای کشورها
url = "https://restcountries.com/v3.1/name/iran"

# فرستادن درخواست GET
response = requests.get(url)

# بررسی وضعیت پاسخ
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON (داده قابل استفاده)
    country = data[0]  # اولین نتیجه از لیست
    print("نام کشور:", country["name"]["common"])
    print("پایتخت:", country["capital"][0])
    print("جمعیت:", country["population"])
    print("منطقه:", country["region"])
else:
    print("خطا در دریافت داده‌ها:", response.status_code)
