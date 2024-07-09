## UPTIME KUMA DEPLOY

### What is it

A simple python script to manage an Uptime Kuma instance

#### Uptime Kuma install (manual)
```bash
git clone https://github.com/louislam/uptime-kuma.git
cd uptime-kuma
npm run setup
```

##### Option 1. Try it
```bash
node server/server.js
```

##### (Recommended) Option 2. Run in the background using PM2 (have to find a way to add the max-http-header to node start params)
##### its limited to a low value for patching well known nodejs exploit
##### Install PM2 if you don't have it:
```bash
npm install pm2 -g && pm2 install pm2-logrotate
```

##### Start Server
```bash
pm2 start server/server.js --name uptime-kuma
node --max-http-header-size=48000 server/server.js
```
#### Add websites to monitor in inventory.yml
```bash
vim inventory.yml
```


#### Add notification
```bash
python3 add_notification.py -i inventory
```
#### Add probes
```bash
python3 add_monitors.py -i inventory
```
