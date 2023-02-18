def eval_loop():
  result = None
  expression = str(input("Enter the expression: "))
  while expression != "done":
    try:
      result = eval(expression)
    except Exception:
      print("Wrong expression!")
      return result
    expression = str(input("Enter the expression: "))
  return result

print("Value returned:", eval_loop())