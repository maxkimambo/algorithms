from unittest import TestCase
import pytest
from datastructures.binary_heap import BinaryHeap


class TestBinaryHeap:


    def test_create_binary_heap(self):

        initial_nodes = [90, 80, 30, 60, 50, 100, 70, 5, 20, 10, 40, 55, 101, 45, 5]
        heap = BinaryHeap(initial_nodes)
        heap.print_heap()
        assert heap is not None

    def test_type_error_creation_binary_heap(self):
        with pytest.raises(TypeError):
            heap = BinaryHeap()



    def test_insert_node(self):
        initial_nodes = [90, 80, 30, 60, 50, 100, 70, 5, 20, 10, 40, 55, 101, 45, 5]
        heap = BinaryHeap(initial_nodes)
        heap.push(102)
        # heap.print_heap()

    def test_remove_node(self):
        initial_nodes = [90, 80, 30, 60, 50, 100, 70, 5, 20, 10, 40, 55, 101, 45, 5]
        heap = BinaryHeap(initial_nodes)
        result = heap.pop()
        heap.print_heap()
        assert result == 101

