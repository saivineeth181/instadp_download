import requests
def insta_dp():
    username=input('\033[92m ENTER USERNAME:\033[0m')

    url = f"https://www.instagram.com/{username}/?__a=1"
    r = requests.get(url)

    if r.ok:
        pic=r.json()
        hd=pic.get('graphql').get('user').get('profile_pic_url_hd')
        t = requests.get(hd, stream=True)
        print(t)
        fname = f"{username}.png"
        if r.ok:
             with open(fname, 'wb') as f:
                f.write(t.content)
                print(f"\033[92m✔ Downloaded:\033[0m {fname}")

        else:
            print('no username')
    else:
        print("try again no username matched')
        insta_dp()
insta_dp()