"""
Unit Tests for BMI Calculator
CSE 4283/6283 Assignment 2

Test Strategy: Boundary Value Analysis (BVA)
  - Tests at and around each category boundary:
      Underweight / Normal weight boundary : BMI = 18.5
      Normal weight / Overweight boundary  : BMI = 25.0
      Overweight / Obese boundary          : BMI = 30.0
"""

import pytest
from bmi_calculator import calculate_bmi, get_bmi_category

# ──────────────────────────────────────────────
# Tests for calculate_bmi()
# ──────────────────────────────────────────────

class TestCalculateBMI:
    """Tests for the calculate_bmi function."""

    def test_example_from_spec(self):
        """Example from assignment: 5'3", 125 lbs → BMI 22.7"""
        result = calculate_bmi(5, 3, 125)
        assert result == 22.7

    def test_returns_float(self):
        """BMI result should be a float (or int treated as numeric)."""
        result = calculate_bmi(5, 10, 170)
        assert isinstance(result, (float, int))

    def test_result_rounded_to_one_decimal(self):
        """Result should be rounded to 1 decimal place."""
        result = calculate_bmi(5, 3, 125)
        # Check rounding by verifying no more than 1 decimal digit
        assert result == round(result, 1)

    def test_zero_extra_inches(self):
        """Height with 0 extra inches should work correctly."""
        result = calculate_bmi(6, 0, 180)
        assert isinstance(result, float)

    def test_tall_heavy_person(self):
        """6'5", 300 lbs → Obese range."""
        result = calculate_bmi(6, 5, 300)
        assert result >= 30.0

    def test_short_light_person(self):
        """4'10", 85 lbs → Underweight range."""
        result = calculate_bmi(4, 10, 85)
        assert result < 18.5

    def test_formula_correctness(self):
        """
        Manual verification:
          5'0" = 60 inches; 130 lbs
          weight_kg = 130 * 0.45 = 58.5
          height_m  = 60 * 0.025 = 1.5
          bmi       = 58.5 / (1.5**2) = 58.5 / 2.25 = 26.0
        """
        result = calculate_bmi(5, 0, 130)
        assert result == 26.0


# ──────────────────────────────────────────────
# Tests for get_bmi_category()
# ──────────────────────────────────────────────

class TestGetBMICategory:
    """
    Tests for get_bmi_category using Boundary Value Analysis.

    Boundaries:
      18.5  → Underweight/Normal weight boundary
      25.0  → Normal weight/Overweight boundary
      30.0  → Overweight/Obese boundary
    """

    # --- Underweight ---
    def test_underweight_just_below_boundary(self):
        """BMI 18.4 — just below Normal weight boundary → Underweight."""
        assert get_bmi_category(18.4) == "Underweight"

    # --- Normal weight ---
    def test_normal_weight_at_lower_boundary(self):
        """BMI 18.5 — exactly at lower boundary → Normal weight."""
        assert get_bmi_category(18.5) == "Normal weight"

    def test_normal_weight_middle(self):
        """BMI 22.0 — middle of Normal weight range."""
        assert get_bmi_category(22.0) == "Normal weight"

    def test_normal_weight_at_upper_boundary(self):
        """BMI 24.9 — exactly at upper boundary → Normal weight."""
        assert get_bmi_category(24.9) == "Normal weight"
      
    # --- Overweight ---
    def test_overweight_at_lower_boundary(self):
        """BMI 25.0 — exactly at lower boundary → Overweight."""
        assert get_bmi_category(25.0) == "Overweight"

    def test_overweight_middle(self):
        """BMI 27.5 — middle of Overweight range."""
        assert get_bmi_category(27.5) == "Overweight"

    def test_overweight_at_upper_boundary(self):
        """BMI 29.9 — exactly at upper boundary → Overweight."""
        assert get_bmi_category(29.9) == "Overweight"

    # --- Obese ---
    def test_obese_at_lower_boundary(self):
        """BMI 30.0 — exactly at Obese boundary → Obese."""
        assert get_bmi_category(30.0) == "Obese"

    def test_obese_just_above_boundary(self):
        """BMI 30.1 — just above Obese boundary → Obese."""
        assert get_bmi_category(30.1) == "Obese"

    def test_clearly_obese(self):
        """BMI 40.0 — well inside Obese range."""
        assert get_bmi_category(40.0) == "Obese"


# ──────────────────────────────────────────────
# End-to-end integration tests
# ──────────────────────────────────────────────

class TestEndToEnd:
    """Integration tests: real height/weight → correct category."""

    def test_underweight_person(self):
        """Very light person should be Underweight."""
        bmi = calculate_bmi(5, 5, 100)
        assert get_bmi_category(bmi) == "Underweight"

    def test_normal_weight_person(self):
        """Average person at healthy weight → Normal weight."""
        bmi = calculate_bmi(5, 7, 150)
        assert get_bmi_category(bmi) == "Normal weight"

    def test_overweight_person(self):
        """Moderately heavy person → Overweight. 5'10" 190 lbs = ~27.3 BMI."""
        bmi = calculate_bmi(5, 10, 190)
        assert get_bmi_category(bmi) == "Overweight"

    def test_obese_person(self):
        """Heavy person → Obese."""
        bmi = calculate_bmi(5, 6, 250)
        assert get_bmi_category(bmi) == "Obese"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
