def test_skill_generate_content_interface():
    """
    This test defines the expected interface
    for the content generation skill.
    """

    input_payload = {
        "trend_name": "AI influencers",
        "platform": "twitter",
        "tone": "informative"
    }

    assert "trend_name" in input_payload
    assert "platform" in input_payload
    assert "tone" in input_payload
