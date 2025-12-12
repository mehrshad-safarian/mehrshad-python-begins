def print_section(title):
    print(f"\n{'=' * 70}")
    print(f"{title}")
    print(f"\n{'=' * 70}")
print_section("basic boolean operators - day off checker".title())

is_weekend = True
is_holiday = False
print("Current status:")
print(f"Is it a weekend?: {is_weekend}")
print(f"Is it a holiday?: {is_holiday}")
get_day_off = is_weekend or is_holiday
print("\nFinal Decision:")
print(f"Does the employee get a day off? {get_day_off}")
print("lets simiulate holiday during a workday...")
is_weekend = False
is_holiday = True
get_day_off = is_weekend or is_holiday
print(f"Is it a weekend?: {is_weekend}")
print(f"Does the employee get a ady off?: {get_day_off}")
if __name__ == "__name__":
    print("\nBasic boolean demo completed! ".istitle())



