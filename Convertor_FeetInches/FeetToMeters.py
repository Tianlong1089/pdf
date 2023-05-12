def feet_to_meters(feets):
    return feets * 0.3048
def inches_to_meters(inches):
    return inches * 0.0254

if __name__ == "__main__":
    var = feet_to_meters(1) + inches_to_meters(1)
    print(f"Un feet y una pulgada es igual a {var} meters ")