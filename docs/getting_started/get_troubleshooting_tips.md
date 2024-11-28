# Troubleshooting Tips

If you're having trouble signing in to Sekoia, get more information about signing in issues and fixing them.

## Common Problems

### WebSocket Problem

If Sekoia.io can't maintain WebSocket connections on the browser, the web application won't automatically refresh with the new contents and a network connectivity error is displayed on top of the application.

#### Troubleshooting Steps

**Step 1: Contact your network administrator**

Contact your network administrator to make sure they support WebSocket connections. Also ask it to review login attempts to the following URL: [app.sekoia.io/live](wss://app.sekoia.io/live)

**Step 2: Collect and send us network logs**

If the problem persists, collect and send the network logs to us so we can investigate the situation further. You can collect network logs through through Google Chrome.

1. Open Google Chrome and navigate to the following link: chrome://net-export/
2. Click Start Logging to Disk
3. Save the file as sekoiaNetlog
4. In another Chrome tab, open your Sekoia workspace
5. Use Sekoia as you normally do. When the problem occurs, go back to the chrome://net-export/ tab and click Stop Logging
6. Find the sekoiaNetlog file in the Downloads folder on your computer
7. Send us a message with the file attached

!!! note
    If you don't use Chrome as your browser, send us a message and we'll help you resolve the issue.