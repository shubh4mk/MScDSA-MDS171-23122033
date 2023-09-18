matrices = {
    "matrix 1": [],
    "matrix 2": [],
    "result matrix": []
}

def inputElement(matrix_name):
    rows = int(input(f"Enter the number of rows for {matrix_name}: "))
    cols = int(input(f"Enter the number of columns for {matrix_name}: "))
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = input(f"Enter the element at row {i+1}, col {j+1}: ")
            row.append(element)
        matrix.append(row)
    matrices[matrix_name] = matrix

def calculationMatrix():
    matrix1 = matrices["matrix 1"]
    matrix2 = matrices["matrix 2"]
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    
    matrices["result matrix"] = result

def export_to_file():
    with open("23122033_ShubhamKumar.txt", 'w') as file:
        result = matrices["result matrix"]
        for row in result:
            with open('your_file.txt', 'a') as file:
                file.write(' '.join(str(x) for x in row) + '\n')       

while True:
    print("\nMenu:")
    print("1. Enter Matrix 1")
    print("2. Enter Matrix 2")
    print("3. Calculate")
    print("4. Export to File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inputElement("matrix 1")
    elif choice == "2":
        inputElement("matrix 2")
    elif choice == "3":
        calculationMatrix()
        print("Multiplication completed.")
    elif choice == "4":
        export_to_file()
        print("Result exported to file.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
