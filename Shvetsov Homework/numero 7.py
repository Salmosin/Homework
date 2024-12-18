#ввод чисел в матрицы осуществляется с отделением каждой следующей цифрой запятой
#после послдней цифры строки запятая не ставится
class Matrix:
    def __init__(self, filename=None):
        if filename:
            self.data = self.load_from_file(filename)
        else:
            self.data = []  # Пустая матрица по умолчанию

    def load_from_file(self, filename):
        """Загрузка матрицы из файла."""
        matrix = []
        with open(filename, 'r') as file:
            for line in file:
                row = [float(x) for x in line.strip().split(',')]
                matrix.append(row)
        return matrix

    def __add__(self, other):
        """Сложение двух матриц."""
        if isinstance(other, Matrix):
            if self.shape() != other.shape():
                raise ValueError("Матрицы должны быть одинакового размера для сложения.")
            result = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in
                      range(len(self.data))]
            return Matrix.from_data(result)
        else:
            raise ValueError("Сложение возможно только с другой матрицей.")

    def __mul__(self, other):
        """Умножение матрицы на число или другую матрицу."""
        if isinstance(other, Matrix):
            if len(self.data[0]) != len(other.data):
                raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(len(other.data)))
                       for j in range(len(other.data[0]))] for i in range(len(self.data))]
            return Matrix.from_data(result)
        elif isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))]
            return Matrix.from_data(result)
        else:
            raise ValueError("Умножение возможно только с числом или другой матрицей.")

    def transpose(self):
        """Транспонирование матрицы."""
        result = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        return Matrix.from_data(result)

    def determinant(self):
        """Вычисление определителя матрицы (только для квадратных)."""
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Определитель можно вычислить только для квадратной матрицы.")
        return self._det_recursive(self.data)

    def _det_recursive(self, matrix):
        """Рекурсивный расчет определителя матрицы."""
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for c in range(len(matrix)):
            minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._det_recursive(minor)
        return det

    def save_to_file(self, filename):
        """Сохранение матрицы в файл."""
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(','.join(map(str, row)) + '\n')

    def shape(self):
        """Возвращает размеры матрицы."""
        return len(self.data), len(self.data[0]) if self.data else (0, 0)

    @classmethod
    def from_data(cls, data):
        """Создает матрицу из списка данных."""
        instance = cls()
        instance.data = data
        return instance

    def __str__(self):
        """Строковое представление матрицы."""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


# Пример использования
if __name__ == "__main__":
    # Пример использования класса
    matrix1 = Matrix("matrix1.txt")
    matrix2 = Matrix("matrix2.txt")

    # Сложение матриц
    matrix_sum = matrix1 + matrix2
    print("Сумма матриц:")
    matrix_sum.save_to_file('out')
    print(matrix_sum)

    # Умножение матрицы на число
    scalar_multiplication = matrix1 * 2
    print("Умножение матрицы1 на 2:")
    print(scalar_multiplication)

    # Умножение двух матриц
    matrix_multiplication = matrix1 * matrix2
    print("Умножение матрицы1 на матрицу2:")
    print(matrix_multiplication)

    print("транспонирование:")
    print(matrix_sum.transpose())