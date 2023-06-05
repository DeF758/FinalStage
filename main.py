'''
Car Center
v.1.0
Gerasimchik D.Y.
QA2022
03.06.2023
'''

from entity.sport_car import SportCar
from entity.off_road_car import OffRoadCar
from entity.budget_car import BudgetCar
from container.car_showroom import CarShowroom
from logic.sales_manager import SalesManager
from util.car_creator import CarCreator


def main():
    showroom = CarShowroom()
    sport = SportCar("BMW", "M5", 70000)
    budget = BudgetCar("Ford", "Focus", 3000, 5, 20)
    off_road = OffRoadCar("Lada", "4x4", 2505, "All-wheel drive vehicle")
    showroom.add(sport)
    showroom.add(budget)
    showroom.add(off_road)
    m = SalesManager.car_max_price(showroom)
    n = SalesManager.car_min_price(showroom)
    print(showroom)
    print(f"\nExpensive car: {m}"
          f"\nCheap car: {n}")
    print()

    ls = CarCreator.create(15)
    print(ls)
    mx = SalesManager.car_max_price(ls)
    mn = SalesManager.car_min_price(ls)
    print(f"\nExpensive car: {mx}"
          f"\nCheap car: {mn}")


if __name__ == '__main__':
    main()
