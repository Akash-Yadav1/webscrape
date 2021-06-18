from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.youtube.com/c/JohnWatsonRooney/videos')

videos = browser.find_elements_by_class_name(
    'style-scope ytd-grid-video-renderer')
video_list = []
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[2]').text
    vid_item = {'Title': title, 'Views': views, 'date': when}
    video_list.append(vid_item)
browser.quit()
df = pd.DataFrame(video_list)
print(df)
