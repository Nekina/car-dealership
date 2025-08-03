from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "year_est":1933},
        {"name":"Mercedes", "description":"Great cars. German technology", "year_est":1926},
        {"name":"Audi", "description":"Great cars. German technology", "year_est":1909},
        {"name":"Kia", "description":"Great cars. Korean technology", "year_est":1944},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "year_est":1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], year_est=data['year_est']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        # NISSAN
        {"name": "Pathfinder", "car_type": "suv", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "car_type": "suv", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "car_type": "suv", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "370Z", "car_type": "coupe", "year": 2022, "car_make": car_make_instances[0]},
        {"name": "Navara", "car_type": "pickup", "year": 2021, "car_make": car_make_instances[0]},

        # Mercedes
        {"name": "A-Class", "car_type": "hatchback", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "GLA", "car_type": "crossover", "year": 2022, "car_make": car_make_instances[1]},
        {"name": "SL-Class", "car_type": "convertible", "year": 2021, "car_make": car_make_instances[1]},

        # Audi
        {"name": "A4", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "car_type": "coupe", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Q5", "car_type": "suv", "year": 2022, "car_make": car_make_instances[2]},
        {"name": "TT", "car_type": "convertible", "year": 2020, "car_make": car_make_instances[2]},

        # Kia
        {"name": "Sorrento", "car_type": "suv", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Carnival", "car_type": "minivan", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cerato", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Stinger", "car_type": "coupe", "year": 2022, "car_make": car_make_instances[3]},
        {"name": "Seltos", "car_type": "crossover", "year": 2023, "car_make": car_make_instances[3]},

        # Toyota
        {"name": "Corolla", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Camry", "car_type": "sedan", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Kluger", "car_type": "suv", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Hilux", "car_type": "pickup", "year": 2021, "car_make": car_make_instances[4]},
        {"name": "Supra", "car_type": "coupe", "year": 2020, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], car_type=data['car_type'], year=data['year'])