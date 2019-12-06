from selenium import webdriver
import time
import os


def dwn(fileid):
    url = 'https://drive.google.com/uc?export=download&id='+fileid
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.refresh()


def all(name, fileid):
    dwn(fileid)
    for file in os.listdir("/Users/apple/Downloads"):
        if not file.startswith('.'):
            filen, extension = os.path.splitext(file)
            os.rename("/Users/apple/Downloads/"+file,
                      "/Users/apple/Developer/id card/Driver/photo/"+name+extension)
    return "/Users/apple/Developer/id card/Driver/photo/"+name+extension
