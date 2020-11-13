def get_average(scores):
    sum=0
    for item in scores:
        sum+=item
    return float(sum)/len(scores)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = get_average(student_marks.get(query_name))
    print('{:.2f}'.format(average))
    