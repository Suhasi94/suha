import pytest

from POM import SearchPage


@pytest.mark.parametrize("gadget", ["mobiles", "books", "computers"])
def test_search(_driver, gadget):
    search_ = SearchPage.SearchPage(_driver)
    search_.enter_search(gadget)
    search_.click_search_btn()
