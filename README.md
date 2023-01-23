This repository is a solution to one of the AWS Developer associate question:

Q-> A company manages an application that stores data in an Amazon DynamoDB table. The company need to keep a record of all new changes made to the DynamoDB table 
in another table within the same AWS region.What is the MOST suitable way to deliver this requirement?
A-> Use DynamoDB Streams.

Although that's the answer but how can we implement it in realtime! Hence I've made this repository with all the necessary documents.

A DynamoDB table will perform the insertion of data. This table has DynamoDB streams enabled with stream-view-type as "NEW_AND_OLD_IMAGES" which will trigger our lambda function.
The lambda function will process the entered data once it has been triggered and will enter the same details in our backup table which is "LambdaToDynamoDB" table along with the timestamp. 
Hence even if the original table is deleted by mistake, the new backup table will still be available for everyone to use.
