import boto3
from datetime import datetime
from src.config.settings import USER_POOL_ID, CORS_HEADERS

dynamodb = boto3.resource('dynamodb')
cognito = boto3.client('cognito-idp')

TABLE_NAME = 'usuarios'

def handler(event, context):
    user_attrs = {attr['Name']: attr['Value'] for attr in event['request']['userAttributes']}
    
    sub = user_attrs.get('sub')
    email = user_attrs.get('email')
    nome = user_attrs.get('custom:nome')
    perfil = user_attrs.get('custom:perfil')

    if not all([sub, email, nome, perfil]):
        raise Exception("Campos obrigatórios faltando")

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item={
        'PK': f'USER#{sub}',
        'email': email,
        'nome': nome,
        'perfil': perfil,
        'dataCadastro': datetime.utcnow().isoformat(),
        'status': 'ATIVO'
    })

    cognito.admin_add_user_to_group(
        UserPoolId=USER_POOL_ID,
        Username=email,
        GroupName=perfil 
    )

    return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": event
        }