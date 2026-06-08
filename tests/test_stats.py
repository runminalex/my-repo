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


# ── Covariance Tests ──────────────────────────────────────────────

class TestCovariance:
    """Test suite for the covariance operation."""

    def test_covariance_positive(self, stats):
        """Test positive covariance for positively correlated data."""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        # Perfect positive linear relationship
        # mean_x = 3, mean_y = 6
        # cov = ((1-3)(2-6) + (2-3)(4-6) + (3-3)(6-6) + (4-3)(8-6) + (5-3)(10-6)) / 5
        # cov = (8 + 4 + 0 + 4 + 8) / 5 = 24 / 5 = 4.8
        assert stats.covariance(x, y) == pytest.approx(4.8)

    def test_covariance_sample(self, stats):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        # Sample covariance = 24 / 4 = 6
        assert stats.covariance(x, y, ddof=1) == pytest.approx(6.0)

    def test_covariance_negative(self, stats):
        """Test negative covariance for negatively correlated data."""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        cov = stats.covariance(x, y)
        assert cov < 0

    def test_covariance_zero(self, stats):
        """Test zero covariance for uncorrelated data."""
        x = [1, 2, 3, 4, 5]
        y = [3, 3, 3, 3, 3]
        # y has zero variance, so cov should be 0
        assert stats.covariance(x, y) == pytest.approx(0.0)

    def test_covariance_different_lengths(self, stats):
        with pytest.raises(ValueError, match="Cannot compute covariance of data sets with different lengths"):
            stats.covariance([1, 2, 3], [1, 2])

    def test_covariance_insufficient_data(self, stats):
        with pytest.raises(ValueError):
            stats.covariance([5], [5], ddof=1)

    def test_covariance_empty(self, stats):
        with pytest.raises(ValueError):
            stats.covariance([], [])


# ── Pearson Correlation Tests ─────────────────────────────────────

class TestPearsonCorrelation:
    """Test suite for the Pearson correlation coefficient."""

    def test_pearson_perfect_positive(self, stats):
        """Perfect positive linear correlation should be 1.0."""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        assert stats.pearson_correlation(x, y) == pytest.approx(1.0)

    def test_pearson_perfect_negative(self, stats):
        """Perfect negative linear correlation should be -1.0."""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        assert stats.pearson_correlation(x, y) == pytest.approx(-1.0)

    def test_pearson_no_correlation(self, stats):
        """No linear correlation should be near 0."""
        x = [1, 2, 3, 4, 5]
        y = [3, 3, 3, 3, 3]
        with pytest.raises(ValueError, match="zero variance"):
            stats.pearson_correlation(x, y)

    def test_pearson_strong_positive(self, stats):
        """Strong positive correlation, but not perfect."""
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2.1, 4.2, 5.9, 8.1, 10.2, 11.8, 14.1, 15.9, 18.2, 19.8]
        r = stats.pearson_correlation(x, y)
        assert r == pytest.approx(1.0, abs=0.02)

    def test_pearson_known_value(self, stats):
        """Test with known values from statistics."""
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        # Known correlation for this data
        r = stats.pearson_correlation(x, y)
        assert r == pytest.approx(0.986, abs=0.01)

    def test_pearson_different_lengths(self, stats):
        with pytest.raises(ValueError, match="Cannot compute correlation of data sets with different lengths"):
            stats.pearson_correlation([1, 2, 3], [1, 2])

    def test_pearson_too_few_points(self, stats):
        with pytest.raises(ValueError, match="Cannot compute correlation with fewer than 2 data points"):
            stats.pearson_correlation([1], [2])

    def test_pearson_constant_x(self, stats):
        """Constant x should raise ValueError (zero variance)."""
        with pytest.raises(ValueError, match="zero variance"):
            stats.pearson_correlation([5, 5, 5], [1, 2, 3])


# ── Spearman Correlation Tests ────────────────────────────────────

