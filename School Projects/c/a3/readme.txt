Name: Andrew Liutiev
ID: 180635320
Email: liut5320@mylaurier.ca
WorkID: cp264a3
Statement: I claim that the enclosed submission is my individual work 

Check list, self-evaluation/marking, marking scheme:
Note: fill self-evaluation for each of the following brackets. The field format is [self-evaluation / total marks / marker's evaluation]. For example, you put your self-evaluation, say 2, like [2/2/]. If marker gives different evaluation value say 1, it will show [2/2/1] in the marking report. 

Evaluation: [self-evaluation/total/marker-evaluation]

Q1 
1. array copy and is_sorted functions      [4/4/] 
2. selection sort                          [3/3/]
3. quick sort                              [3/3/]

Q2 
1. is magic square function                [4/4/]
2. matrix transpose                        [2/2/]
3. matrix multiply                         [4/4/]

Q3
1. letter count and lower case             [4/4/]
2. word count                              [3/3/]
3. trim                                    [3/3/]

Total:                                    [30/30/]

Test result:
Q1 output: (copy the screen output of your test run) 
Algorithm correctness testing:
Input array:
  3   1   4   5   2   7   6   9   8
Is sorted:0
Selection sort:
  0   1   2   3   4   5   6   7   9
Is sorted:1
Quick sort:
  1   2   3   4   5   6   7   9   9
Is sorted:1
Algorithm runtime testing:
time_span(selection_sort(2000 numbers) for 10 times): 78.0 (ms)
time_span(quick_sort(2000 numbers) for 1000 times): 266.0 (ms)
time_span(selection_sort(2000 numbers))/time_span(quick_sort(2000 numbers)): 29.3

Q2 output: (copy the screen output of your test run) 

m1:
   8   1   6
   3   5   7
   4   9   2
is_magic_square:1

m1':
   8   3   4
   1   5   9
   6   7   2
is_magic_square:1

m1*m1':
 101  71  53
  71  83  71
  53  71 101
is_magic_square:0

Q3 output: (copy the screen output of your test run) 

Input string: "     This Is    a Test   "
Letter count:11
Word count:4
This Is a Test
After trimming:"This Is a Test"
After lower case:"this is a test"

