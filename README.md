# aws-route53-delete-record-sets
If you need to delete hundreds or thousands of Route53 record sets, here you go. 

I needed to delete tens of thousands of record sets but the other scripts I found did them one at a time. This script will batch them.

*Use at your own risk*. I used this successfully, but there isn't any error handling going on here.


_NOTE_: This does not delete NS and SOA records.


# Usage
```
pip install boto3
python route53_delete_record_sets HOSTED_ZONE_ID
```