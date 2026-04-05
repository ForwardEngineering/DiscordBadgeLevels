import requests
import time
import json
import os
import uuid
import re

class a:
    def __init__(self, t):
        self.u = "https://discord.com/api/v9"
        self.n = 0
        self.un = None
        self.uid = None
        self.hbs = str(uuid.uuid4())
        self.ads = str(uuid.uuid4())
        self.es = 0
        self.ls = str(uuid.uuid4())
        self.st = None
        self.super_props = None
        
        self.c = {
            'locale': 'en-US',
        }
        
        self.h = self.get_dynamic_headers(t)
        if not self.h:
            self.h = {
                'authorization': t,
                'content-type': 'application/json',
            }

    def get_dynamic_headers(self, token):
        headers = {
            'authorization': token,
            'content-type': 'application/json',
        }
        
        try:
            r = requests.get('https://discord.com/app', timeout=10)
            if r.status_code == 200:
                build_match = re.search(r'"buildNumber":"(\d+)"', r.text)
                if build_match:
                    build_number = build_match.group(1)
                    
            browser_version = "146.0.0.0"
            
            sp_data = {
                "os": "Windows",
                "browser": "Chrome",
                "device": "",
                "system_locale": "it-IT",
                "has_client_mods": False,
                "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
                "browser_version": browser_version,
                "os_version": "10",
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "https://discord.com/channels/@me",
                "referring_domain_current": "discord.com",
                "release_channel": "stable",
                "client_build_number": 523061,
                "client_event_source": None,
                "client_launch_id": str(uuid.uuid4()),
                "launch_signature": self.ls,
                "client_heartbeat_session_id": self.hbs,
                "client_app_state": "focused"
            }
            
            import base64
            sp_json = json.dumps(sp_data)
            self.super_props = base64.b64encode(sp_json.encode()).decode()
            
            headers.update({
                'accept': '*/*',
                'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': f'"Chromium";v="{browser_version.split(".")[0]}", "Not-A.Brand";v="24", "Google Chrome";v="{browser_version.split(".")[0]}"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'Europe/Rome',
                'x-super-properties': self.super_props,
            })
            
            return headers
            
        except Exception as e:
            return None

    def s(self, t, p=None):
        self.es += 1
        ts = int(time.time() * 1000)
        
        if p is None:
            p = {}
        
        token_part = self.h.get('authorization', '').split('.')[0] if 'authorization' in self.h else ''
        
        d = {
            'token': f'{token_part}.aBWJ_VyfPH8NPA9Dlu8o9b_DZwo',
            'events': [{
                'type': t,
                'properties': {
                    'client_track_timestamp': ts,
                    'client_heartbeat_session_id': self.hbs,
                    'event_sequence_number': self.es,
                    'client_performance_memory': 0,
                    'accessibility_features': 524544,
                    'rendered_locale': 'en-US',
                    'uptime_app': int(time.time() - self.st) if self.st else 30,
                    'launch_signature': self.ls,
                    'client_rtc_state': 'DISCONNECTED',
                    'client_app_state': 'focused',
                    'client_viewport_width': 1365,
                    'client_viewport_height': 963,
                    'client_uuid': str(uuid.uuid4()),
                    'client_send_timestamp': ts,
                    **p
                },
            }],
        }
        
        try:
            r = requests.post(f"{self.u}/science", cookies=self.c, headers=self.h, json=d, timeout=10)
            return r.status_code == 200
        except:
            return False

    def hb(self):
        return self.s('client_ad_heartbeat', {
            'client_ad_session_id': self.ads,
            'client_heartbeat_initialization_timestamp': int(self.st * 1000) if self.st else 0,
            'client_heartbeat_version': 3,
        })

    def g(self):
        try:
            r = requests.get(f"{self.u}/users/@me", headers=self.h, timeout=10)
            if r.status_code == 200:
                d = r.json()
                self.un = d.get('username')
                self.uid = d.get('id')
                return True
            return False
        except:
            return False

    def gu(self):
        try:
            r = requests.get(f"{self.u}/gorilla/user-data/@me", headers=self.h, timeout=10)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    def gc(self):
        try:
            r = requests.get(f"{self.u}/gorilla/counters", headers=self.h, timeout=10)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    def sc(self, cc, cb):
        d = {'crafting_class': cc, 'combat_class': cb}
        try:
            r = requests.post(f"{self.u}/gorilla/user-data/@me", headers=self.h, json=d, timeout=10)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    def stg(self):
        try:
            r = requests.post(f"{self.u}/gorilla/activity/gathering/start", headers=self.h, timeout=10)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    def cg(self):
        try:
            r = requests.post(f"{self.u}/gorilla/activity/gathering/complete", headers=self.h, timeout=10)
            if r.status_code == 200:
                return r.json()
            return None
        except:
            return None

    def d(self, d, n):
        if not d or 'user_data' not in d:
            return False
        
        u = d['user_data']
        xp = u.get('xp', 0)
        lv = u.get('level', 0)
        ch = d.get('changes', {})
        
        cc = u.get('crafting_class', 'none')
        cb = u.get('combat_class', 'none')
        
        s = u.get('stats', {})
        rc = s.get('resource_contribution', {})
        ac = s.get('activity_completion', {})
        gca = ac.get('gathering', 0)
        
        if hasattr(self, 'xpv') and self.xpv is not None:
            xg = xp - self.xpv
        else:
            xg = 0
        
        if lv < 100:
            xn = ((lv + 1) * 1000) - xp
        else:
            xn = 0
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("-" * 60)
        print(f"DiscordBadgeLevels - {self.un} [{n}]")
        print("-" * 60)
        
        print(f"\nPROGRESS".ljust(30) + f"CLASSES")
        print(f"  LV {lv}/100".ljust(30) + f"  Craft: {cc.replace('_', ' ').title()}")
        print(f"  XP {xp}".ljust(30) + f"  Combat: {cb.replace('_', ' ').title()}")
        print(f"  +{xg} XP".ljust(30))
        print(f"  ->{xn} to next")
        
        print(f"\nGAINED".ljust(30) + f"TOTAL")
        gained_items = list(ch.items())[:3]
        total_items = list(rc.items())[:3]
        
        for i in range(3):
            g = gained_items[i] if i < len(gained_items) else (None, None)
            t_item = total_items[i] if i < len(total_items) else (None, None)
            
            g_text = f"+{g[1]} {g[0].title()}" if g[0] else ""
            t_text = f"{t_item[1]} {t_item[0].title()}" if t_item[0] else ""
            
            print(f"  {g_text:<26}".ljust(30) + f"  {t_text}")
        
        print(f"\nGATHERINGS: {gca}")
        
        c = self.gc()
        if c:
            print("\n" + "-" * 60)
            print("WORLD RESOURCES")
            print("-" * 60)
            
            rc = c.get('resource_counters', [])
            
            for i in range(0, len(rc), 2):
                r1 = rc[i]
                name1 = r1.get('id', '').replace('_', ' ').title()
                cur1 = r1.get('current_count', 0)
                
                if i + 1 < len(rc):
                    r2 = rc[i + 1]
                    name2 = r2.get('id', '').replace('_', ' ').title()
                    cur2 = r2.get('current_count', 0)
                    print(f"  {name1:<20} {cur1:>12,}    {name2:<20} {cur2:>12,}")
                else:
                    print(f"  {name1:<20} {cur1:>12,}")
        
        print("\n" + "-" * 60)
        
        self.xpv = xp
        return True

    def r(self, n):
        self.hb()
        
        sd = self.stg()
        if not sd:
            return False
        
        time.sleep(3)
        
        cd = self.cg()
        if not cd:
            return False
        
        self.d(cd, n)
        return True

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.st = time.time()
        
        print("=" * 60)
        print("DiscordBadgeLevels - Last Meadow XP Farmer")
        print("https://github.com/ForwardEngineering/DiscordBadgeLevels")
        print("=" * 60)
        
        if not self.g():
            print("\nFailed to authenticate")
            input("\nPress Enter...")
            return
        
        print(f"\nAuthenticated: {self.un}")
        
        print("\nInitializing...")
        self.hb()
        time.sleep(1)
        
        ud = self.gu()
        if ud:
            if ud.get('level', 0) == 0 and ud.get('crafting_class') is None:
                print("Selecting classes...")
                r = self.sc('armor_crafter', 'healer')
                if r:
                    print("Classes selected: Armor Crafter / Healer")
                time.sleep(1)
        
        print("\nFarming XP (Ctrl+C to stop)")
        print()
        
        self.n = 0
        self.xpv = None
        time.sleep(1)
        
        try:
            while True:
                self.n += 1
                if not self.r(self.n):
                    time.sleep(5)
                else:
                    time.sleep(2)
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 60)
            print("STOPPED")
            print("=" * 60)
            print(f"\nTotal Sessions: {self.n}")
            
            fd = self.gu()
            if fd:
                print(f"Final Level: {fd.get('level', 0)}")
                print(f"Final XP: {fd.get('xp', 0)}")
            print("\nhttps://github.com/ForwardEngineering/DiscordBadgeLevels")
            input("\nPress Enter...")

def main():
    if not os.path.exists('token.json'):
        print("token.json not found")
        print('\nCreate token.json with: {"token": "your_token"}')
        input("\nPress Enter...")
        return
    
    try:
        with open('token.json', 'r') as f:
            d = json.load(f)
            t = d.get('token')
    except:
        print("Error reading token.json")
        input("\nPress Enter...")
        return
    
    if not t:
        print("Token not found")
        input("\nPress Enter...")
        return
    
    a(t).run()

if __name__ == "__main__":
    main()
