# everything except the line with canary.discord.com/api/v6/invite is by me 
def main():
  import requests, os

  def get_invite_code():
    import random
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    code = ""
    for i in range(8):
      code += chars[random.randrange(len(chars))]
    return code

  while 1:
    code = get_invite_code()
    print(f"Trying: {code}")
    try:
      request = requests.get(f"https://canary.discord.com/api/v6/invite/{code}?with_counts=true", timeout=1)
      if request.status_code == 200:
        print(f"{code} worked! Added {code} to working.txt")
        if os.path.exists("working.txt"):
          if open("working.txt","r") > 1:
            open("working.txt","a").write(f"\n{code}")
          else:
            open("working.txt","a").write(f"{code}")
        else:
          if open("working.txt","r") > 1:
            open("working.txt","a").write(f"\n{code}")
          else:
            open("working.txt","a").write(f"{code}")
    except Exception:
      if request.status_code == 404:
        print(f"{code} didn't work.")
      else:
        print(f"I am being ratelimited.")


import threading

for i in range(50): threading.Thread(target=main).start();print(f"Started thread {i}")
