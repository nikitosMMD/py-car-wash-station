class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = max(1, min(7, comfort_class))
        self.clean_mark = max(1, min(10, clean_mark))
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = max(1.0, min(11.0, distance_from_city_center))
        self.clean_power = max(1.0, min(10.0, clean_power))
        self.average_rating = max(1.0, min(5.0, average_rating))
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        if car.clean_mark >= self.clean_power:
            return 0.0

        price = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, car_list):
        total_income = 0.0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate):
        total_ratings = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)