class TestSpearmanCorrelation:
    """Test suite for the Spearman rank correlation coefficient."""

    def test_spearman_perfect_monotonic(self, stats):
        """Perfect monotonic relationship should be 1.0."""
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]  # Monotonically increasing (non-linear)
        r = stats.spearman_correlation(x, y)
        assert r == pytest.approx(1.0)

    def test_spearman_perfect_negative_monotonic(self, stats):
        """Perfect inverse monotonic relationship should be -1.0."""
        x = [1, 2, 3, 4, 5]
        y = [25, 16, 9, 4, 1]  # Monotonically decreasing
        r = stats.spearman_correlation(x, y)
        assert r == pytest.approx(-1.0)

    def test_spearman_with_ties(self, stats):
        """Spearman with tied ranks should still produce valid results."""
        x = [1, 2, 3, 4, 5]
        y = [5, 5, 5, 6, 7]  # Some ties in y
        r = stats.spearman_correlation(x, y)
        # Manually compute: ranks of x = [1,2,3,4,5], ranks of y = [2,2,2,4,5]
        # Pearson on ranks...
        assert r == pytest.approx(0.821, abs=0.01)

    def test_spearman_pearson_agreement(self, stats):
        """For linear data, Spearman should equal Pearson."""
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2 * v + 1 for v in x]
        r_pearson = stats.pearson_correlation(x, y)
        r_spearman = stats.spearman_correlation(x, y)
        assert r_pearson == pytest.approx(r_spearman)

    def test_spearman_different_lengths(self, stats):
        with pytest.raises(ValueError, match="Cannot compute correlation of data sets with different lengths"):
            stats.spearman_correlation([1, 2, 3], [1, 2])

    def test_spearman_too_few_points(self, stats):
        with pytest.raises(ValueError, match="Cannot compute correlation with fewer than 2 data points"):
            stats.spearman_correlation([1], [2])


# ── Linear Regression Tests ───────────────────────────────────────

class TestLinearRegression:
    """Test suite for the linear regression operation."""

    def test_regression_perfect_line(self, stats):
        """Perfect linear relationship: y = 2x + 1."""
        x = [1, 2, 3, 4, 5]
        y = [3, 5, 7, 9, 11]  # y = 2x + 1
        result = stats.linear_regression(x, y)
        assert result["slope"] == pytest.approx(2.0)
        assert result["intercept"] == pytest.approx(1.0)
        assert result["r_squared"] == pytest.approx(1.0)
        assert result["r"] == pytest.approx(1.0)

    def test_regression_fit(self, stats):
        """Known regression line from statistical data."""
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        result = stats.linear_regression(x, y)
        # slope = cov(x,y) / var(x)
        # cov(x,y)_pop = 10.8, var(x)_pop = 2, slope = 10.8/2 = 5.4
        # intercept = mean(y) - slope * mean(x) = 5.6 - 5.4 * 3 = 5.6 - 16.2 = -10.6
        assert result["slope"] == pytest.approx(5.4, abs=0.1)
        assert result["intercept"] == pytest.approx(-10.6, abs=0.1)
        assert result["r_squared"] == pytest.approx(0.972, abs=0.01)

    def test_regression_zero_slope(self, stats):
        """Flat line (no relationship)."""
        x = [1, 2, 3, 4, 5]
        y = [5, 5, 5, 5, 5]
        with pytest.raises(ValueError, match="zero variance"):
            stats.linear_regression(x, y)

    def test_regression_negative_slope(self, stats):
        """Negative linear relationship."""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]  # y = -2x + 12
        result = stats.linear_regression(x, y)
        assert result["slope"] == pytest.approx(-2.0)
        assert result["intercept"] == pytest.approx(12.0)
        assert result["r_squared"] == pytest.approx(1.0)

    def test_regression_different_lengths(self, stats):
        with pytest.raises(ValueError, match="Cannot perform regression on data sets with different lengths"):
            stats.linear_regression([1, 2, 3], [1, 2])

    def test_regression_too_few_points(self, stats):
        with pytest.raises(ValueError, match="Cannot perform regression with fewer than 2 data points"):
            stats.linear_regression([1], [2])

    def test_regression_constant_x(self, stats):
        """Constant x should raise ValueError."""
        with pytest.raises(ValueError, match="zero variance"):
            stats.linear_regression([5, 5, 5], [1, 2, 3])


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

    def test_correlation_large_dataset(self, stats):
        """Test correlation on a larger dataset."""
        x = list(range(1, 101))
        y = [2 * v + 3 + (v % 3 - 1) for v in x]  # Nearly perfect linear
        r = stats.pearson_correlation(x, y)
        assert r == pytest.approx(1.0, abs=0.01)

    def test_regression_large_dataset(self, stats):
        """Test regression on a larger dataset."""
        x = list(range(1, 101))
        y = [2 * v + 3 for v in x]
        result = stats.linear_regression(x, y)
        assert result["slope"] == pytest.approx(2.0)
        assert result["intercept"] == pytest.approx(3.0)
        assert result["r_squared"] == pytest.approx(1.0)
