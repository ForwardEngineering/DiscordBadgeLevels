import requests
import time
import sys
import json
import os

class a:
    def __init__(self, t):
        self.u = "https://discord.com/api/v9"
        self.n = 0
        self.un = None
        self.h = {
            'authorization': t,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def g(self):
        r = requests.get(f"{self.u}/users/@me", headers=self.h)
        if r.status_code == 200:
            d = r.json()
            self.un = f"{d.get('username')}#{d.get('discriminator')}"
            return True
        return False

    def s(self):
        r = requests.post(f"{self.u}/gorilla/activity/gathering/start", headers=self.h)
        return r.json() if r.status_code == 200 else None

    def e(self):
        r = requests.post(f"{self.u}/gorilla/activity/gathering/complete", headers=self.h)
        return r.json() if r.status_code == 200 else None

    def d(self, d, n):
        if not d or 'user_data' not in d:
            return False
        
        u = d['user_data']
        xp = u.get('xp', 0)
        lv = u.get('level', 0)
        ch = d.get('changes', {})
        
        if hasattr(self, 'xp') and self.xp is not None:
            xg = xp - self.xp
        else:
            xg = 0
        
        st = u.get('stats', {})
        ac = st.get('activity_completion', {})
        gc = ac.get('gathering', 0)
        
        if lv < 100:
            xn = ((lv + 1) * 1000) - xp
            ns = f"{xn} XP to level {lv + 1}"
        else:
            ns = "MAX LEVEL"
        
        sys.stdout.write('\033[2J\033[H')
        
        print(f"Discord: {self.un}")
        print(f"Session: {n}")
        print(f"Level: {lv}/100")
        print(f"XP: {xp}")
        print(f"+XP: +{xg}")
        print()
        print("Resources:")
        for r, a in ch.items():
            if a > 0:
                print(f"  {r}: +{a}")
        print()
        print(f"Total: {gc}")
        print(f"Next: {ns}")
        
        self.xp = xp
        
        return True

    def r(self, n):
        if not self.s():
            return False
        
        r = self.e()
        
        if r:
            self.d(r, n)
            return True
        return False

    def run(self):
        if not self.g():
            print("Failed to get user info")
            return
        
        self.n = 0
        self.xp = None
        sys.stdout.write('\033[2J\033[H')
        
        try:
            while True:
                self.n += 1
                if not self.r(self.n):
                    sys.stdout.write('\033[2J\033[H')
                    print("ERROR - retrying...")
                    time.sleep(2)
                    
        except KeyboardInterrupt:
            sys.stdout.write('\033[2J\033[H')
            print(f"\nStopped - Total: {self.n}")

def main():
    if not os.path.exists('token.json'):
        print("token.json not found!")
        return
    
    with open('token.json', 'r') as f:
        data = json.load(f)
        token = data.get('token')
        
    if not token:
        print("Token not found in token.json!")
        return
    
    a(token).run()

if __name__ == "__main__":
    main()