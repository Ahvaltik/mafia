import NSAagent
import agent
import random
from NSAModule import Exists
from NSAModule import Before
from NSAModule import Less
from NSAModule import Predicate
import TestDifficultyManager
from multiprocessing import Process

__author__ = 'Pawel'


class Transaction:
    def __init__(self, civilian, resource, amount):
        self.civilian = civilian
        self.resource = resource
        self.amount = amount


class System:
    def __init__(self, difficulty='easy', civilians_number=20, gangsters_number=2):
        self.day = 0
        self.agents = []
        self.gangsters = []
        self.resources = {}
        self.current_transaction = []
        self.list_of_names = map(lambda x: 'a' + str(x), range(civilians_number + gangsters_number))

        elements = {
            "possible_predicate_names":
                ["is", "killed", "nightKilled", "voted", "day", "resource"],
            "possible_predicates_args":
                self.list_of_names,
            "predicates_data": {
                "nightKilled": {
                    "amount_of_args": 1
                },
                "killed": {
                    "amount_of_args": 1
                },
                "is": {
                    "amount_of_args": 1
                },
                "day": {
                    "amount_of_args": 1
                },
                "resource": {
                    "amount_of_args": 3
                }
            },
            "rule_elements_factories":
                [Exists.Exists(), Before.Before(), Less.Less()]
        }
        test_difficulty_manager = TestDifficultyManager.TestDifficultyManager(self, elements, difficulty)
        for i in range(civilians_number):
            self.agents.append(test_difficulty_manager.createNSACivilian(int(2.5*(civilians_number+gangsters_number))))
        for i in range(gangsters_number):
            self.gangsters.append(test_difficulty_manager.createGangster())
        self.agents.extend(self.gangsters)
        self.agents = random.sample(self.agents, len(self.agents))

    def add_resource(self, civilian, resource_name, number):
        if resource_name in self.resources.keys():
            self.resources[resource_name] += number
        else:
            self.resources[resource_name] = number
        self.current_transaction.append(Transaction(civilian, resource_name, number))

    def substract_resource(self, civilian, resource_name, number):
        if resource_name not in self.resources.keys():
            self.current_transaction.append(Transaction(civilian, resource_name, 0))
            return 0
        if self.resources[resource_name] < number:
            result = number - self.resources[resource_name]
            self.resources[resource_name] = 0
            self.current_transaction.append(Transaction(civilian, resource_name, -result))
            return result
        self.resources[resource_name] -= number
        self.current_transaction.append(Transaction(civilian, resource_name, -number))
        return number

    def __create_poll(self):
        vote = {}
        results = {}
        max_votes = 0
        best_candidate = None
        for civilian in self.agents:
            vote[civilian] = civilian.vote()
            if vote[civilian] not in results.keys():
                results[vote[civilian]] = 0
            results[vote[civilian]] += 1
            if results[vote[civilian]] > max_votes:
                max_votes = results[vote[civilian]]
                best_candidate = vote[civilian]
        if best_candidate:
            self.agents.remove(best_candidate)
            if not best_candidate.civilian:
                self.gangsters.remove(best_candidate)
            best_candidate.execute()
            # self.deadmen.append(best_candidate)
            # self.polls.append(vote)
        self.hanged = best_candidate
        self.last_poll = vote

    def __create_night_poll(self):
        vote = {}
        results = {}
        max_votes = 0
        best_candidate = None
        for gangster in self.gangsters:
            vote[gangster] = gangster.vote()
            if vote[gangster] not in results.keys():
                results[vote[gangster]] = 0
            results[vote[gangster]] += 1
            if results[vote[gangster]] > max_votes:
                max_votes = results[vote[gangster]]
                best_candidate = vote[gangster]
        if best_candidate:
            self.agents.remove(best_candidate)
            best_candidate.execute()
            # self.deadmen.append(best_candidate)
            # self.night_polls.append(vote)
        self.murdered = best_candidate

    def step(self):
        # print str(len(self.gangsters)) + "/" + str(len(self.agents))
        self.current_transaction = []
        predicates = [Predicate.Predicate('day', [str(self.day)])]
        self.__night_step()
        self.__create_night_poll()
        if not self.murdered is None:
            predicates.append(Predicate.Predicate('nightKilled', [self.murdered.name]))
        self.__day_step()
        self.__create_poll()
        # self.transactions.append(self.current_transaction)
        for transaction in self.current_transaction:
            predicates.append(Predicate.Predicate('resource', [transaction.civilian.name, transaction.resource,
                                                               str(transaction.amount)]))
        for elector in self.last_poll.keys():
            chosen = self.last_poll[elector]
            if chosen is not None:
                predicates.append(Predicate.Predicate('voted', [elector.name, chosen.name]))
        if self.hanged is not None:
            predicates.append(Predicate.Predicate('killed', [self.hanged.name]))
        # print map(lambda x: str(x), predicates)
        for civilian in self.agents:
            civilian.acknowledge(predicates)
        self.day += 1

    def __day_step(self):
        for civilian in self.agents:
            civilian.step()

    def __night_step(self):
        for gangster in self.gangsters:
            gangster.night_step()

    def finished(self):
        return 2 * len(self.gangsters) > len(self.agents) or len(self.gangsters) == 0

    def gang_exists(self):
        return len(self.gangsters) > 0
