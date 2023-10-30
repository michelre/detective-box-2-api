import boto3
from api.config import settings


class Storage:
    def __init__(self):
        session = boto3.session.Session()
        self.client = session.client(
            's3',
            endpoint_url=settings.aws_endpoint_url,
            region_name='fra1',
            aws_access_key_id=settings.aws_key_id,
            aws_secret_access_key=settings.aws_secret_key
        )

    def get(self, name):
        try:
            return self.client.get_object(
                Bucket=settings.aws_bucket,
                Key=name
            )
        except Exception:
            return None

    def list(self):
        try:
            return self.client.list_objects(Bucket=settings.aws_bucket)
        except Exception:
            return None
