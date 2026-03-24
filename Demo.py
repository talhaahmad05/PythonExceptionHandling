# ─── 1. ArithmeticException → ZeroDivisionError ───────────────────────────
print("=== Arithmetic Exception ===")
try:
    numerator = 100
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    print(f"Arithmetic Error: Cannot divide by zero. Details: {e}")


# ─── 2. NullPointerException → AttributeError / TypeError ─────────────────
print("\n=== Null Pointer Exception ===")
try:
    obj = None
    length = len(obj)        # calling a function on None
except TypeError as e:
    print(f"Null Pointer Error: Object is None/invalid. Details: {e}")


# ─── 3. NumberFormatException → ValueError ────────────────────────────────
print("\n=== Number Format Exception ===")
try:
    user_input = "abc123"
    number = int(user_input)  # invalid string-to-int conversion
except ValueError as e:
    print(f"Number Format Error: Invalid number format. Details: {e}")


# ─── 4. ArrayIndexOutOfBoundsException → IndexError ──────────────────────
print("\n=== Array Index Out Of Bounds Exception ===")
try:
    my_list = [10, 20, 30]
    print(my_list[10])        # index 10 doesn't exist
except IndexError as e:
    print(f"Index Out of Bounds Error: Invalid index accessed. Details: {e}")


# ─── All in one with finally ───────────────────────────────────────────────
print("\n=== Combined Example with finally ===")
try:
    data = ["5", "hello", "15"]
    total = int(data[0]) + int(data[1])   # ValueError here
except ZeroDivisionError as e:
    print(f"Arithmetic Error: {e}")
except TypeError as e:
    print(f"Null Pointer Error: {e}")
except ValueError as e:
    print(f"Number Format Error: {e}")
except IndexError as e:
    print(f"Index Out of Bounds Error: {e}")
else:
    print(f"Success! Total = {total}")
finally:
    print("Execution finished.")