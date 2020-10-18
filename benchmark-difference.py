import csv

def get_result(fileName):
    with open(fileName) as f:
        next(f)  # Skip the header
        reader = csv.reader(f, skipinitialspace=True)
        return dict(reader)

headResult = get_result('profile-out/benchmark.csv')
mergeResult = get_result('profile-out-merge/benchmark.csv')

headMean = headResult['mean']
mergeMean = mergeResult['mean']

print "Branch Head Build Time: " + headMean + " | Base Branch Build Time: " + mergeMean



