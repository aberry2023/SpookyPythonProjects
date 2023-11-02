def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_camry = make_car('toyota', 'camry', color='red')
print(my_camry)
