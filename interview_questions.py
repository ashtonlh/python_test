def test_compute_factorial():
    input_number = 5

    result = compute_factorial(input_number)

    assert result == 120

    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))