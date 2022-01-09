mport threading
def f4f():
    from scratchclient import ScratchSession
    from random import randint
    from time import sleep

    s = ScratchSession('ImIsNotGagarinten', 'kajismy228friend')
    for i in range(100):
        for user in s.get_user("griffpatch").get_followers(offset=i+2*10):
            user.follow()
            for i in range(30):
                print('Posting... Attemps:'+str(i))
                user.post_comment("F4F Please! This Number For U: "+str(randint(0,545595446964695489)))
            print(user.username)


if name == "main":
    for i in range(1):
        p = threading.Thread(target=f4f)
        print("Запуск Ещё одного потока")
        p.start()
