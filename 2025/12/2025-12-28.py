import re

def to_screaming_snake_case(variable_name: str) -> str:
    convert = re.sub( '(?<!^)(?=[A-Z])', '_', variable_name ).upper()
    convert = convert.replace('-','_')

    print(convert)
    return convert


assert to_screaming_snake_case("userEmail") == "USER_EMAIL"
assert to_screaming_snake_case("UserPassword") == "USER_PASSWORD"
assert to_screaming_snake_case("user_id") == "USER_ID"
assert to_screaming_snake_case("user-address") == "USER_ADDRESS"
assert to_screaming_snake_case("username") == "USERNAME"