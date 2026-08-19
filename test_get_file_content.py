from functions.get_file_content import get_file_content

test_cases: list[dict[str, str | tuple[str, str]]] = [
    {"case": "lorem.txt", "args": ("calculator", "lorem.txt")},
    {"case": "main.py", "args": ("calculator", "main.py")},
    {"case": "calculator.py", "args": ("calculator", "pkg/calculator.py")},
    {"case": "out of bounds", "args": ("calculator", "/bin/cat")},
    {"case": "non-existent file", "args": ("calculator", "pkg/does_not_exist.py")},
    ]

def test(test_cases: list[dict[str, str | tuple[str, str]]]) -> tuple[list[str], list[str]]:
    results: list[str] = []
    cases: list[str] = []
    for test_case in test_cases:
        cases.append(test_case["case"])
        results.append(get_file_content(test_case["args"][0], test_case["args"][1]))
    return cases, results

def main() -> None:
    print("Initialising test cases for get_file_content:")
    print("==============================")
    cases, results = test(test_cases)
    print(f'Running test case for "{cases[0]}":')
    print(f"lorem.txt length: {len(results[0])}")
    print(f"lorem.txt truncated: {'truncated' in results[0]}")
    print("==============================")
    for i in range(1, len(cases)):
        print(f'Running test case for "{cases[i]}":')
        print(results[i])
        print("==============================")
    print("End of test cases.")

main()
