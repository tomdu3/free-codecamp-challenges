import unittest
from character_limit import can_post

"""
1. can_post("Hello world") should return "short post".
Waiting:2. can_post("This is a longer message but still under eighty characters.") should return "long post".
Waiting:3. can_post("This message is too long to fit into either of the character limits for a social media post.") should return "invalid post".
    """


def test_can_post():
    assert can_post("Hello world") == "short post"
    assert (
        can_post("This is a longer message but still under eighty characters.")
        == "long post"
    )
    assert (
        can_post(
            "This message is too long to fit into either of the character limits for a social media post."
        )
        == "invalid post"
    )
