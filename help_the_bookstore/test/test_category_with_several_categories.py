from src.check_stock import check_stock

def test_several_categories_all_books():
    assert check_stock(['ABARA 10', 'ANOSD 15','BASKS 10', 'AJDNR 30', 'CADJS 10', 'FEKJS 5', 'ANJKF 5', 'FJASD 20', 'TASDF 4'],['A', 'F']) == '(A : 60) - (F : 25)'
    
def test_one_category_all_books_and_some_empty():
    assert check_stock(['ABARA 10', 'ANOSD 15','BASKS 10', 'AJDNR 30', 'CADJS 10', 'FEKJS 5', 'ANJKF 5', 'FJASD 20', 'TASDF 4'],['A', 'F', 'E']) == '(A : 60) - (F : 25) - (E : 0)'
    
def test_one_category_all_books_and_some_empty_different_order():
    assert check_stock(['ABARA 10', 'ANOSD 15','BASKS 10', 'AJDNR 30', 'CADJS 10', 'FEKJS 5', 'ANJKF 5', 'FJASD 20', 'TASDF 4'],['E', 'F', 'A']) == '(E : 0) - (F : 25) - (A : 60)'
