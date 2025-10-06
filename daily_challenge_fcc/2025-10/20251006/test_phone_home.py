from phone_home import send_message


def assert_almost_equal(a, b, places=4):
    """Helper to compare numbers rounded to specified decimal places."""
    assert round(a, places) == round(b, places), f"Expected {b} got {a}"


def test_examples():
    # Provided failing cases
    assert_almost_equal(send_message([300000, 300000]), 2.5)
    assert_almost_equal(send_message([384400, 384400]), 3.0627)
    assert_almost_equal(send_message([54600000, 54600000]), 364.5)
    assert_almost_equal(send_message([1000000, 500000000, 1000000]), 1674.3333)
    assert_almost_equal(send_message([10000, 21339, 50000, 31243, 10000]), 2.4086)
    assert_almost_equal(send_message([802101, 725994, 112808, 3625770, 481239]), 21.1597)
