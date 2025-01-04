import threading
class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for i in range(5)]
        self.eat_lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        

        left_fork = philosopher
        right_fork = (philosopher + 1) % 5


        if philosopher == 4:
            first_fork = right_fork
            second_fork = left_fork
            first_pick = pickRightFork
            second_pick = pickLeftFork
            first_put = putRightFork
            second_put = putLeftFork

        else:
            first_fork = left_fork
            second_fork = right_fork
            first_pick = pickLeftFork
            second_pick = pickRightFork
            first_put = putLeftFork
            second_put = putRightFork


        with self.eat_lock:
            with self.forks[first_fork]:
                with self.forks[second_fork]:
                    first_pick()  # Pick the first fork
                    second_pick()  # Pick the second fork
                    eat()  # Eat
                    second_put()  # Put down the second fork
                    first_put()  # Put down the first fork



