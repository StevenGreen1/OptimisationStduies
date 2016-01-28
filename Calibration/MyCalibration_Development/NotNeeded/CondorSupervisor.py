#!/usr/bin/python

import os, sys, getopt, re, subprocess

#-------------------------------------------------------------------------------------------------------------------------------------------

def GetJobString():
    jobString  = 'executable              = ' + os.environ['HOME'] + '/jobs/lar/lar.sh                           \n'
    jobString += 'initial_dir             = ' + os.environ['HOME'] + '/jobs/lar/                                 \n'
    jobString += 'notification            = never                                                                \n'
    jobString += 'Requirements            = (memory > 2048) && (OSTYPE == \"SLC6\")                              \n'
    jobString += 'Rank                    = memory                                                               \n'
    jobString += 'output                  = ' + os.environ['HOME'] + '/CondorLogs/lar.out                        \n'
    jobString += 'error                   = ' + os.environ['HOME'] + '/CondorLogs/lar.err                        \n'
    jobString += 'log                     = ' + os.environ['HOME'] + '/CondorLogs/lar.log                        \n'
    jobString += 'environment             = CONDOR_JOB=true                                                      \n'
    jobString += 'Universe                = vanilla                                                              \n'
    jobString += 'getenv                  = false                                                                \n'
    jobString += 'copy_to_spool           = true                                                                 \n'
    jobString += 'should_transfer_files   = yes                                                                  \n'
    jobString += 'when_to_transfer_output = on_exit_or_evict                                                     \n'
  return jobString

#-------------------------------------------------------------------------------------------------------------------------------------------

def GetJobArguments(scripts, firstLine):
  arguments = firstLine.split()

  if 4 != len(arguments):
    print 'Invalid arguments found in runlist.'
    sys.exit(3)

  nEvents = arguments[0]
  nSkip = arguments[1]
  inputFile = arguments[2]
  outputFile = arguments[3]

  jobArguments = 'arguments = ' + scripts + ' ' + nEvents + ' ' + nSkip + ' ' + inputFile + ' ' + outputFile

#  #For python-style target script
#  jobArguments = 'arguments = -c ' + scripts + ' -n ' + nEvents + ' -i ' + inputFile + ' -o ' + outputFile
#
#  if 0 != int(nSkip):
#    jobArguments += ' -e ' + nSkip

  jobArguments += '\n'
  return jobArguments

#-------------------------------------------------------------------------------------------------------------------------------------------

def main():
  scripts = ''
  runlist = ''
  maxRuns = 1

  try:
    opts, args = getopt.getopt(sys.argv[1:],"hc:r:m:",["scripts=","runlist=","maxRuns="])
  except getopt.GetoptError:
    print 'condorSupervisor.py -c <script(s) colon-separated list> -r <runlist> -m <maxRuns>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
       print 'condorSupervisor.py -c <script(s) colon-separated list> -r <runlist> -m <maxRuns>'
       sys.exit()
    elif opt in ("-c", "--scripts"):
       scripts = arg
    elif opt in ("-r", "--runlist"):
       runlist = arg
    elif opt in ("-m", "--maxRuns"):
       maxRuns = arg

  maxRuns = int(maxRuns)

  if not runlist or not os.path.isfile(runlist):
    print 'Invalid runlist specified'
    sys.exit(2)

  while True:
    queueProcess = subprocess.Popen(['condor_q'], stdout=subprocess.PIPE)
    queueOutput = queueProcess.communicate()[0]

    regex = re.compile('lar|Pandora')
    queueList = regex.findall(queueOutput)
    nQueued = len(queueList)

    if nQueued >= maxRuns:
      subprocess.call(["usleep", "500000"])
    else:
      with open(runlist, 'r') as file:
        firstLine = file.readline()
        fileContents = file.read().splitlines(True)

      nRemaining = len(fileContents)

      with open(runlist, 'w') as file:
        file.truncate()
        file.writelines(fileContents)

      with open('tempLAr.job', 'w') as jobFile:
        jobFile.truncate()
        jobString  = GetJobString()
        jobString += GetJobArguments(scripts, firstLine)
        jobString += 'queue 1 \n'
        jobFile.write(jobString)

      subprocess.call(['condor_submit', 'tempLAr.job'])
      print 'Submitted job as there were only ' + str(nQueued) + ' jobs in the queue and ' + str(nRemaining) + ' jobs remaining.'
      subprocess.call(["usleep", "500000"])
      os.remove('tempLAr.job')

      if 0 == nRemaining:
        print 'Runlist empty'
        sys.exit(0)

#-------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
