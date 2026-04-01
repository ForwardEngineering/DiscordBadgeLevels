# DiscordBadgeLevels

Auto-level your Last Meadow badge on Discord.

## How it works

The script uses Discord's internal API:

-   `POST /gorilla/activity/gathering/start` → starts gathering
-   `POST /gorilla/activity/gathering/complete` → completes it and gives
    XP

It loops continuously and prints:
- your level
- XP gained
- resources collected

## Requirements

-   Python 3
-   requests library

``` bash
pip install requests
```

## How to use

1.  Get your Discord token

-   Open Discord in browser\
-   Press F12 → Console\
-   Paste this and press Enter:

``` js
let m;webpackChunkdiscord_app.push([[Math.random()],{},e=>{for(let i in e.c){let x=e.c[i];if(x?.exports?.getToken){m=x;break}}}]);m&&console.log("Token:",m.exports.getToken());
```

-   Copy the token

2.  Create `token.json`

``` json
{
  "token": "your_token_here"
}
```

3.  Run the script

``` bash
python auto.py
```

4.  Stop anytime with Ctrl+C

## Notes

-   You need the Last Meadow badge unlocked
-   Runs until you stop it
-   Retries automatically if it fails
