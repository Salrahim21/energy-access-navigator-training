
appliances = [
    {"name":"LED lamp",
     "power_w":10,
     "hours_per_day":5},
    {"name":"TV",
     "power_w":60,
     "hours_per_day":4}
]


def calculate_daily_kwh(appliances: list[dict]) -> float:
    total_wh = 0

    for a in appliances:
        power = a["power_w"]
        hours = a["hours_per_day"]

        energy_wh = power * hours
        total_wh += energy_wh
        if hours < 0 or hours > 24:
         raise ValueError("Hours must be between 0 and 24")

    return total_wh / 1000


try:
    result = calculate_daily_kwh(appliances)
    print(f"Daily energy consumption: {result} kWh")

except ValueError as error:
    print(f"Unable to calculate energy: {error}")
if __name__ == "__main__":
    try:
        result = calculate_daily_kwh(appliances)
        print(f"Daily energy consumption: {result} kWh")

    except ValueError as error:
        print(f"Unable to calculate energy: {error}")