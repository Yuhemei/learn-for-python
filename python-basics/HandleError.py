try:
    print(0)
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("finally")