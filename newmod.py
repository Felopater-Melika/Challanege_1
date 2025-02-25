import os


def create_module_structure():
    module_number = int(input("Enter module number: "))
    num_exercises = int(input("Enter number of exercises: "))

    module_folder = f"{module_number}"
    challenge_folder = os.path.join(module_folder, f"Challenge_{module_number}")
    os.makedirs(challenge_folder, exist_ok=True)

    main_py_path = os.path.join(challenge_folder, "main.py")
    with open(main_py_path, "w") as f:
        f.write("# Main script for Challenge {module_number}\n")

    for i in range(1, num_exercises + 1):
        exercise_folder = os.path.join(module_folder, f"ex-{module_number}-{i}")
        os.makedirs(exercise_folder, exist_ok=True)

        exercise_main_py = os.path.join(exercise_folder, "main.py")
        with open(exercise_main_py, "w") as f:
            f.write(f"# Main script for exercise {module_number}-{i}\n")

    print(f"Module {module_number} structure created successfully.")


if __name__ == "__main__":
    create_module_structure()