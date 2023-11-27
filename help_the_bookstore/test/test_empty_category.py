from src.check_stock import check_stock

def test_empty_category():
    assert check_stock(['A'],[]) == ''