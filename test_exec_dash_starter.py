from monthly_sales import to_usd
    
def test_to_usd():
    result = to_usd(10)
    assert result =="$10.00"


from monthly_sales import get_top_sellers

def test_get_top_sellers():
    result = top_sellers
    