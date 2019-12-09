def test_input_text(expected_result, actual_result):
    try:
        assert actual_result in expected_result
    except AssertionError:
        print(f"expected \'{actual_result}\' to be substring of \'{expected_result}\'")
x, y = map(str, input().split())
test_input_text(x, y)
