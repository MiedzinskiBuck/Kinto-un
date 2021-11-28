import boto3

class Sts:

    def get_client(self, session):
        client = session.client('sts')
        return client

    def assume_role(self, client, acc_number, role_name, session_name):
        try:
            response = client.assume_role(
                    RoleArn='arn:aws:iam::{}:role/{}'.format(acc_number, role_name),
                    RoleSessionName=session_name,
                    DurationSeconds=3600
                    )
            return response
        except Exception as e:
            return(e.response["Error"]["Code"])

    def get_account_number(self, client, access_key_id):
        try:
            response = client.get_access_key_info(
                AccessKeyId=access_key_id
            )
            return response["Account"]
        except Exception as e:
            return(e)
