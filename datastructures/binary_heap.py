class BinaryHeap:

    def __init__(self, nodes):
        if not isinstance(nodes, list):
            raise TypeError('Please provide initial list of nodes as a list')
        self.nodes = nodes
        # create empty list to store our heap
        self.heap = []

        for n in nodes:
            self.push(n)

    def get_size(self):
        return len(self.heap)

    def push(self, node):

        self.heap.insert(len(self.heap), node)
        self.__percolate_up()

    def __percolate_up(self, node_to_percolate=0):

        if node_to_percolate == 0:
            current_node = self.heap.index(self.heap[-1])  # node being percolated
        else:
            current_node = node_to_percolate

        print(f"current node : {current_node}")

        # if its the first element we don't need to percolate
        if len(self.heap) == 1:
            print("nothing to percolate up")
            return

        print("percolating..")
        # Using integer division would be the same as (x -1)/2 which allows us to find the parent node
        parent_index = (current_node // 2)

        parent_value = self.heap[parent_index]

        if self.heap[current_node] > parent_value:
            print("swapping")

            # do the swap
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[current_node]
            self.heap[current_node] = tmp
            # current node takes the index of the parent
            current_node = parent_index
            # swap complete
            print(f"swapped {current_node} to position of {self.heap[parent_index]}")
            return self.__percolate_up(current_node)

    def __percolate_down(self, node_to_percolate=0):

        print("Percolating down")
        current_node = node_to_percolate

        print(f"current node {current_node}")

        if not current_node:
            last_node = self.heap.pop()
            # Move last node to be the first
            self.heap = [last_node] + self.heap

        max_child, child_index = self.__max_child(current_node)

        print(f"child {max_child} , child index: {child_index}")
        if not max_child or not child_index:
            return

        # check if swap is necessary
        if max_child >= self.heap[current_node]:
            # do the swap
            tmp = self.heap[current_node]
            self.heap[current_node] = self.heap[child_index]
            self.heap[child_index] = tmp
            # swap complete
            print(f"swapped {self.heap[child_index]} to position of {self.heap[current_node]}")

            # continue percolating at the child level
            return self.__percolate_down(child_index)

    def __max_child(self, node_index):

        left_child_index = (2 * node_index) + 1
        right_child_index = (2 * node_index) + 2

        try:
            left_child = self.heap[left_child_index]
            right_child = self.heap[right_child_index]

            max_child = max(left_child, right_child)
            if left_child == max_child:
                return max_child, left_child_index

            if right_child == max_child:
                return max_child, right_child_index


        except IndexError:
            # means no children for a node exist
            return None, None

    def print_heap(self):
        print(f"{self.heap}")

    def pop(self):

        result = self.heap.pop(0)
        self.__percolate_down()


        return result
