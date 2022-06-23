'''
Minimize lateness

Scenario example

▪ IIT Madras has a single 3D  printer 

▪ A number of users need to use  this printer 

▪ Each user will get access to the  printer, but may not finish before  deadline 

▪ Goal is to minimize the lateness 

Algorithm

1) Sort all job in ascending order of deadlines

2) Start with time t = 0

3) For each job in the list

	-> Schedule the job at time t
	-> Finish time = t + processing time of job
	-> t = finish time

4) Return (start time, finish time) for each job
'''

from operator import itemgetter
 
def minimize_lateness(jobs):
    schedule =[]
    max_lateness = 0
    t = 0
     
    sorted_jobs = sorted(jobs,key=itemgetter(2))
     
    for job in sorted_jobs:
        job_start_time = t
        job_finish_time = t + job[1]
 
        t = job_finish_time
        if(job_finish_time > job[2]):
            max_lateness =  max (max_lateness, (job_finish_time - job[2]))
        schedule.append((job[0],job_start_time, job_finish_time))
 
    return max_lateness, schedule
 
jobs = [(1, 3, 6), (2, 2, 9), (3, 1, 8), (4, 4, 9), (5, 3, 14), (6, 2, 15)]
max_lateness, sc = minimize_lateness(jobs)
print ("Maximum lateness is :" + str(max_lateness))
for t in sc:
    print ('JobId= {0}, start time= {1}, finish time= {2}'.format(t[0],t[1],t[2]))

'''
Output : 

Maximum lateness is :1
JobId= 1, start time= 0, finish time= 3
JobId= 3, start time= 3, finish time= 4
JobId= 2, start time= 4, finish time= 6
JobId= 4, start time= 6, finish time= 10
JobId= 5, start time= 10, finish time= 13
JobId= 6, start time= 13, finish time= 15
'''