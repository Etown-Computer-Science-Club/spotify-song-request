# spotify-song-request

1. Visit the following URL after replacing CLIENT_ID, SCOPE, and REDIRECT_URI. Make sure the REDIRECT_URI is URL encoded.

```
https://accounts.spotify.com/authorize?response_type=code&client_id=3e37e768beae458baea868d157704ba2&scope=user-modify-playback-state%20user-read-playback-state&redirect_uri=https://etowncs.club
```

2. Get code from the redirect URL

3. Get the refresh token

```curl
curl -d client_id=CLIENT_ID -d client_secret=CLIENT_SECRET -d grant_type=authorization_code -d code=CODE -d redirect_uri=REDIRECT_URI https://accounts.spotify.com/api/token
```
