from sys import exit

needPassword = input()
password = "0"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'()*+,-./:;<=>?@[\]^_{|}~"

for a in range(len(characters)):
  for b in range(len(characters)):
    for c in range(len(characters)):
      for d in range(len(characters)):
        for e in range(len(characters)):
          for f in range(len(characters)):
            for g in range(len(characters)):
              for h in range(len(characters)):
                password = characters[a] + characters[b] + characters[c] + characters[d] + characters[e] + characters[f] + characters[g] + characters[h]
                print(password)
                if (str(password) == str(needPassword):
                  print("Password found!")
                  exit(0)
