"""Tests for the Statistics module."""

import pytest
import math
from src.stats import Statistics


@pytest.fixture
def stats():
    """Provide a fresh Statistics instance for each test."""
    return Statistics()


# ── Mean Tests ──────────────────────────────────────────────────────

class TestMean:
    """Test suite for the mean operation."""

    def test_mean_basic(self, stats):
        assert stats.mean([1, 2, 3, 4, 5]) == 3.0

    def test_mean_single_value(self, stats):
        assert stats.mean([42]) == 42.0

    def test_mean_floats(self, stats):
        assert stats.mean([1.5, 2.5, 3.0]) == pytest.approx(7.0 / 3.0)

    def test_mean_negative(self, stats):
        assert stats.mean([-5, 0, 5]) == 0.0

    def test_mean_all_same(self, stats):
        assert stats.mean([7, 7, 7, 7]) == 7.0

    def test_mean_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute mean of an empty data set"):
            stats.mean([])


# ── Median Tests ────────────────────────────────────────────────────

class TestMedian:
    """Test suite for the median operation."""

    def test_median_odd(self, stats):
        assert stats.median([1, 3, 5]) == 3.0

    def test_median_even(self, stats):
        assert stats.median([1, 2, 3, 4]) == 2.5

    def test_median_unsorted(self, stats):
        assert stats.median([5, 1, 3, 2, 4]) == 3.0

    def test_median_single(self, stats):
        assert stats.median([42]) == 42.0

    def test_median_two_values(self, stats):
        assert stats.median([10, 20]) == 15.0

    def test_median_floats(self, stats):
        assert stats.median([1.1, 2.2, 3.3]) == 2.2

    def test_median_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute median of an empty data set"):
            stats.median([])


# ── Mode Tests ──────────────────────────────────────────────────────

class TestMode:
    """Test suite for the mode operation."""

    def test_mode_single(self, stats):
        assert stats.mode([1, 1, 2, 3]) == [1.0]

    def test_mode_multiple(self, stats):
        result = stats.mode([1, 1, 2, 2, 3])
        assert result == [1.0, 2.0]

    def test_mode_all_unique(self, stats):
        result = stats.mode([1, 2, 3, 4])
        # All values appear once, so all are modes
        assert result == [1.0, 2.0, 3.0, 4.0]

    def test_mode_all_same(self, stats):
        assert stats.mode([5, 5, 5]) == [5.0]

    def test_mode_floats(self, stats):
        result = stats.mode([1.5, 1.5, 2.5])
        assert result == [1.5]

    def test_mode_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute mode of an empty data set"):
            stats.mode([])


# ── Variance Tests ──────────────────────────────────────────────────

class TestVariance:
    """Test suite for the variance operation."""

    def test_variance_population(self, stats):
        # Population variance of [2, 4, 4, 4, 5, 5, 7, 9]
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        # mean = 5, sum of squared diff = (9+1+1+1+0+0+4+16) = 32, variance = 32/8 = 4
        assert stats.variance(data) == pytest.approx(4.0)

    def test_variance_sample(self, stats):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        # Sample variance = 32/7 ≈ 4.571
        assert stats.variance(data, ddof=1) == pytest.approx(32.0 / 7.0)

    def test_variance_all_same(self, stats):
        assert stats.variance([5, 5, 5, 5]) == 0.0

    def test_variance_two_values(self, stats):
        assert stats.variance([1, 3]) == 1.0  # mean=2, diff=1,1 => 2/2=1

    def test_variance_insufficient_data(self, stats):
        with pytest.raises(ValueError, match="Cannot compute variance with ddof=1 on a data set of size 1"):
            stats.variance([5], ddof=1)

    def test_variance_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute variance with ddof=0 on a data set of size 0"):
            stats.variance([])


# ── Standard Deviation Tests ───────────────────────────────────────

class TestStandardDeviation:
    """Test suite for the standard deviation operation."""

    def test_std_population(self, stats):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        # variance = 4, std = sqrt(4) = 2
        assert stats.standard_deviation(data) == pytest.approx(2.0)

    def test_std_sample(self, stats):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        # sample variance = 32/7 ≈ 4.571, std = sqrt(32/7)
        assert stats.standard_deviation(data, ddof=1) == pytest.approx(math.sqrt(32.0 / 7.0))

    def test_std_all_same(self, stats):
        assert stats.standard_deviation([5, 5, 5, 5]) == 0.0

    def test_std_insufficient_data(self, stats):
        with pytest.raises(ValueError):
            stats.standard_deviation([5], ddof=1)


