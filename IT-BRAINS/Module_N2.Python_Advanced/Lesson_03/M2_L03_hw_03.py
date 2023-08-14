# Module 2, Lecture 3, Homework 3
# Develop a Vehicle class to represent a means of transportation.
# Add attributes such as name, speed, and cost. Implement the __gt__ method
# that compares two vehicles based on their speed.
# Create a list of vehicles and sort it by speed.

class Vehicle:
    """
    Represents a means of transportation.
    """

    def __init__(self, name, speed, cost):
        # Initializes a Vehicle object with the given name, speed, and cost.
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        """
        Compares two Vehicle objects based on their speed.

        Args:
            other (Vehicle): The other Vehicle object to compare.

        Returns:
            bool: True if the current Vehicle object has a higher speed than the other Vehicle, False otherwise.
        """
        return self.speed > other.speed

    def __lt__(self, other):
        """
        Compares two Vehicle objects based on their speed.

        Args:
            other (Vehicle): The other Vehicle object to compare.

        Returns:
            bool: True if the current Vehicle object has a lower speed than the other Vehicle, False otherwise.
        """
        return self.speed < other.speed

    def __repr__(self):
        """
        Returns a string representation of the Vehicle object.

        Returns:
            str: A string representation of the Vehicle object.
        """
        return f"Vehicle(name='{self.name}', speed={self.speed}, cost={self.cost})"


lk_bmw_x5 = Vehicle(name="bmw_x5", speed=250, cost=86000)
lk_audi_q7 = Vehicle(name="audi_q7", speed=225, cost=81000)
lk_opel_insignia = Vehicle(name="opel_insignia", speed=230, cost=20000)
lk_nissan_tiida = Vehicle(name="nissan_tiida", speed=199, cost=23000)
lk_toyota_rav4 = Vehicle(name="toyota_rav4", speed=180, cost=86000)

vehicles = [lk_bmw_x5, lk_audi_q7, lk_opel_insignia, lk_nissan_tiida, lk_toyota_rav4]

# sorted_vehicles = sorted(vehicles, key=lambda s: s.speed)
sorted_vehicles = sorted(vehicles)


for vehicle in sorted_vehicles:
    print(vehicle)

