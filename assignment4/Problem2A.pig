register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);
-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
--group the n-triples by object column
subjects = group ntriples by (subject) PARALLEL 50;
-- flatten the subjects out (because group by produces a tuple of each object
-- in the first column, and we want each subject to be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;
-- we want to group by the counts to get the x axis
xaxis = group count_by_subject by (count) PARALLEL 50;
-- the number of tuples associated to each count makes the y axis
histogram = foreach xaxis generate ($0), COUNT($1) PARALLEL 50;
-- store the results in the folder /user/hadoop/Problem2A
store histogram into '/user/hadoop/Problem2A' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/Problem2A';

