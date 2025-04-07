from src.product import Product


def test_print_mixin(capsys):
    Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Product, Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5"
