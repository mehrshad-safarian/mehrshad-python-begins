def monitor_temperature(temp):
    SAFE_MIN = 20
    SAFE_MAX = 25
    if temp   <  SAFE_MIN:
        return "too cold!"
    elif temp >  SAFE_MAX:
        return "Too Hot!"
    else:
        return "Temperature OK"
    
print(f"monitor_temperature(18):{monitor_temperature(18)}")
print(f"monitor_temperature(22):{monitor_temperature(22)}")
print(f"monitor_temperature(33):{monitor_temperature(33)}")
