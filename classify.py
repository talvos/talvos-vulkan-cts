import os
import sys

PASS  = open('PASS', 'w')
FAIL  = open('FAIL', 'w')
NOSUPPORT  = open('NOSUPPORT', 'w')
WARN  = open('WARN', 'w')
CRASH  = open('CRASH', 'w')

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print 'Usage: python classify.py CASEFILE [deqp-vk]'
    exit(1)

CASEFILE = sys.argv[1]
CASES = open(CASEFILE, 'r').readlines()

DEQP = 'deqp-vk'
if len(sys.argv) > 2:
    DEQP = sys.argv[2]

n = 0
passed = 0
failed = 0
crashed = 0
warned = 0
nosupport = 0
total = len(CASES)

passes = []

while n < total:

    # Prepare the next 1000 tests
    with open('TMP', 'w') as TMP:
        for line in CASES[n:n+1000]:
            TMP.write(line)

    ret = os.system('/bin/bash -c ' + \
                    '"(' + DEQP + ' --deqp-caselist-file=$PWD/TMP --deqp-crashhandler=enable || false) >OUTPUT 2>ERROR"')

    RESULTS = open('TestResults.qpa', 'r').read()
    pos = 0
    while True:
        tstart = RESULTS.find('<TestCaseResult', pos)
        if tstart < 0:
            break

        nstart = RESULTS.find('CasePath="', tstart)
        nstart += 10
        nend = RESULTS.find('"', nstart)
        name = RESULTS[nstart:nend]

        n += 1

        rstart = RESULTS.find('<Result StatusCode="', nend)
        if rstart < 0:
            CRASH.write(name + '\n')
            CRASH.flush()
            crashed += 1
            break

        rstart += 20
        rend = RESULTS.find('">', rstart)
        status = RESULTS[rstart:rend]

        if status == 'Pass':
            PASS.write(name + '\n')
            PASS.flush()
            passed += 1
        elif status == 'Fail':
            FAIL.write(name + '\n')
            FAIL.flush()
            failed += 1
        elif status == 'NotSupported':
            NOSUPPORT.write(name + '\n')
            NOSUPPORT.flush()
            nosupport += 1
        elif status == 'QualityWarning':
            WARN.write(name + '\n')
            WARN.flush()
            warned += 1
        else:
            print status + ': ' + name

        pos = rend

        # Find slow
        tstart = RESULTS.find('Test case duration in microseconds', nend)
        tstart = RESULTS.find('"us">', tstart)
        tstart += 5
        tend = RESULTS.find('</Number', tstart)
        runtime = float(RESULTS[tstart:tend]) * 1e-6
        if status == 'Pass':
            passes.append((name,runtime))

    print "%d / %d -- %.2f%%" % (passed, n, 100.0*passed/float(n))

print
print '%10s: %6d / %d  -- %6.2f%%' % ('PASS', passed, total, 100.0*passed/float(total))
print '%10s: %6d / %d  -- %6.2f%%' % ('FAIL', failed, total, 100.0*failed/float(total))
print '%10s: %6d / %d  -- %6.2f%%' % ('CRASH', crashed, total, 100.0*crashed/float(total))
print '%10s: %6d / %d  -- %6.2f%%' % ('WARN', warned, total, 100.0*warned/float(total))
print '%10s: %6d / %d  -- %6.2f%%' % ('NOSUPPORT', nosupport, total, 100.0*nosupport/float(total))
print

RUNTIMES = open('RUNTIMES', 'w')
for p in passes:
    print >>RUNTIMES, '%.3f %s' % (p[1], p[0])
