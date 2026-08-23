from fastmcp import FastMCP

mcp = FastMCP("calculator")


def _as_number(x):
    if isinstance(x, (int, float)):
        return float(x)

    if isinstance(x, str):
        return float(x.strip())

    raise TypeError("Expected a number")


@mcp.tool()
async def calculator(
    first_num: float,
    second_num: float,
    operation: str
) -> dict:
    """Perform add, subtract, multiply or divide."""

    a = _as_number(first_num)
    b = _as_number(second_num)

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = a / b

    else:
        raise ValueError(
            "Invalid operation. Use add, subtract, multiply or divide."
        )

    return {
        "first_num": a,
        "second_num": b,
        "operation": operation,
        "result": result
    }


# if __name__ == "__main__":
#     mcp.run()