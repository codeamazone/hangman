def what_to_do(instructions):
    x = instructions.startswith("Simon says")
    y = instructions.endswith("Simon says")
    if x:
        return instructions.replace("Simon says", "I")
    elif y:
        action = instructions.replace("Simon says", "")
        return f"I {action}"
    else:
        return "I won't do it!"
