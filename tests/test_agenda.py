from agenda import agenda

def test_agenda():
    result = agenda("2023-10-01", "2023-10-31")
    
    assert isinstance(result, list)
    
    assert all(isinstance(item, dict) for item in result)
    
    expected_keys = {'date', 'event', 'location'}
    assert all(expected_keys.issubset(item.keys()) for item in result)
    
    for item in result:
        assert "2023-10-01" <= item['date'] <= "2023-10-31"