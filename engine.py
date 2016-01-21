from system import *


class Engine:
    def __init__(self):
        self.results = []
        pass

    def start(self):
        for difficulty in ['easy', 'medium', 'hard']:
            for gangster_number in [2, 5, 8]:
                for civilian_number in [20, 50, 80]:
                    test_number = 10
                    gang_wins = 0
                    day_avrg = 0.0
                    for i in range(test_number):
                        system = System(difficulty, civilian_number, gangster_number)
                        while not system.finished():
                            system.step()
                        if system.gang_exists():
                            gang_wins += 1
                        day_avrg += system.day
                    day_avrg /= 10
                    line_list = [difficulty, str(civilian_number), str(gangster_number), str(gang_wins), str(test_number),
                                 str(day_avrg)]
                    print line_list
                    self.results.append(' '.join(line_list))

    def result(self, file_name):
        result_text = '\n'.join(self.results)
        file1 = open(file_name)
        file1.write(result_text)
