from src.check_stock import check_stock

def test_category_with_no_books():
    assert check_stock(['ABARA 10'],['B']) == '(B : 0)'
    
def test_categories_with_no_books():
    assert check_stock(['ABARA 10'],['B','C']) == '(B : 0) - (C : 0)'