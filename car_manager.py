from car import Car
import random
import turtle

#COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_TYPES = [["BlueCarRight.gif", "BrightGreenCarRight.gif", "DarkBlueCarRight.gif", "GreenCarRight.gif",
              "BMW-Z4Right.gif"],
             ["BlueCarLeft.gif", "BrightGreenCarLeft.gif", "DarkBlueCarLeft.gif", "GreenCarLeft.gif", "BMW-Z4Left.gif"]]
STARTING_POSITIONS = [(0, (-350, -205)), (0, (-350, -145)), (0, (-350, -80)), (180, (350, 80)), (180, (350, 145)),
                      (180, (350, 205))]
BASE_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.lanes = [0, 1, 2, 3, 4, 5]
        self.last_lane = -1
        for car_shape_list in CAR_TYPES:
            for car_shape in car_shape_list:
                car_shape = 'graphics/' + car_shape
                turtle.register_shape(car_shape)

    def create_car(self):
        # Make sure we do not get 2 cars in a row in the same lane.
        if len(self.lanes) == 0:
            self.lanes = [0, 1, 2, 3, 4, 5]
        lane = random.choice(self.lanes)
        while lane == self.last_lane:
            lane = random.choice(self.lanes)
        self.lanes.remove(lane)
        self.last_lane = lane

        # Set up the car
        starting_info = STARTING_POSITIONS[lane]
        #get the car type by using the first index in starting info into CAR_TYPE.
        #index = 0 if starting_info[0] == else 1
        shape = random.choice(CAR_TYPES[starting_info[0] // 180]) # added floor division
        shape = 'graphics/' + shape

        # create and add a car
        car = Car(shape, starting_info[1], starting_info[0], BASE_MOVE_DISTANCE + random.randint(-1, 5))
        self.cars.append(car)   #(Car(shape, starting_info[1], starting_info[0], BASE_MOVE_DISTANCE + random.randint(-1, 5)))

    def update_cars(self):
        # remove cars that are off the road
        self.cars = [car for car in self.cars if (car.heading() == 0 and car.xcor() < 350) or
                     (car.heading() == 180 and car.xcor() > -350)]
        # iterate over cars and move the ones still in the list
        for car in self.cars:
            car.move()

    def is_collision(self, other):
        # Get a rectangle around other (the player)
        other_top_edge = other.ycor() + 12
        other_bottom_edge = other.ycor() - 12
        other_left_edge = other.xcor() - 12
        other_right_edge = other.xcor() + 12

        # check each car to see if the distance between the edges overlap
        for car in self.cars:
            car_top_edge = car.ycor() + 11
            car_bottom_edge = car.ycor() - 11
            car_left_edge = car.xcor() - 20
            car_right_edge = car.xcor() + 20
            if (
                    (
                         (other_top_edge - car_bottom_edge > 0 and car_top_edge - other_top_edge > 0) or
                         (car_top_edge - other_bottom_edge > 0 and other_bottom_edge - car_bottom_edge > 0)
                    ) and
                    (
                            (other_left_edge - car_left_edge > 0 and car_right_edge - other_left_edge > 0) or
                            (other_right_edge - car_left_edge > 0 and car_right_edge - other_right_edge > 0)
                    )
            ):
                return True

        return False

