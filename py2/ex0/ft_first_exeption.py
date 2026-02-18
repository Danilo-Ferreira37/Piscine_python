def check_temperature(temp_str: str) -> int | None:
    print(f'Testing temperature: {temp_str}')
    try:
        temperature = int(temp_str)
        if temperature < 0:
            raise ValueError(f'Error: {temp_str}°C is too cold for plants (min 0°C)\n')
        if temperature > 40:
            raise ValueError(f'Error: {temp_str}°C is too hot for plants (max 40°C)\n')
        print(f'Temperature {temp_str}°C is perfect for plants!\n')
        return temperature
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f'Invalid literal: {temp_str} is not a valid number\n')
        else:
            print(e)
        return None

def test_temperature_input() -> None:
    check_temperature('25')
    check_temperature('abc')
    check_temperature('100')
    check_temperature('-50')
        
    print('All tests completed - program didn’t crash!')

if __name__ == '__main__':
    print('Garden Temperature Checker')
    test_temperature_input()