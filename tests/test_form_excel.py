import pytest
from utils.excel_reader import read_excel
from pages.form_page import FormPage

data = read_excel("data/test_data.xlsx")

@pytest.mark.parametrize("row", data)
def test_form_fill(row, browser_page):
    try:
        form = FormPage(browser_page)
        form.open()

        form.fill_form(
            name=row["name"],
            email=row["email"],
            phone=row["phone"],
            address=row["address"]
        )

        message = form.get_success_message()
        assert "success" in message.lower()

    except Exception as e:
        # Completely swallow the failure
        #print(f"Test failed for row: {row}. Error: {e}")
        pytest.fail(f"Test failed for row={row}: {e}", pytrace=False)
        #pass     # prevents pytest from marking it as failed

