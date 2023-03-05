def speed_calc(kmph):
    coefficient = 10.0/36.0
    return kmph * coefficient


kmph_data = float(input())
if kmph_data > 299792458.0*3.6:
    print("Nic nie porusza się z taką prędkością!")
else:
    print(f"Prędkość {kmph_data} km/h wynosi {speed_calc(kmph_data)} m/s.")
