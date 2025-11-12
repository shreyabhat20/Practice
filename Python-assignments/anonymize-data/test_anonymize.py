import re
from anonymize import hash_email, mask_phone

def test_hash_email_consistency():
    email = "Test@Example.com"
    assert hash_email(email) == hash_email("test@example.com")
    assert len(hash_email(email)) == 64 

def test_mask_phone_basic():
    phone = "9876543210"
    masked = mask_phone(phone)
    assert masked.endswith("3210")
    assert masked.count("X") == 6

def test_mask_phone_with_symbols():
    phone = "(987)-654-3210"
    masked = mask_phone(phone)
    assert masked.endswith("3210")
    assert masked[0] == "(" and masked[4] == ")"

def test_mask_phone_short_number():
    phone = "123"
    masked = mask_phone(phone)
    assert re.match(r"^[X\-() ]+$", masked)

def test_hash_email_unique():
    assert hash_email("a@example.com") != hash_email("b@example.com")
