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
        # find the parent
        # current_index = self.heap.index(current_node)

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

        # while parent_index > 0:
        #     print(f"Processing parent index {parent_index}")
        #     if self.heap[current_index] > self.heap[parent_index]:
        #
        #
        #         # we have a new current index
        #         current_index = self.heap.index(current_node)
        #         # calculate the new parent
        #         parent_index = current_index // 2

    def print_heap(self):
        print(f"{self.heap}")


    def pop(self):
        # TODO percolation
        result = self.heap.pop(0)
        return result

    @staticmethod
    def add_node(node):
        print(node)
