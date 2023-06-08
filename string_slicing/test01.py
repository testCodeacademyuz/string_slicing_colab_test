from string_slicing import CheckSolution
from string_slicing import test_cases

task = "taskOne"

class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    
    def test_cases_runner(self):
        results = []
        for test_case in test_cases[task]:
            try:
                answer = self.solution(*test_case["input"]) 
            except:
                answer = "None"
            excepted = test_case["expected"]

            result = {
                "input": map(str, test_case["input"]),
                "answer": answer,
                "expected": excepted,
                "isSolved": answer == excepted
            }
            results.append(result)
        return results
    
    def check(self, solution, tg_username):
        results = self.test_cases_runner()
        isSolved = all([result["isSolved"] for result in results])
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")
