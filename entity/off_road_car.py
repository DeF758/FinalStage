from entity.auto import Auto


class OffRoadCar(Auto):
    def __init__(self, brand='no brand', model='no model', price=0,
                 drive_unit='four-wheel drive'):
        super().__init__(brand, model, price)
        self.__drive_unit = (drive_unit if isinstance(drive_unit, str)
                                           and len(drive_unit) > 0
                             else "no information")

    @property
    def drive_unit(self):
        return self.__drive_unit

    @drive_unit.setter
    def drive_unit(self, drive_unit):
        if isinstance(drive_unit, str):
            self.__drive_unit = drive_unit

    def __str__(self):
        return (super().__str__()
                + f" (Drive unit - {self.__drive_unit})")
