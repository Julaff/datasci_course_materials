register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
 raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);
-- parse each line into ntriples
ntriples = FOREACH raw GENERATE FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
-- we filter on the desired field
file1 = FILTER ntriples by subject matches '.*rdfabout\\.com.*';
-- we make a copy of the filtered data
file2 = FOREACH file1 GENERATE * as (subject2:chararray,predicate2:chararray,object2:chararray);
-- we join on object=subject2
joinfile = JOIN file1 by object, file2 by subject2;
-- we remove duplicates
cleanjoinfile = DISTINCT joinfile;
-- store the results in the folder /user/hadoop/Problem3B
STORE cleanjoinfile into '/user/hadoop/Problem3B' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/Problem3B';

