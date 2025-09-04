#!/usr/bin/env python


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 or not s[:2].isalpha():
        # print("Bad length or 2 first not alpha")
        return False
    elif len(s) == 2 and s[:2].isalpha():
        # print("Only 2 alphas")
        return True

    else:
        # print(f"0, {s[0]} - First alpha")
        # print(f"1, {s[1]} - Second alpha")
        i = 2
        while i < len(s):
            if s[i].isalpha():
                if s[i - 1].isdecimal():
                    # print(f"{i}, {s[i]} - Decimal before alpha")
                    return False
                elif len(s) == (i + 1):
                    # print(f"{i}, {s[i]} - Only alphas")
                    return True
                else:
                    # print(f"{i}, {s[i]} - Iterating alphas")
                    pass
            elif s[i].isdecimal():
                if s[i] == "0" and not s[i - 1].isdecimal():
                    # print(f"{i}, {s[i]} - First decimal is 0")
                    return False
                else:
                    if s[i].isdecimal() and len(s) == (i + 1):
                        # print(f"{i}, {s[i]} - Iterating last decimal")
                        return True
                    elif s[i].isdecimal():
                        # print(f"{i}, {s[i]} - Iterating decimals")
                        pass
                    else:
                        # print(f"{i}, {s[i]} - Is not decimal")
                        return False
            else:
                # print(f"{i}, {s[i]} - Not alpha, neither decimal")
                return False
            i += 1


main()
