//---------------------------------------------------------
void magic_square(int *m, int n) {
    /* assign 3X3 matrix to following values
     8     1     6
     3     5     7
     4     9     2
     */
    int values[9] = { 8, 1, 6, 3, 5, 7, 4, 9, 2 };
    int i, len = n*n, *p = values;
    for (i = 0; i < len; i++) *m++ = *p++;
}


//---------------------------------------------------------
void display_matrix(int *m, int n) {
    int *p = m, i, j;
    for (i = 0; i < n; i++) {
        printf("\n");
        for (j = 0; j < n; j++) printf("%4d", *p++); 
    }
    printf("\n");
}

//---------------------------------------------------------
int is_magic_square(int *m, int n)
{
    int sumOfRows = 0, sumOfColumns = 0, sumOfDiagonal = 0, sum = 0, isSquare = 1;
    for (int firstRef = 0; firstRef < n; firstRef++)
    {
        for (int secondRef = 0; secondRef < n; secondRef++)
        {
            // calculates major diagonal
            if (firstRef == secondRef)
            { 
                sum += *(m + (firstRef * n) + secondRef);
            }
            // calculates minor diagonal
            if (firstRef + secondRef == n - 1)
            {
                sumOfDiagonal += *(m + (firstRef * n) + secondRef);
            }
        }
    }
    for (int firstRef = 0; firstRef < n; firstRef++)
    {
        sumOfRows = 0; //resets values for row sum and column sum for next iteration in inner loop
        sumOfColumns = 0;
        for (int secondRef = 0; secondRef < n; secondRef++)
        {
            //calculates row sum
            sumOfRows += *(m + (firstRef * n) + secondRef); 
            //calculates count sum
            sumOfColumns += *(m + (secondRef * n) + firstRef); 
        }
        if (sumOfDiagonal != sum)
        {
            return 0;
        } else if (sum != sumOfColumns && sum != sumOfRows)
        { 
            // compares the sum of cols and rows
            return 0;
        }
    }
    return 1;
}

//---------------------------------------------------------
void transpose_matrix(int *m1, int *m2, int n) {
    int row = 0, col = 0, count = 0;
    for (row = 0; row < n; row++)
    {
        for (col = 0; col < n; col++)
        {
            count = *(m1 + (row * n) + col);
            *(m1 + (row * n) + col) = *(m2 + (col * n) + row);
            *(m2 + (col * n) + row) = count;
        }
    }
}

//---------------------------------------------------------
void multiply_matrix(int *m1, int *m2, int *m3, int n)
{
    int first = 0, second = 0, third = 0, sum = 0;

    magic_square(m1, n);
    transpose_matrix(m1, m2, n);

    for (first = 0; first < n; first++)
    {
        for (second = 0; second < n; second++)
        {
            sum = 0;
            for (third = 0; third < n; third++)
            {
                sum += *(m1 + (first * n + third)) * *(m2 + (third * n + second));
            }
            *(m3 + (first * n + second)) = sum;
        }
    }
}