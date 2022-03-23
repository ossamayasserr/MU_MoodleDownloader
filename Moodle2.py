from moodle_functions import OpenBrowser, LoginMoodle, ListCourses, ParseWeeks, DownloadedLinks, ListNotDownloaded, Exit, StartDownload, cd_realpath, MakeDownloadFolder

### MAIN ###
courses_dir_path = "D:/College/"
tmp_dl_dir = MakeDownloadFolder(courses_dir_path)
cd_realpath()
driver = OpenBrowser(dl_dir=tmp_dl_dir)  # Run the browser
LoginMoodle(driver)     # Get MyU then sign in then E-paltform


if input("Get Courses Info?(y/N) --> ").strip().lower() == 'y': pass
else: Exit(driver)

courses = ListCourses(driver)     # Print the courses I have on Moodle
downloaded_links = DownloadedLinks() # Get the links of downloaded files in a list(downloaded_links)
all_data = ParseWeeks(courses, driver, downloaded_links)
not_downloaded_nodes = ListNotDownloaded(all_data, downloaded_links)
while True:
    q1 = input("Start downloading?(Y/N) --> ").strip().lower()
    if q1 in ['y', 'yes']:
        StartDownload(all_data, not_downloaded_nodes, driver, courses_dir_path)
    elif q1 in ['n', 'no']:
        break


# for line in lines[63:500]:
#     print("Getting", line)
#     driver.get(line)
#     input("Next?")

# import requests
# link = "https://vc1.mans.edu.eg/moodle2022/mod/url/view.php?id=105"
# link = "https://vc1.mans.edu.eg/moodle2022/mod/resource/view.php?id=9686"
# link = "https://vc1.mans.edu.eg/moodle2022/pluginfile.php/65917/mod_resource/content/1/POM Lecture 7 .mp4"

# with open("C:/Users/elkeb/Desktop/text.html", 'w', encoding='utf-8') as f:
#     r = requests.get(link, cookies={'MoodleSession':'iflnd5vk0bo2g9jn22dsdnijng'})
#     r = requests.head(link, cookies={'MoodleSession':'iflnd5vk0bo2g9jn22dsdnijng'})
#     f.write(r.text)
# import pySmartDL
# pySmartDL.SmartDL(link).start()
# r.status_code
# r.history
# r.headers['Location']
# r.url
# r.text[:500]

# all_a = driver.find_elements_by_tag_name("a")
# print(len(all_a))
# resource_link = driver.find_element_by_class_name("urlworkaround")
# resource_link = resource_link.find_element_by_tag_name('a').text
# print(resource_link)

Exit(driver)