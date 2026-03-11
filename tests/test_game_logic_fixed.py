import pytest
from logic_utils import (
    check_guess,
    update_score,
    get_range_for_difficulty,
    parse_guess
)

def test_check_guess_logic_fix():
    """Verify that high/low hints are correct (fixed hint bug)."""
    # Too High
    outcome, message = check_guess(99, 36)
    assert outcome == "Too High"
    assert "LOWER" in message
    
    # Too Low
    outcome, message = check_guess(10, 36)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    
    # Win
    outcome, message = check_guess(36, 36)
    assert outcome == "Win"

def test_update_score_glitch_fix():
    """Verify that scores are correctly deducted for wrong guesses (fixed scoring bug)."""
    current_score = 100
    
    # Even-numbered attempt that previously gave +5 points
    new_score = update_score(current_score, "Too High", attempt_number=2)
    assert new_score == 95, "Should deduct 5 points even on even attempts"
    
    # Odd-numbered attempt
    new_score = update_score(current_score, "Too Low", attempt_number=3)
    assert new_score == 95

def test_difficulty_ranges():
    """Verify the correct ranges for each difficulty."""
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_parse_guess_validation():
    """Verify that user input is correctly parsed or rejected."""
    # Valid
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    
    # Decimal (should be converted to int)
    ok, val, err = parse_guess("42.5")
    assert ok is True
    assert val == 42
    
    # Non-number
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."
    
    # Empty
    ok, val, err = parse_guess("")
    assert ok is False
    assert "Enter a guess" in err
