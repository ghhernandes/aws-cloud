# S3 101

- *Object-based* (image, audio, video, text files)
- max 5TB size per file
- limited storage
- files are stored in *buckets*
- have *universal namespace*
- success uploads returns HTTP status code 200 
- allowed *static websites*

## Key Fundamentals

- *Key* = object name
- *Value* = object content (bytes)

*POST objects* instantly appears on S3 bucket

*PUTS/DELETE* have a delay

*Buckets* are global, but stored on a specific region. *Cross Replication*
can be utilized for replying to others regions.


## S3 Transfer Acceleration

**Link**: https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html

Make use of **Edge Locations**. As the data arrives at an edge location, data is routed to Amazon S3 over an *optimized network path*.

Increases upload speed in 300% depending region.



## Storage Types

- **S3 Standard** stored in multiples availability zones. Can sustain lose of 2 AZ's simultaneously. 99.99% availability. 99.999999999% durability.
- **S3 IA (Infrequently Accessed)** low frequency access, but fast recovery. Lower cost, but higher recovery costs.
- **S3 One Zone - IA** like *S3 IA* but without multi-az.
- **S3 Intelligent Tiering** cost otimized. Uses Machine Learning to move data between *tiers* without performance or operational impact.
- **S3 Glacier** to store data for minimal access. High recovery time.
- **S3 Glacier Deep Archive** like *S3 Glacier*, but with higher recovery time (eg 12 hours).


