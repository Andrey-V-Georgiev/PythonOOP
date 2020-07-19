import unittest

from Workers import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Pesho', 5, 3)
    """
    Test if the worker is initialized  with correct name, salary and energy
    """
    def test_worker_is_init_with_proper_name(self):
        self.assertEqual(self.worker.name, 'Pesho')

    """
    Test if the  worker 's energy is incremented after the rest method is called
    """
    def test_worker_energy_is_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 4)

    """
    Test if an  error is raised if the  worker  tries  to   work  with negative energy or equal to 0
    """
    def test_worker_with_zero_energy_throws_exception(self):
        no_energy_worker = Worker('Pesho', 5, 0)
        with self.assertRaises(Exception) as context:
            no_energy_worker.work()

    """
    Test if the worker's money is increased by his salary correctly after the work method is called
    """
    def test_worker_salary_is_incremented_after_working(self):
        money_before = self.worker.money
        self.worker.work()
        money_after = self.worker.money
        worker_salary = self.worker.salary
        self.assertEqual(money_before + worker_salary, money_after)

    """
    Test if the  worker's energy is decreased after the work method is called
    """
    def test_worker_energy_is_decreased_after_working(self):
        energy_before = self.worker.energy
        self.worker.work()
        energy_after = self.worker.energy
        self.assertEqual(energy_before - 1, energy_after)

    """
    Test if the get_info method returns the proper string with correct values
    """
    def test_worker_get_info_return_correct_string(self):
        name = self.worker.name
        money = self.worker.money
        self.assertEqual(self.worker.get_info(), f'{name} has saved {money} money.')


if __name__ == '__main__':
    unittest.main()

