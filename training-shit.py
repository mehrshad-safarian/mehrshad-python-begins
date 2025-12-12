while True:
    try:
        # TODO 1
        receipt_number = 1000

        # TODO 2 & 3: گرفتن ورودی‌ها
        slice = int(input("How many slices: "))
        price_per_slice = float(input("Price per slice: "))

        # TODO 4: محاسبه کل
        total = slice * price_per_slice

        # TODO 5: مقایسه با شماره رسید و چاپ نتیجه
        print(total == receipt_number)

        break  # وقتی همه چیز درست بود، از حلقه خارج می‌شویم

    # BONUS TODO 6: مدیریت خطا
    except ValueError:
        print("That's not a valid number! Please try again.")
