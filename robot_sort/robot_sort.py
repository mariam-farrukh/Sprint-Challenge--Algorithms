class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # RULES:
            # You may use any pre-defined robot methods.
            # You may NOT modify any pre-defined robot methods.
            # You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
            # You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
            # You may use iterators. (`while`, `for`, `break`, `continue`)
            # You may NOT store any variables. (`=`)
            # You may NOT access any instance variables directly. (`self._anything`)
            # You may NOT use any Python libraries or class methods. (`sorted()`, etc.)
            # You may define robot helper methods, as long as they follow all the rules.
        # Type of sorts: (Need best sort for swapping)
            # Selection sort --> Don't think I can used this because can't store any variable
            # Bubble Sort --> Best swapping method, go with this kind of sort for swapping items.
            # Insertion sort --> Doesn't go well with swapping items
        # Pseudocode for Bubble sort:
            # Compare i to i+1 in the item array. If item is smaller, swap, if not, move on.
            # Swaps 'None' with value in the list
            # Note above: Light should be used in this situation for the robot to go through all of the steps. 
            # This means that the light should be used to start and end the movements
            # So the robot must have its light on to start. While the light is on, the starting item None should be swapped.
            # Then the robot will move right if it can move right
            # It will then compare the items and based on constraints above, if compare_it() == 1, then it should swap items.
            # Then the roboto should keep moving left to go back to the beginning until it encounters None.
            # Once there, the robot should swap the item with the starting position again when back at the beginning
            # Check if the robot can go right again. If it can, then repeat the bubble sort, and if it can't then set the lights off and be done.
            # So if it can no longer move right, then the lights should be turned off and everything has been sorted.
        
        self.set_light_on()
        while self.light_is_on():
            # Swap item with None
            if self._item == None:
                self.swap_item()
            # Move to the list to the right
            while self.can_move_right():
                self.move_right()

                # Compare item to item in list. If item is larger than item in list, comparing will return one, so swap the items.
                if self.compare_item() == 1:
                    self.swap_item()
            
            # Move to the left if we don't encounter None
            while self.can_move_left() == True and self.compare_item() is not None:
                self.move_left()
            
            # When back at the starting position, items should be swapped.
            self.swap_item()
            # Check if we can go further to the right (because back at starting position). 
            # If we can't move right, then we've reached the end of the list and that means that everything is sorted and the light can turn off
            if self.can_move_right() is not True:
                self.set_light_off()
            else:
                self.move_right()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)