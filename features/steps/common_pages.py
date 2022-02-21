
from google_search_page import *


def verify_particular_page(driver, page):
    temp_variable = ''
    print("value passed is :- ", page)
    if page == 'FILM':
        temp_variable = 'Film'
    elif page == 'TELEVISION':
        temp_variable = 'Television'
    elif page == 'WEB SERIES':
        temp_variable = 'Web Series'
    elif page == 'INTERVIEWS':
        temp_variable = 'Interviews'
    print("inside function verify particular page")
    var_link = driver.find_element(By.XPATH, "//a[normalize-space()='"+page+"']")
    assert var_link.is_displayed(), temp_variable+" link is not displayed in the navigation bar"
    var_link.click()
    title = temp_variable+" - SHADOW & ACT"
    print(title)
    WebDriverWait(driver, 40).until(ec.title_is(title))
    assert driver.title == temp_variable+" - SHADOW & ACT", "title of the page "+page+" does not match"
    page_header = driver.find_element(By.XPATH, "//h1[normalize-space()='"+temp_variable+"']")
    assert page_header.is_displayed(), "header of the page "+temp_variable+" is not displayed"
    # verify_each_article(page, temp_variable)
    # verify_number_of_articles(temp_variable)
    # verify_final_article(page, temp_variable)
    # verify_footer_exists(page)


def verify_footer_exists(driver, page):
    print("in function verify_footer_exists")
    temp_footer = driver.find_element(By.XPATH, "//footer[@class='sa-footer bg-black text-white']")
    actions = ActionChains(driver)
    actions.move_to_element(temp_footer).perform()
    assert temp_footer.is_displayed(), "footer is not present for ShadowAndAct page :"+page


def verify_number_of_articles(driver, temp_variable):
    print("inside function verify_number_of_articles")
    temp_number = driver.find_elements(By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles are :- ", len(temp_number))
    assert len(temp_number) > 0, "Articles are not present for " + temp_variable + " page"
    load_more_stories_button = driver.find_element(By.XPATH, "//button[normalize-space()='Load More Stories']")
    load_more_stories_button.click()
    if temp_variable == "Interviews" or temp_variable == "Web Series":
        time.sleep(2)
    time.sleep(2)
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='Load More Stories']")))
    temp_number_post_click = driver.find_elements(
      By.XPATH,
      "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles after 'Load More Stories' button click are :- ", len(temp_number_post_click))
    assert len(temp_number_post_click) > len(temp_number), \
        "Articles are not appended post 'Load More Stories' button click for " + temp_variable + " page"


def verify_load_more(driver, number):
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='Load More Stories']")))
    load_more_stories_button = driver.find_element(By.XPATH, "//button[normalize-space()='Load More Stories']")
    if number == 12:
        print("when number of articles are :- ", number)
        actions = ActionChains(driver)
        actions.move_to_element(load_more_stories_button).perform()
    if number == 18:
        print("when number of articles are :- ", number)
        time.sleep(2)
        actions = ActionChains(driver)
        actions.move_to_element(load_more_stories_button).perform()
        # time.sleep(1)
        # driver.execute_script("arguments[0].scrollIntoView();", load_more_stories_button)
    load_more_stories_button.click()
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, "//button[normalize-space()='Load More Stories']")))


def verify_each_article(driver, page, temp_variable):
    print("inside function verify_each_article")
    temp_number = driver.find_elements(By.XPATH, "//div[@class='article-card d-flex flex-column col-4 col-desktop-4']")
    print("number of articles are :- ", len(temp_number))
    assert len(temp_number) > 0, "Articles are not present for "+temp_variable+" page"
    if len(temp_number) == 6:
        count = 0
    elif len(temp_number) == 12:
        count = 6
    elif len(temp_number) == 18:
        count = 12
    time.sleep(5)
    while count < len(temp_number):
        if len(temp_number) == 12 and count != 6:
            verify_load_more(driver, len(temp_number))
        # elif len(temp_number) == 18 and count != 12:
        #     verify_load_more(len(temp_number))
        #     # time.sleep(1)
        #     verify_load_more(len(temp_number))
        temp_string = str(count + 1)
        print("count : ", count)
        print("tempString : ", temp_string)
        temp_xpath_img = "(//div[@class='article-card d-flex flex-column col-4 col-desktop-4']/a/img)["+temp_string+"]"
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((
          By.XPATH, temp_xpath_img)))
        time.sleep(1)
        article_heading = driver.find_element(By.XPATH, temp_xpath_img)
        actions = ActionChains(driver)
        actions.move_to_element(article_heading).perform()
        article = article_heading.get_attribute("title")
        assert article_heading.is_displayed(), "Article heading is not displayed for: "+article+": article in page :" \
                                               + page
        print("article is :", article)
        image_present = driver.execute_script(
          "return arguments[0].complete && typeof arguments[0].naturalWidth "
          "!= \"undefined\" && arguments[0].naturalWidth > 0",
          article_heading)
        if image_present:
            print("Image displayed.")
        else:
            print("Image not displayed.")
            assert image_present, "image is not displayed for " + article
        category_str = "(//div[@class='article-card__categories'])["+temp_string+"]"
        temp_category = driver.find_element(By.XPATH, category_str)
        print("category is/are :", temp_category.text)
        assert temp_category.text is not None and \
               temp_category.text != "", "Category is not present for " + article + " article in page "+page
        author_str = "(//div[@class='article-card__meta d-flex']/a/span)["+temp_string+"]"
        temp_author = driver.find_element(By.XPATH, author_str)
        print("author is :", temp_author.text)
        assert temp_author.text is not None and \
               temp_author.text != "", "Author is not present for " + article + " article in page " + page
        date_str = "(//div[@class='article-card__meta d-flex']/p)["+temp_string+"]"
        temp_date = driver.find_element(By.XPATH, date_str)
        print("date is :", temp_date.text)
        assert temp_date.text is not None and \
               temp_date.text != "", "Date is not present for " + article + " article in page " + page
        driver.execute_script("arguments[0].click();", article_heading)
        print("clicked on article heading")
        WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
        time.sleep(2)
        if page == "WEB SERIES" or page == "TELEVISION":
            time.sleep(3)
        print("Current window title: " + driver.title)
        temp_str = driver.title
        temp = temp_str.split(' -')
        compare_1 = str(temp[0])
        compare_2 = article
        print("deduced string is :", compare_1)
        print("text string is :", compare_2)
        assert compare_1 == compare_2, \
            "for shadowandact.com in articles of the " \
            ""+page+", for :" + article + ": article , title text does not match"
        driver.back()
        temp_title = temp_variable+" - SHADOW & ACT"
        print("title is :- ", temp_title)
        WebDriverWait(driver, 40).until(ec.title_is(temp_title))
        count += 1
        if len(temp_number) == 18:
            break


