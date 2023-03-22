import sys
import boto3

if len(sys.argv) != 2:
  print("Usage: route53_delete_record_sets HOSTED_ZONE_ID")
  sys.exit(1)


HOSTED_ZONE_ID = sys.argv[1]
BATCH_ITEMS = 1000

client = boto3.client('route53')

confirm = input(f"This will delete all non NS and SOA record sets in hosted zone {HOSTED_ZONE_ID}. Are you sure you want to continue (yes/no)? ")
if confirm != "yes":
  sys.exit(1)

while True:
  print("Grabbing batch of records...")
  records = client.list_resource_record_sets(HostedZoneId=HOSTED_ZONE_ID, MaxItems=f"{BATCH_ITEMS}")
  changes = [{ "Action": "DELETE", "ResourceRecordSet": r} for r in records["ResourceRecordSets"] if r["Type"] not in ["NS", "SOA"]]
  if len(changes) == 0:
    break

  print(f"Deleting {len(changes)} records...")
  client.change_resource_record_sets(HostedZoneId=HOSTED_ZONE_ID,
    ChangeBatch={ "Changes": changes }
  )

print("Done.")