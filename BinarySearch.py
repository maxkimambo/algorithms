class BinarySearch:

    def __init__(self, values):

        if not isinstance(values, list):
            raise TypeError

        # sorted array of integers
        self.store = values

    def contains(self, num):
        return self.__search(num, self.store)

    def __search(self, num, array_segment):

        mid = self.__midpoint(array_segment)
        mid_value = array_segment[mid]

        if mid_value is 0 or mid_value == len(self.store):
            # value not found
            return False

        if num == mid_value:
            # value found
            return True

        if num < mid_value:
            # continue searching the left side
            segment = array_segment[:mid]
        elif num > mid_value:
            segment = array_segment[mid:]

        return self.__search(num, segment)

    def __midpoint(self, array_segment):
        return len(array_segment) // 2
