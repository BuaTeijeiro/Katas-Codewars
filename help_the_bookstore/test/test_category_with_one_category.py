from src.check_stock import check_stock

def test_one_category():
    assert check_stock(['ABARA 10'],['A']) == '(A : 10)'