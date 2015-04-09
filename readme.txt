The program is produced and owned by Xichang Zhao.

Installation of "Levenshtein" module is required for running the program (project1.py). (the package is included)

In case the module cannot be installed on server, project1b.py can be used. Notice that the execution time will be much slower since a written function was used instead (even though it is still a dynamic programming edit-distance algorithm).

The program takes a location file ("US.txt"like format) and a tweets file ("set_tweets.txt"like format) to print out the ids of those tweets that may include the locations listed in the location file (standard according to the threshold of edit distance)

The default settings for the location file name, tweets file name and boundary are "US_small.txt", "training_set_tweets_small.txt" and 1 respectively.

The setting can be changed by entering arguments upon running, the orders are location file, tweets file and boundary (Remember to include ".txt" for file names!!)

The sample tests "b.txt" and "a.txt" are location file and tweet file respectively, they contain some of representative cases.