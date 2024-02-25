import discord
import webbrowser
import requests
from requests_oauthlib import OAuth2Session

CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
REDIRECT_URI = 'REDIRECT_URI'


def login(client_id, client_secret, redirect_uri) -> str:
    authorization_base_url = 'https://discord.com/api/oauth2/authorize'
    token_url = 'https://discord.com/api/oauth2/token'

    scope = ['email', 'identify', 'guilds', 'guilds.members.read',
             'rpc', 'rpc.video.read', 'rpc.voice.read', 'voice']

    vc = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = vc.authorization_url(authorization_base_url)

    webbrowser.open(authorization_url)

    redirect_response = input('Paste the full callback URL: ')

    token = vc.fetch_token(token_url, client_secret=client_secret,
                           authorization_response=redirect_response)

    return token


if __name__ == '__main__':
    authentication = login(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    headers = {'Authorization': f'Bearer {authentication["access_token"]}'}
    user = requests.get('https://discord.com/api/users/@me', headers=headers)
    guilds = requests.get(
        'https://discord.com/api/users/@me/guilds', headers=headers)
    print(user.json())
    print(guilds.json())
