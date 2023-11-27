from src.format_bookstore import format_bookstore

def test_format_one_type():
    assert format_bookstore({'A':10},['A']) == '(A : 10)'
    
def test_format_several_types():
    assert format_bookstore({'A':10, 'B':20},['A','B']) == '(A : 10) - (B : 20)'
    
def test_format_several_types_other_order():
    assert format_bookstore({'A':10, 'B':20},['B','A']) == '(B : 20) - (A : 10)'