from functions.run_python_file import run_python_file

test_cases: list[dict[str, object]] = [
    {"case": "calculator instructions", "args": ("calculator", "main.py")},
    {"case": "calculator addition", "args": ("calculator", "main.py", ["5 + 3"])},
    {"case": "run test file", "args": ("calculator", "tests.py")},
    {"case": "out of bounds", "args": ("calculator", "../main.py")},
    {"case": "non-existent", "args": ("calculator", "nonexistent.py")},
    {"case": "non-python", "args": ("calculator", "lorem.txt")},
    ]

def test(test_cases: list[dict[str, object]]) -> tuple[list[str], list[str]]:
    results: list[str] = []
    cases: list[str] = []
    for test_case in test_cases:
        cases.append(test_case["case"])
        if len(test_case["args"]) == 3:
            print(f"arrived with test case {test_case["case"]}")
            results.append(run_python_file(test_case["args"][0], test_case["args"][1], test_case["args"][2]))
        else:
            results.append(run_python_file(test_case["args"][0], test_case["args"][1]))
    return cases, results

def main() -> None:
    print("Initialising test cases for run_python_file:")
    print("==============================")
    cases, results = test(test_cases)
    for i in range(0, len(cases)):
        print(f'Running test case for "{cases[i]}":')
        print(results[i])
        print("==============================")
    print("End of test cases.")

main()
