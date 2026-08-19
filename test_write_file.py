from functions.write_file import write_file

test_cases: list[dict[str, str | tuple[str, str, str]]] = [
    {"case": "replace lorem", "args": ("calculator", "lorem.txt", "wait, this isn't lorem ipsum")},
    {"case": "lorem in pkg", "args": ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")},
    {"case": "out of bounds", "args": ("calculator", "/temp/temp.txt", "this should not be allowed")},
    ]

def test(test_cases: list[dict[str, str | tuple[str, str]]]) -> tuple[list[str], list[str]]:
    results: list[str] = []
    cases: list[str] = []
    for test_case in test_cases:
        cases.append(test_case["case"])
        results.append(write_file(test_case["args"][0], test_case["args"][1], test_case["args"][2]))
    return cases, results

def main() -> None:
    print("Initialising test cases for write_file:")
    print("==============================")
    cases, results = test(test_cases)
    for i in range(0, len(cases)):
        print(f'Running test case for "{cases[i]}":')
        print(results[i])
        print("==============================")
    print("End of test cases.")

main()
