import subprocess
import sys

PASS = open('PASS', 'w')
FAIL = open('FAIL', 'w')
NOSUPPORT = open('NOSUPPORT', 'w')
WARN = open('WARN', 'w')
TIMEOUT = open('TIMEOUT', 'w')
CRASH = open('CRASH', 'w')

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: python classify.py CASEFILE [deqp-vk]')
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
timedout = 0
warned = 0
nosupport = 0
total = len(CASES)
if total == 0:
    print('Test file is empty.')
    exit(1)
print('Running %d tests' % total)

passes = []

while n < total:

    # Prepare the next 1000 tests
    with open('TMP', 'w') as TMP:
        for line in CASES[n:n+1000]:
            TMP.write(line)

    # Run the tests
    OUTPUT = open('OUTPUT', 'w')
    ERROR = open('ERROR', 'w')
    subprocess.call(
        [DEQP,
        '--deqp-caselist-file=TMP',
        '--deqp-crashhandler=enable',
        '--deqp-watchdog=enable'],
        stdout=OUTPUT, stderr=ERROR)

    # Loop over test results
    RESULTS = open('TestResults.qpa', 'r').read()
    pos = 0
    while True:
        # Find start of next test result
        tstart = RESULTS.find('<TestCaseResult', pos)
        if tstart < 0:
            if n == 0:
                print('Fatal crash before any tests have run (see ERROR).')
                exit(1)
            break

        nstart = RESULTS.find('CasePath="', tstart)
        nstart += 10
        nend = RESULTS.find('"', nstart)
        name = RESULTS[nstart:nend]

        n += 1

        # Get status code if present (otherwise assume test crashed)
        rstart = RESULTS.find('<Result StatusCode="', nend)
        if rstart < 0:
            if RESULTS.find('#terminateTestCaseResult Timeout', nend) > 0:
                TIMEOUT.write(name + '\n')
                TIMEOUT.flush()
                timedout += 1
            else:
                CRASH.write(name + '\n')
                CRASH.flush()
                crashed += 1
            break
        rstart += 20
        rend = RESULTS.find('">', rstart)
        status = RESULTS[rstart:rend]

        # Add test to appropriate group
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
            print(status + ': ' + name)

        pos = rend

        # Get test runtime
        tstart = RESULTS.find('Test case duration in microseconds', nend)
        tstart = RESULTS.find('"us">', tstart)
        tstart += 5
        tend = RESULTS.find('</Number', tstart)
        runtime = float(RESULTS[tstart:tend]) * 1e-6
        if status == 'Pass':
            passes.append((name,runtime))

    print('%d / %d -- %.2f%%' % (passed, n, 100.0*passed/float(n)))

print()
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('PASS', passed, total,100.0*passed/float(total)))
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('FAIL', failed, total,100.0*failed/float(total)))
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('CRASH', crashed, total,100.0*crashed/float(total)))
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('TIMEOUT', timedout, total,100.0*timedout/float(total)))
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('WARN', warned, total,100.0*warned/float(total)))
print('%10s: %6d / %d  -- %6.2f%%' % \
    ('NOSUPPORT', nosupport, total,100.0*nosupport/float(total)))
print()

# Dump runtimes for tests that passed
RUNTIMES = open('RUNTIMES', 'w')
for p in passes:
    RUNTIMES.write('%.3f %s\n' % (p[1], p[0]))
