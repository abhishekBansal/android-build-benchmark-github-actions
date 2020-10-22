import csv

def get_result(fileName):
    with open(fileName) as f:
        next(f)  # Skip the header
        reader = csv.reader(f, skipinitialspace=True)
        return dict(reader)

baseResult = getResult('profile-out/benchmark.csv')
mergeResult = getResult('profile-out-merge/benchmark.csv')

baseMean = baseResult['mean']
mergeMean = mergeResult['mean']

buildStr = "Branch Head Build Time: " + mergeMean + " | Base Branch Build Time: " + baseMean
# print result on console and write in a file
print buildStr
with open("benchmark-result.txt", 'w') as f:
    f.write(buildStr)