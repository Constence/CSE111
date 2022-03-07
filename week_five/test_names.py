from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Betty", "Brown") == "Brown; Betty"
    assert make_full_name("Lionel", "Messi") == "Messi; Lionel"

def test_extract_family_name(): 
    assert extract_family_name("Brown; Betty") == "Brown"
    assert extract_family_name("Messi; Lionel") == "Messi"

def test_extract_given_name():
    assert extract_given_name("Brown/ Betty") == "Betty"
    assert extract_given_name("Messi/ Lionel") == "Lionel"

pytest.main(["-v", "--tb=line", "-rN", __file__])
