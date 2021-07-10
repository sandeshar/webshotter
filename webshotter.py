from selenium import webdriver
import multiprocessing as mp
import numpy as np
import parms
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


# Prepare driver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options ,executable_path=GeckoDriverManager().install())

args = parms.args

domains = np.array(open(args.filename).read().splitlines())

domains = np.array_split(domains, 3)


def take_shot(a):
    for y in domains[int(a)]:
        try:
            print("[+] Trying to screenshot: ",y)
            driver.get(formaturl(y))
            rem = ["https://", "http://"]
            path = f"{args.output}/{y}.png"
            for strToReplace in rem:
                path = path.replace(strToReplace, "")
            driver.save_screenshot(path)
        except:
            print("[--]Failed to screen shot: ",y)
        else:
            print("Success ",y)
    driver.quit()


def start_task():
    t1 = mp.Process(target=take_shot, args=(str(0)))
    t2 = mp.Process(target=take_shot, args=(str(1)))
    t3 = mp.Process(target=take_shot, args=(str(2)))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("[++] Finished")
    driver.quit()


def formaturl(url):
    if("https://" not in url):
        if("http://" not in url):
            return "http://" + url
        else:
            return url
    else:
        return url


if __name__ == '__main__':
    start_task()
