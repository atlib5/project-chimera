def test_trend_fetcher_output_structure():
    """
    This test defines the expected output structure
    for the trend fetching agent.
    """

    trend_output = {
        "source": "twitter",
        "trend_name": "AI influencers",
        "timestamp": "2026-02-01T10:00:00Z"
    }

    assert "source" in trend_output
    assert "trend_name" in trend_output
    assert "timestamp" in trend_output