def verify_final_article(driver, page, temp_variable):
    temp_string = "7"
    print("tempString : ", temp_string)
    temp_xpath_img = "(//div[@class='article-card d-flex flex-column col-4 col-desktop-4']/a/img)[" + temp_string + "]"
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((
      By.XPATH, temp_xpath_img)))
    time.sleep(4)
    article_heading = driver.find_element(By.XPATH, temp_xpath_img)
    actions = ActionChains(driver)
    actions.move_to_element(article_heading).perform()
    article = article_heading.get_attribute("title")
    assert article_heading.is_displayed(), "Article heading is not displayed for: " + article + ": article in page :" \
                                           + page
    print("article is :", article)
    image_present = driver.execute_script(
      "return arguments[0].complete && typeof arguments[0].naturalWidth "
      "!= \"undefined\" && arguments[0].naturalWidth > 0",
      article_heading)
    if image_present:
        print("Image displayed.")
    else:
        print("Image not displayed.")
        assert image_present, "image is not displayed for " + article
    category_str = "(//div[@class='article-card__categories'])[" + temp_string + "]"
    temp_category = driver.find_element(By.XPATH, category_str)
    print("category is/are :", temp_category.text)
    assert temp_category.text is not None and \
           temp_category.text != "", "Category is not present for " + article + " article in page " + page
    author_str = "(//div[@class='article-card__meta d-flex']/a/span)[" + temp_string + "]"
    temp_author = driver.find_element(By.XPATH, author_str)
    print("author is :", temp_author.text)
    assert temp_author.text is not None and \
           temp_author.text != "", "Author is not present for " + article + " article in page " + page
    date_str = "(//div[@class='article-card__meta d-flex']/p)[" + temp_string + "]"
    temp_date = driver.find_element(By.XPATH, date_str)
    print("date is :", temp_date.text)
    assert temp_date.text is not None and \
           temp_date.text != "", "Date is not present for " + article + " article in page " + page
    driver.execute_script("arguments[0].click();", article_heading)
    print("clicked on article heading")
    WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH, "/html/head/title")))
    time.sleep(3)
    print("Current window title: " + driver.title)
    temp_str = driver.title
    temp = temp_str.split(' -')
    compare_1 = str(temp[0])
    compare_2 = article
    print("deduced string is :", compare_1)
    print("text string is :", compare_2)
    assert compare_1 == compare_2, "On" + page + "having article :" + article + ": , title text does not match"
    driver.back()
    temp_title = temp_variable + " - SHADOW & ACT"
    print("title is :- ", temp_title)
    WebDriverWait(driver, 40).until(ec.title_is(temp_title))


# environment()
# page_load()
# post_page_load_pop_up()
# verify_particular_page("FILM")
# verify_each_article("FILM", "Film")
# # to click load more 1 time
# verify_number_of_articles("Film")
# verify_each_article("FILM", "Film")
# # to click load more 2 times
# verify_number_of_articles("Film")
# verify_number_of_articles("Film")
# verify_each_article("FILM", "Film")
# driver.quit()
# # verify_particular_page("TELEVISION")
# verify_particular_page("WEB SERIES")
# verify_particular_page("INTERVIEWS")
# verify_particular_page("INTERVIEWS")
# verify_each_article("INTERVIEWS", "Interviews")
# # to click load more 1 time
# verify_number_of_articles("Film")
# verify_each_article("INTERVIEWS", "Interviews")
# # to click load more 2 times
# verify_number_of_articles("Interviews")
# verify_number_of_articles("Interviews")
# verify_each_article("INTERVIEWS", "Interviews")
