from functions.get_files_info import get_files_info

test_cases: list[dict[str, str | tuple[str, str]]] = [
    {"case": "current directory", "args": ("calculator", ".")},
    {"case": "pkg", "args": ("calculator", "pkg")},
    {"case": "/bin", "args": ("calculator", "/bin")},
    {"case": "out of bounds", "args": ("calculator", "../")},
    ]

def test(test_cases: list[dict[str, str | tuple[str, str]]]) -> tuple[list[str], list[str]]:
    results: list[str] = []
    cases: list[str] = []
    for test_case in test_cases:
        cases.append(test_case["case"])
        results.append(get_files_info(test_case["args"][0], test_case["args"][1]))
    return cases, results

def main() -> None:
    print("Initialising test cases for get_files_info:")
    print("==============================")
    cases, results = test(test_cases)
    for i in range(0, len(cases)):
        print(f'Running test case for "{cases[i]}":')
        print(results[i])
        print("==============================")
    print("End of test cases.")

main()