# ── Min/Max Tests ──────────────────────────────────────────────────

class TestMinMax:
    """Test suite for min and max operations."""

    def test_min(self, stats):
        assert stats.min([3, 1, 4, 1, 5, 9]) == 1.0

    def test_min_single(self, stats):
        assert stats.min([42]) == 42.0

    def test_min_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute min of an empty data set"):
            stats.min([])

    def test_max(self, stats):
        assert stats.max([3, 1, 4, 1, 5, 9]) == 9.0

    def test_max_single(self, stats):
        assert stats.max([42]) == 42.0

    def test_max_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute max of an empty data set"):
            stats.max([])


# ── Range Tests ────────────────────────────────────────────────────

class TestRange:
    """Test suite for the range operation."""

    def test_range_basic(self, stats):
        assert stats.range([1, 5, 3, 9, 2]) == 8.0

    def test_range_single(self, stats):
        assert stats.range([42]) == 0.0

    def test_range_all_same(self, stats):
        assert stats.range([7, 7, 7]) == 0.0

    def test_range_negative(self, stats):
        assert stats.range([-5, 10]) == 15.0

    def test_range_empty(self, stats):
        with pytest.raises(ValueError, match="Cannot compute range of an empty data set"):
            stats.range([])


# ── Quartiles Tests ────────────────────────────────────────────────

class TestQuartiles:
    """Test suite for the quartiles operation."""

    def test_quartiles_odd_count(self, stats):
        # Data: [1, 3, 5, 7, 9] — odd count
        # Q2 = 5, lower = [1, 3], Q1 = 2, upper = [7, 9], Q3 = 8
        q = stats.quartiles([1, 3, 5, 7, 9])
        assert q["Q1"] == 2.0
        assert q["Q2"] == 5.0
        assert q["Q3"] == 8.0

    def test_quartiles_even_count(self, stats):
        # Data: [1, 2, 3, 4, 5, 6] — even count
        # Q2 = 3.5, lower = [1, 2, 3], Q1 = 2, upper = [4, 5, 6], Q3 = 5
        q = stats.quartiles([1, 2, 3, 4, 5, 6])
        assert q["Q1"] == 2.0
        assert q["Q2"] == 3.5
        assert q["Q3"] == 5.0

    def test_quartiles_unsorted(self, stats):
        q = stats.quartiles([9, 1, 5, 3, 7])
        assert q["Q2"] == 5.0

    def test_quartiles_too_few(self, stats):
        with pytest.raises(ValueError, match="Cannot compute quartiles of a data set with fewer than 2 elements"):
            stats.quartiles([5])


# ── IQR Tests ──────────────────────────────────────────────────────

class TestIQR:
    """Test suite for the IQR operation."""

    def test_iqr_basic(self, stats):
        # [1, 3, 5, 7, 9] -> Q1=2, Q3=8 -> IQR=6
        assert stats.iqr([1, 3, 5, 7, 9]) == 6.0

    def test_iqr_even(self, stats):
        assert stats.iqr([1, 2, 3, 4, 5, 6]) == 3.0

    def test_iqr_too_few(self, stats):
        with pytest.raises(ValueError):
            stats.iqr([5])


# ── Edge Cases ─────────────────────────────────────────────────────

class TestEdgeCases:
    """Test edge cases and error conditions across the module."""

    def test_large_dataset(self, stats):
        """Verify performance and correctness with a larger data set."""
        data = list(range(1, 1001))
        assert stats.mean(data) == pytest.approx(500.5)
        assert stats.median(data) == pytest.approx(500.5)
        assert stats.min(data) == 1.0
        assert stats.max(data) == 1000.0

    def test_negative_values(self, stats):
        data = [-10, -5, 0, 5, 10]
        assert stats.mean(data) == 0.0
        assert stats.median(data) == 0.0
        assert stats.variance(data) == pytest.approx(50.0)

    def test_floating_point_precision(self, stats):
        """Test that results handle floating point correctly."""
        data = [0.1, 0.2, 0.3, 0.4]
        assert stats.mean(data) == pytest.approx(0.25)
        assert stats.median(data) == pytest.approx(0.25)
