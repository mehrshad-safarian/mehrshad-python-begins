sales_data = [
    [110, 520, 340, 800], # Product A daily sales
    [250, 660, 420, 720], # Product B daily sales
    [730, 240, 910, 500], # Product C daily sales
    [0, 340, 800, 900], # Product E daily sales
]

daily_encome = (sum(day) for day in sales_data)
print(f"A Product Encome : ${next(daily_encome)}")
print(f"B Product Encome : ${next(daily_encome)}")
print(f"C Product Encome : ${next(daily_encome)}")
print(f"E Product Encome : ${next(daily_encome)}")

Total_Encome = list(map(sum, sales_data))
print(f"Total Encome: {Total_Encome}")