import discord
import webbrowser
import requests
from requests_oauthlib import OAuth2Session

CLIENT_ID = '1210850089489408052'
CLIENT_SECRET = 'd5j21x_3kUiMO8slW2W05yEzuRvZypXF'
REDIRECT_URI = 'http://localhost:5000/callback'


def login(client_id, client_secret, redirect_uri) -> str:
    authorization_base_url = 'https://discord.com/api/oauth2/authorize'
    token_url = 'https://discord.com/api/oauth2/token'

    scope = ['email', 'identify', 'voice']

    vc = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = vc.authorization_url(authorization_base_url)

    webbrowser.open(authorization_url)

    redirect_response = input('Paste the full callback URL: ')

    token = vc.fetch_token(token_url, client_secret=client_secret,
                           authorization_response=redirect_response)

    return token


if __name__ == '__main__':
    access_token = login(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
