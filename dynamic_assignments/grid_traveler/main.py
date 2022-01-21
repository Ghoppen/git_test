class GridTraveller(object):

    calculated_number_of_roads = {(1, 1): 1}

    def __get_calculated_road(self, rows_columns: tuple) -> int:
        if rows_columns in self.calculated_number_of_roads.keys():
            return self.calculated_number_of_roads[rows_columns]

    def find_amount_of_ways(self, grid_rows: int, grid_columns: int) -> int:
        rows_columns = (grid_rows, grid_columns)
        calculated_road = self.__get_calculated_road(rows_columns)
        if not all(rows_columns):
            return 0
        elif calculated_road is not None:
            return calculated_road
        else:
            self.calculated_number_of_roads[rows_columns] = self.find_amount_of_ways(
                grid_rows - 1, grid_columns
            ) + self.find_amount_of_ways(grid_rows, grid_columns - 1)
            return self.calculated_number_of_roads[rows_columns]


traveller = GridTraveller()
ways = traveller.find_amount_of_ways(3, 3)

print(ways)
