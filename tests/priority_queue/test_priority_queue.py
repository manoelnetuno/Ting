import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_line = PriorityQueue()

    file1 = {'nome_do_arquivo': 'file1.txt', 'qtd_linhas': 3}
    file2 = {'nome_do_arquivo': 'file2.txt', 'qtd_linhas': 7}
    file3 = {'nome_do_arquivo': 'file3.txt', 'qtd_linhas': 1}

    priority_line.enqueue(file3)
    priority_line.enqueue(file2)
    priority_line.enqueue(file1)

    assert len(priority_line) == 3
    assert len(priority_line.high_priority) == 2
    assert len(priority_line.regular_priority) == 1

    assert priority_line.high_priority.search(0) == file3
    assert priority_line.high_priority.search(1) == file1
    assert priority_line.regular_priority.search(0) == file2

    assert priority_line.search(0) == file3
    assert priority_line.search(1) == file1
    assert priority_line.search(2) == file2

    with pytest.raises(IndexError):
        priority_line.search(5)

    assert priority_line.dequeue() == file3
    assert priority_line.dequeue() == file1
    assert priority_line.dequeue() == file2

    with pytest.raises(IndexError):
        priority_line.dequeue()