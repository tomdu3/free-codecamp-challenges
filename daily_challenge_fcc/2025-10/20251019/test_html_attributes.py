import pytest
from html_attributes import extract_attributes

def test_span_class():
    assert extract_attributes('<span class="red"></span>') == ["class, red"]

def test_meta_charset():
    assert extract_attributes('<meta charset="UTF-8" />') == ["charset, UTF-8"]

def test_no_attributes():
    assert extract_attributes("<p>Lorem ipsum dolor sit amet</p>") == []

def test_input_multiple_attributes():
    assert extract_attributes('<input name="email" type="email" required="true" />') == [
        "name, email",
        "type, email",
        "required, true",
    ]

def test_button_id_and_class():
    assert extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') == [
        "id, submit",
        "class, btn btn-primary",
    ]