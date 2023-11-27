from src.check_stock import check_stock

def test_one_category_several_books():
    assert check_stock(['ABARA 10', 'ANOSD 15'],['A']) == '(A : 25)'
    
def test_one_category_several_books_and_spam():
    assert check_stock(['ABARA 10', 'ANOSD 15', 'BJSDF 20'],['A']) == '(A : 25)'