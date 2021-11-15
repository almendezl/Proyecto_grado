import boto3

client = boto3.client(
	"sns",
	aws_access_key_id ="AKIAZIHTODSFBNMRVKXJ",
	aws_secret_access_key="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",
	region_name="us-east-2"
)

client.publish(
	PhoneNumber="+573214200365",
	Message="Prueba de SMS"
)