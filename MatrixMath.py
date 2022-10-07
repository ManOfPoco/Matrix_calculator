# import math
from fractions import Fraction


class MatrixOperation:
    def __init__(self, lst) -> None:
        self.lst = lst

    @staticmethod
    def separator():
        print("----------------------")

    def __add__(self, other):
        new_lst = []
        if isinstance(other, MatrixOperation):
            for i in range(len(self.lst)):
                matr = []
                for j in range(len(self.lst[i])):
                    print(f'{self.lst[i][j]} + {other.lst[i][j]} = {self.lst[i][j] + other.lst[i][j]}')
                    matr.append(self.lst[i][j] + other.lst[i][j])
                new_lst.append(matr)
            self.separator()
            return MatrixOperation(new_lst)
        self.separator()
        new_lst = [[lst[i] + other for i in range(len(self.lst[0]))] for lst in self.lst]
        print(new_lst)
        return MatrixOperation(new_lst)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        new_lst = []
        if isinstance(other, MatrixOperation):
            for i in range(len(self.lst)):
                matr = []
                for j in range(len(self.lst[i])):
                    print(f'{self.lst[i][j]} - {other.lst[i][j]} = {self.lst[i][j] - other.lst[i][j]}')
                    matr.append(self.lst[i][j] - other.lst[i][j])
                new_lst.append(matr)
            self.separator()
            return MatrixOperation(new_lst)
        self.separator()
        new_lst = [[lst[i] - other for i in range(len(self.lst[0]))] for lst in self.lst]
        print(new_lst)
        return MatrixOperation(new_lst)

    def __rsub__(self, other):
        return self - other

    def inequality(self, other):
        return (2 * self) - other

    def __mul__(self, other):
        new_lst = []
        if isinstance(other, MatrixOperation):
            for i in range(len(self.lst)):

                if len(self.lst[1]) != len(other.lst) and self.lst is not other.lst:
                    return self.inequality(other)
                matr = [0 for _ in range(len(other.lst[0]))]
                calculations = []

                for j in range(len(self.lst[i])):
                    for k in range(len(other.lst[0])):
                        calculations.append(f"{self.lst[i][j]} * {other.lst[j][k]}")
                        # print(
                        #     f"Элемент номер {k}: {self.lst[i][j]} * {other.lst[j][k]} = {self.lst[i][j] * other.lst[j][k]}")
                        matr[k] += self.lst[i][j] * other.lst[j][k]

                # show the actions
                for calc in range(len(other.lst[0])):
                    print(end="| ")
                    for cal in range(calc, len(calculations), len(other.lst[0])):
                        print(calculations[cal], end=" + ")
                    print(end="|    ")
                print(matr)
                new_lst.append(matr)

            print(f"\nНовая матрица: \n{new_lst}")
            self.separator()
            return MatrixOperation(new_lst)

        self.separator()
        new_lst = [[lst[i] * other for i in range(len(self.lst[0]))] for lst in self.lst]
        print(new_lst)
        return MatrixOperation(new_lst)

    def __rmul__(self, other):
        return self * other

    def transportation(self):
        new_matrix = []
        for i in range(len(self.lst)):
            matrix = []
            for j in range(len(self.lst)):
                matrix.append(self.lst[j][i])
            new_matrix.append(matrix)
        return MatrixOperation(new_matrix)

    def __eq__(self, other) -> bool:
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                if self.lst[i][j] != other.lst[i][j]:
                    return False
        return True

    def __pow__(self, other):
        return self * self

    def determinant_2order(self):
        second_order = self.lst[0][0] * self.lst[1][1] - \
                       self.lst[0][1] * self.lst[1][0]

        print(f"{self.lst[0][0]} * {self.lst[1][1]} - {self.lst[0][1]} * {self.lst[1][0]} = {second_order}")
        return MatrixOperation(second_order)

    def determinant_3order(self):

        first_part = self.lst[0][0] * self.lst[1][1] * self.lst[2][2] + \
                     self.lst[0][1] * self.lst[1][2] * self.lst[2][0] + \
                     self.lst[0][2] * self.lst[1][0] * self.lst[2][1]
        print(
            f"({self.lst[0][0]} * {self.lst[1][1]} * {self.lst[2][2]}) + ({self.lst[0][1]} * {self.lst[1][2]} * {self.lst[2][0]}) + ({self.lst[0][2]} * {self.lst[1][0]} * {self.lst[2][1]})",
            end="")

        second_part = first_part - self.lst[0][2] * self.lst[1][1] * self.lst[2][0] - \
                      self.lst[0][0] * self.lst[1][2] * self.lst[2][1] - \
                      self.lst[0][1] * self.lst[1][0] * self.lst[2][2]
        print(
            f" - ({self.lst[0][2]} * {self.lst[1][1]} * {self.lst[2][0]}) - ({self.lst[0][0]} * {self.lst[1][2]} * {self.lst[2][1]}) - ({self.lst[0][1]} * {self.lst[1][0]} * {self.lst[2][2]})",
            end="")
        print(
            f" = {self.lst[0][0] * self.lst[1][1] * self.lst[2][2]} + {self.lst[0][1] * self.lst[1][2] * self.lst[2][0]} + {self.lst[0][2] * self.lst[1][0] * self.lst[2][1]} - {self.lst[0][2] * self.lst[1][1] * self.lst[2][0]} - {self.lst[0][0] * self.lst[1][2] * self.lst[2][1]} - {self.lst[0][1] * self.lst[1][0] * self.lst[2][2]} = {second_part}")
        return MatrixOperation(second_part)

    def determinant_principle_diagonal(self):
        for i in range(len(self.lst)):
            print(self.lst[i], self.lst[i][:2])

        return self.determinant_3order()

    def find_method_to_determination(self):
        if len(self.lst) == 2:
            determin = self.determinant_2order()
        elif len(self.lst) == 3:
            determin = self.determinant_3order()
        else:
            determin = self.laplas_formula()

        return determin

    def find_minor(self, element):
        if not isinstance(element, str):
            raise ValueError("Елемент должен быть строкой")

        if (-1) ** (int(element[0]) + int(element[1])) == -1:
            print(f"(-1) ^ ({int(element[0])} + {int(element[1])}) = ", end="")
            return -1
        print(f"(-1) ^ ({int(element[0])} + {int(element[1])}) = ", end="")
        return 1

    def algebra_addition_element(self, element):
        new_matrix = []
        for i in range(len(self.lst)):
            matrix = []
            if i == int(element[0]) - 1:
                continue
            for j in range(len(self.lst)):
                if j == int(element[1]) - 1:
                    continue
                matrix.append(self.lst[i][j])
            new_matrix.append(matrix)
        print(new_matrix)

        if len(new_matrix) == 1:
            minor = MatrixOperation(new_matrix[0][0])
        elif len(new_matrix) == 2:
            minor = MatrixOperation(new_matrix).determinant_2order()
        elif len(new_matrix) == 3:
            minor = MatrixOperation(new_matrix).determinant_3order()
        return MatrixOperation(minor.lst)

    def laplas_formula(self):
        new_matrix = []
        ln = len(self.lst)
        for i in range(ln):
            find_part_element = self.algebra_addition_element(str(ln) + str(i + 1)).lst
            find_minor = self.find_minor(str(ln) + str(i + 1))

            new_matrix.append((self.lst[ln - 1][i] * find_minor * \
                               find_part_element))

            res_of_multiply = self.lst[ln - 1][i] * find_minor
            print(f"{self.lst[ln - 1][i]} * {find_minor} = {res_of_multiply}")
            print()
            print(f"{find_part_element} * {res_of_multiply} = {new_matrix[i]}")
            self.separator()
        for i in new_matrix:
            print(i, end=" ")
        print("=", sum(new_matrix))
        print()
        return MatrixOperation(sum(new_matrix))

    def reverse_matrix(self) -> list:
        print("1)Find the determinant det A:\n")
        determin = self.find_method_to_determination()

        if determin.lst == 0:
            raise ValueError("Determinant mustn't be equal to 0")
        self.separator()

        print("2)Find algebraic additions:\n")
        new_matrix = []
        for i in range(len(self.lst)):
            matrix_row = []
            for j in range(len(self.lst[i])):
                element = str(i + 1) + str(j + 1)
                print(f"For element A{element} -> {self.lst[i][j]}:")
                particular_element = self.algebra_addition_element(element).lst
                minor_part_element = self.find_minor(element)
                matrix_row.append(particular_element * minor_part_element)

                print(f"{particular_element} * {minor_part_element} = {particular_element * minor_part_element}")
                print()
            new_matrix.append(matrix_row)
        self.separator()

        print(f"3)Creating new matrix:\n{new_matrix}\n")
        new_matrix = MatrixOperation(new_matrix)
        self.separator()

        print(f"4)Transportain matrix:\n")
        new_matrix = new_matrix.transportation()
        print(f"Matrix after transportation:\n{new_matrix.lst}\n")
        self.separator()

        print(f"Find reverse matrix by divide our matrix to determin from paragraph 1 -> it's {determin.lst}:\n")
        reverse_matrix_to_show = []
        reverse_matrix_non_divided = []
        new_matrix = new_matrix.lst

        for i in range(len(new_matrix)):
            matrix_row_to_show = []
            matrix_row_non_divided = []
            for j in range(len(new_matrix[i])):
                matrix_row_to_show.append(f"{Fraction(new_matrix[i][j], determin.lst)}")
                matrix_row_non_divided.append(Fraction(new_matrix[i][j], determin.lst))

            reverse_matrix_to_show.append(matrix_row_to_show)
            reverse_matrix_non_divided.append(matrix_row_non_divided)

        print(reverse_matrix_to_show)
        print()
        return MatrixOperation(reverse_matrix_non_divided)

    def determine_second_minor(self, level: int) -> list:
        minor = []

        for i in range(2):
            minor.append(self.lst[i][level:level + 2])

        if len(minor[0]) != 2:
            minor = []
            level -= 3
            for i in range(2):
                minor.append(self.lst[i + 1][level:level + 2])

        print(minor)
        return minor

    def determine_third_minor(self, position: int, iteration_number: int) -> list:
        minor = []
        for i in range(3):
            res = []
            if iteration_number < position:
                res.append(self.lst[i][iteration_number])
                res.extend(self.lst[i][position:position + 2])
                minor.append(res)
            elif iteration_number >= position:
                if iteration_number + 2 < len(self.lst[0]):
                    res.append(self.lst[i][position:position + 2] + [self.lst[i][iteration_number + 2]])
                    minor.append(*res)
                else:
                    if i <= 1:
                        res.append(self.lst[i][position:position + 2] + [self.lst[i][iteration_number]])
                        minor.append(*res)
                    else:
                        res.append(self.lst[i + 1][position:position + 2] + [self.lst[i + 1][iteration_number]])
                        minor.append(*res)
        self.separator()
        print()
        print(minor)
        return minor

    def determine_fourth_minor(self, position: int, iteration_number: int) -> list:
        minor = []
        for i in range(4):
            res = []
            if iteration_number < position:
                res.append(self.lst[i][iteration_number])
                res.extend(self.lst[i][position:position + 3])
                minor.append(res)
            elif iteration_number >= position:
                res.append(self.lst[i][position:position + 3] + [self.lst[i][iteration_number + 3]])
                minor.append(*res)
        print()
        print(minor)
        return minor

    def bypass_minors_method(self):
        second_order_minor, rang_A = self.determine_second_minor(0), 0

        minor = MatrixOperation(second_order_minor).determinant_2order()

        if minor.lst != 0:
            position = 0
            print("Minor not equal to 0 that is:", minor.lst)
        else:
            for i in range(1, (len(self.lst[0]) - 1) * (len(self.lst) - 1) + 1):
                print("Minor equal to zero\n")
                second_order_minor = self.determine_second_minor(i)
                minor = MatrixOperation(second_order_minor).determinant_2order()
                if minor.lst != 0:
                    print(f"Minor not equal to 0 that is: {minor.lst}\n")
                    position = i
                    break
            else:
                print("Rang of the matrix equal 0")
                return MatrixOperation(rang_A)

        print("Determine 3order minors:\n")
        print("Rang of the matrix >= 2")
        rang_A = 2

        if len(self.lst[0]) > len(self.lst):
            count_of_iteration = len(self.lst[0]) - 2
        elif len(self.lst) == len(self.lst[0]):
            count_of_iteration = len(self.lst)
        # elif len(self.lst[0]) < len(self.lst):
        #     count_of_iteration = len(self.lst) - 2

        for i in range(count_of_iteration):
            third_order_minor = self.determine_third_minor(position, i)
            minor = MatrixOperation(third_order_minor).determinant_3order()
            if minor.lst != 0:
                print("Minor is not equal to zero so rang equal 3")
                rang_A = 3
                break

        print()

        if rang_A == 3:
            if len(self.lst) > 3:
                print(self.separator())
                print("We can also find fourth minors:\n")
                for i in range(len(self.lst[0]) - len(self.lst) + 1):
                    fourth_order_minor = self.determine_fourth_minor(position, i)
                    minor = MatrixOperation(fourth_order_minor).laplas_formula()
                    if minor.lst != 0:
                        print("Minor is not equal to zero", end=" ")
                        rang_A = 4
                        break
            else:
                print("There is no other minors")
        print("Rang is", rang_A)
        return MatrixOperation(rang_A)

    def matrix_method(self, results):
        print(f"A = {self.lst}")
        print(f"1.Find the reverse matrix: ")
        reverse_matrix = self.reverse_matrix()
        print(f"2.Solve the system of equations: \n",
              f"Multiply reverse matrix by results: \n")

        j = 0
        for i in range(len(reverse_matrix.lst)):
            print(f"{reverse_matrix.lst[i]}   {results.lst[j]}")
            j += 1
        print()
        new_matrix = reverse_matrix * results
        return MatrixOperation(new_matrix)

    def change_matrix(self, col, change_values):
        new_matrix = []
        for i in range(len(self.lst)):
            matrix = []
            for j in range(len(self.lst[i])):
                if j == col:
                    matrix.append(change_values.lst[i][0])
                    continue
                matrix.append(self.lst[i][j])
            new_matrix.append(matrix)
        return MatrixOperation(new_matrix)

    def cramers_rule(self, results):
        print(f"A = {self.lst}")
        print(f"1.Find the determinant: \n△ = ", end="")

        first_determin = self.find_method_to_determination()
        print()
        if first_determin.lst == 0:
            raise ValueError(f"The determinant equals to 0 so there is no solutions")

        solve_system_equals = {f"x{i + 1}": 0 for i in range(len(self.lst))}
        for i in range(len(self.lst)):
            new_matrix = self.change_matrix(i, results)
            print(f"△{i+1} = ", end="")
            print(f"{new_matrix.lst} = ", end="")
            determin = new_matrix.find_method_to_determination()
            print(f"x{i+1} = {determin.lst} / {first_determin.lst} = {Fraction(determin.lst, first_determin.lst)}")
            print()
            # delete if needed
            solve_system_equals[f"x{i + 1}"] = f"{Fraction(determin.lst, first_determin.lst)}"
            # if need be uncomment
            # solve_system_equals[f"x{i + 1}"] = Fraction(determin.lst, first_determin.lst)}
        print(solve_system_equals)
        return MatrixOperation(solve_system_equals)


a = MatrixOperation([[4, -3, -2],
                     [2, 5, 3],
                     [6, -3, 5]])

b = MatrixOperation([[9],
                     [-7],
                     [5]])

d = MatrixOperation([[1, 2, 3],
                     [1, 2, 3],
                     [1, 2, 3]])

e = MatrixOperation([[-1, 5, 1, 14],
                     [2, 3, -4, 20],
                     [1, -2, 3, 6],
                     [3, -2, -5, 6]])

q = a.matrix_method(b)
# print(q.lst)
